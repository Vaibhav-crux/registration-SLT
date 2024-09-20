from app.config.refreshSession import create_session
from app.models.shiftTiming import ShiftTiming  # Assuming the model is defined here

def get_shift_timings():
    """
    Fetches the shift timing data from the ShiftTiming table.

    :return: A dictionary with the shift name as the key and a tuple (from_time, to_time) as the value.
    """
    session = create_session()
    shift_timings = session.query(ShiftTiming).all()
    
    shift_data = {}
    for shift in shift_timings:
        shift_data[shift.shift_name] = (shift.from_time, shift.to_time)

    session.close()
    return shift_data
