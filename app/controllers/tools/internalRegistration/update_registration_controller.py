# app/controllers/tools/internalRegistration/update_registration_controller.py
from app.config.refreshSession import create_session
from app.models.vehicleRegistration import VehicleRegistration
from sqlalchemy.exc import SQLAlchemyError

def update_vehicle_registration(updated_data):
    """Update the vehicle registration data."""
    session = create_session()
    try:
        registration_data = session.query(VehicleRegistration).filter_by(rfidTag=updated_data["rfidTag"]).one_or_none()
        
        if registration_data:
            for key, value in updated_data.items():
                setattr(registration_data, key, value)
            session.commit()
            return True
        else:
            return False
    except SQLAlchemyError as e:
        print(f"Error while updating vehicle registration: {e}")
        session.rollback()
        return False
    finally:
        session.close()
