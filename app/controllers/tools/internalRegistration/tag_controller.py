from app.config.refreshSession import create_session
from app.models.allotedTags import AllotedTags

def fetch_tag_data(tag_value):
    """
    Fetches the tag data based on RFID or Vehicle Number.

    :param tag_value: The RFID tag or Vehicle Number to search for.
    :return: A dictionary containing the tag data or None if not found.
    """
    session = create_session()
    try:
        # Check if the value is an RFID tag or Vehicle Number
        tag_data = session.query(AllotedTags.rfidTag, AllotedTags.typeOfVehicle, AllotedTags.vehicleNumber).filter(
            (AllotedTags.rfidTag == tag_value) | (AllotedTags.vehicleNumber == tag_value)
        ).first()
        
        if tag_data:
            return {
                "rfidTag": tag_data.rfidTag,
                "typeOfVehicle": tag_data.typeOfVehicle,
                "vehicleNumber": tag_data.vehicleNumber,
            }
        return None
    except Exception as e:
        print(f"An error occurred while fetching tag data: {e}")
        return None
    finally:
        session.close()
