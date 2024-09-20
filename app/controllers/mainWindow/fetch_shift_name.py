from datetime import datetime, time
from sqlalchemy import or_, and_
from app.config.refreshSession import create_session
from app.models.shiftTiming import ShiftTiming

def fetch_shift_name():
    """Fetch the shift name based on the current time."""
    session = create_session()

    try:
        # Get the current time
        now = datetime.now().time()

        # Query the database to find the current shift
        # For shifts that cross midnight, we need to handle the range properly
        current_shift = session.query(ShiftTiming).filter(
            or_(
                # For normal shifts within the same day
                and_(ShiftTiming.from_time <= now, ShiftTiming.to_time >= now),
                # For shifts that go over midnight
                and_(ShiftTiming.from_time > ShiftTiming.to_time, or_(
                    ShiftTiming.from_time <= now,
                    ShiftTiming.to_time >= now
                ))
            )
        ).first()

        if current_shift:
            return current_shift.shift_name
        else:
            return "No Shift Available"  # If no matching shift is found, return a default value

    except Exception as e:
        print(f"Error fetching shift name: {e}")
        return "Unknown Shift"
    
    finally:
        session.close()
