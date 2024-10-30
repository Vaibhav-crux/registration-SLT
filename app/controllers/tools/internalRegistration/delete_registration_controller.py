# app/controllers/tools/internalRegistration/delete_registration_controller.py
from app.config.refreshSession import create_session
from app.models.vehicleRegistration import VehicleRegistration
from sqlalchemy.exc import SQLAlchemyError

def delete_vehicle_registration(rfid_tag, vehicle_no):
    """Delete the vehicle registration data for the given RFID tag and vehicle number."""
    session = create_session()
    try:
        # Attempt to find and delete the record
        registration_data = session.query(VehicleRegistration).filter_by(rfidTag=rfid_tag, vehicleNumber=vehicle_no).one_or_none()
        
        if registration_data:
            session.delete(registration_data)
            session.commit()
            return True
        else:
            return False
    except SQLAlchemyError as e:
        print(f"Error while deleting vehicle registration: {e}")
        session.rollback()
        return False
    finally:
        session.close()
