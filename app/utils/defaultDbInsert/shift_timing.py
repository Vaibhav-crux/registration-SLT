from app.config.refreshSession import create_session
from app.models.shiftTiming import ShiftTiming
from datetime import time

def automate_saving_default_shifts():
    session = create_session()
    
    # Check if any data already exists in the shift_timing table
    existing_shifts = session.query(ShiftTiming).count()
    
    if existing_shifts == 0:
        # If no data exists, insert the default shifts
        default_shifts = [
            ShiftTiming(shift_name="A Shift", from_time=time(6, 0, 0), to_time=time(13, 59, 59)),
            ShiftTiming(shift_name="B Shift", from_time=time(14, 0, 0), to_time=time(21, 59, 59)),
            ShiftTiming(shift_name="C Shift", from_time=time(22, 0, 0), to_time=time(5, 59, 59)),
        ]
        
        session.add_all(default_shifts)
        session.commit()
        print("Default shift timings have been inserted successfully.")
    
    session.close()
