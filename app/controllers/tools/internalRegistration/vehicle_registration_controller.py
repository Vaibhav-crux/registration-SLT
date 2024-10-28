# app/controllers/tools/internalRegistration/vehicle_registration_controller.py
from app.config.refreshSession import create_session
from app.models.vehicleRegistration import VehicleRegistration
from PyQt5.QtCore import QDate

def fetch_vehicle_registration_data(tag_value):
    """Fetches vehicle registration data based on RFID or Vehicle Number.
    :param tag_value: The RFID tag or Vehicle Number to search for.
    :return: A dictionary containing the vehicle registration data or None if not found.
    """
    session = create_session()
    try:
        # Attempt to find a record by RFID tag or vehicle number
        registration_data = session.query(VehicleRegistration).filter(
            (VehicleRegistration.rfidTag == tag_value) |
            (VehicleRegistration.vehicleNumber == tag_value)
        ).first()

        if registration_data:
            # Convert registration data to dictionary and ensure QDate conversion for date fields
            return {
                "rfidTag": registration_data.rfidTag,
                "typeOfVehicle": registration_data.typeOfVehicle,
                "vehicleNumber": registration_data.vehicleNumber,
                "doNumber": registration_data.doNumber,
                "transporter": registration_data.transporter,
                "weighbridgeNo": registration_data.weighbridgeNo,
                "driverOwner": registration_data.driverOwner,
                "visitPurpose": registration_data.visitPurpose,
                "placeToVisit": registration_data.placeToVisit,
                "personToVisit": registration_data.personToVisit,
                "validityTill": QDate.fromString(registration_data.validityTill, "yyyy-MM-dd") if registration_data.validityTill else None,
                "section": registration_data.section
            }
        else:
            return None
    finally:
        session.close()
