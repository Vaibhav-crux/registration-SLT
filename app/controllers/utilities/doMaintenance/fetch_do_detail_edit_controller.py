from app.config.refreshSession import create_session
from app.models.doMaintenance import DoData

def fetch_do_details(do_number: str):
    """
    Searches for the given DO Number in the database.

    :param do_number: The DO Number to search for.
    :return: The DoData object if found, None otherwise.
    """
    session = create_session()
    try:
        result = session.query(DoData).filter_by(doNumber=do_number).first()
        return result  # Return the DoData object directly
    finally:
        session.close()