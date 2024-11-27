from app.config.refreshSession import create_session
from app.models.allotedTags import AllotedTags
from app.models.vehicleRegistration import VehicleRegistration
from sqlalchemy import or_

def check_alloted_and_registered_status(rfid_tag, vehicle_no):
    session = create_session()
    try:
        # Check in AllotedTags
        alloted_tag = session.query(AllotedTags).filter(
            or_(
            AllotedTags.rfidTag == rfid_tag,
            AllotedTags.vehicleNumber == vehicle_no  if vehicle_no else False
        )).first()
        # alloted_tag = session.query(AllotedTags).filter(
        #     (AllotedTags.rfidTag == rfid_tag) | (AllotedTags.vehicleNumber == vehicle_no)
        # ).first()

        # Check in VehicleRegistration
        vehicle_registration = session.query(VehicleRegistration).filter(
            or_(
            VehicleRegistration.rfidTag == rfid_tag,
            VehicleRegistration.vehicleNumber == vehicle_no  if vehicle_no else False
        )).first()
        # vehicle_registration = session.query(VehicleRegistration).filter(
        #     (VehicleRegistration.rfidTag == rfid_tag) | (VehicleRegistration.vehicleNumber == vehicle_no)
        # ).first()

        if alloted_tag and vehicle_registration:
            return "Already alloted and registered", None
        elif alloted_tag and not vehicle_registration:
            return "Alloted but not registered", alloted_tag
        elif not alloted_tag and vehicle_registration:
            return "Not alloted but registered", None
        else:
            return "Not alloted not registered", None
    finally:
        session.close()
