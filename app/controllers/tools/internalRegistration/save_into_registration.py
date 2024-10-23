from app.models.vehicleRegistration import VehicleRegistration
from app.config.refreshSession import create_session

def check_existing_in_vehicle_registration(rfid_tag, vehicle_number):
    """Check if a record exists in VehicleRegistration."""
    db = create_session()
    try:
        existing_record = db.query(VehicleRegistration).filter(
            VehicleRegistration.rfidTag == rfid_tag,
            VehicleRegistration.vehicleNumber == vehicle_number
        ).first()
        return existing_record is not None
    finally:
        db.close()

def save_vehicle_registration(**kwargs):
    """
    Save the Vehicle Registration data into the database.

    :param **kwargs: Data to be saved into the VehicleRegistration table.
    """
    db = create_session()  # Create a new session using create_session

    try:
        # Create a VehicleRegistration instance with the given keyword arguments
        new_registration = VehicleRegistration(**kwargs)
        
        # Add and commit to the database
        db.add(new_registration)
        db.commit()
        db.refresh(new_registration)
        
        print("Vehicle registration saved successfully.")
        return new_registration
    except Exception as e:
        db.rollback()
        print(f"Error saving vehicle registration: {e}")
        raise
    finally:
        db.close()  # Ensure the session is closed
