from app.config.refreshSession import create_session
from app.models.vehicleRegistration import VehicleRegistration

def fetch_vehicle_registration_data(tag_value):
    """
    Fetches vehicle registration data based on RFID or Vehicle Number.

    :param tag_value: The RFID tag or Vehicle Number to search for.
    :return: A dictionary containing the vehicle registration data or None if not found.
    """
    session = create_session()
    try:
        registration_data = session.query(VehicleRegistration).filter(
            (VehicleRegistration.rfidTag == tag_value) | (VehicleRegistration.vehicleNumber == tag_value)
        ).first()
        
        if registration_data:
            # Print the data to debug
            print("Fetched Registration Data:", registration_data)
            return {
                "vehicleNumber": registration_data.vehicleNumber,
                "doNumber": registration_data.doNumber,
                "transporter": registration_data.transporter,
                "driverOwner": registration_data.driverOwner,
                "weighbridgeNo": registration_data.weighbridgeNo,
                "visitPurpose": registration_data.visitPurpose,
                "placeToVisit": registration_data.placeToVisit,
                "personToVisit": registration_data.personToVisit,
                "validityTill": registration_data.validityTill,
                "section": registration_data.section,
            }
        else:
            print("No registration data found for the given tag value.")
        return None
    except Exception as e:
        print(f"An error occurred while fetching vehicle registration data: {e}")
        return None
    finally:
        session.close()
