from app.config.refreshSession import create_session
from app.models.doMaintenance import DoData

def fetch_do_numbers():
    """
    Fetches the list of DO Numbers from the database.

    :return: A list of DO Numbers.
    """
    session = create_session()
    try:
        # Query the database for all DO Numbers
        do_numbers = session.query(DoData.doNumber).all()

        # Extract DO Numbers from the query result
        do_number_list = [do_number[0] for do_number in do_numbers]
        return do_number_list
    except Exception as e:
        print(f"An error occurred while fetching DO Numbers: {e}")
        return []
    finally:
        session.close()

def fetch_transport_and_weighbridge(do_number):
    """
    Fetches the transporter and weighbridge number for a given DO Number.

    :param do_number: The DO Number to search for.
    :return: A tuple containing (transporter, weighbridge_no) or (None, None) if not found.
    """
    session = create_session()
    try:
        # Query the database for the transporter and weighbridge number
        result = session.query(DoData.transporter, DoData.weighbridgeNo).filter(DoData.doNumber == do_number).first()
        if result:
            return result
        return None, None
    except Exception as e:
        print(f"An error occurred while fetching transporter and weighbridge: {e}")
        return None, None
    finally:
        session.close()