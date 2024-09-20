from app.config.refreshSession import create_session
from app.models.shiftTiming import ShiftTiming

def update_shift_timing(shift_name, from_time, to_time):
    """
    Updates the shift timing in the database for a given shift.
    
    :param shift_name: The name of the shift (e.g., "A Shift").
    :param from_time: The updated start time for the shift.
    :param to_time: The updated end time for the shift.
    """
    session = create_session()

    try:
        # Fetch the shift timing record by shift_name
        shift_timing = session.query(ShiftTiming).filter_by(shift_name=shift_name).first()

        if not shift_timing:
            print(f"No shift found with name: {shift_name}")
            return False

        # Update the shift timing with the new values
        shift_timing.from_time = from_time
        shift_timing.to_time = to_time

        # Commit the changes
        session.commit()
        return True
    except Exception as e:
        print(f"Error updating shift timing: {e}")
        session.rollback()
        return False
    finally:
        session.close()
