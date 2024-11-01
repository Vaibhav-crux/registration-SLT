# update_registration_controller.py
from app.models.vehicleRegistration import VehicleRegistration
from app.config.refreshSession import create_session
from datetime import datetime
from PyQt5.QtWidgets import QLineEdit

def update_vehicle_registration(data, fields):
    session = create_session()
    try:
        # Retrieve the record based on unique identifiers
        vehicle_registration = session.query(VehicleRegistration).filter_by(
            vehicleNumber=data['vehicle_no'],
            rfidTag=data['rfid_tag']
        ).first()

        if not vehicle_registration:
            print("Vehicle registration not found.")
            return False, "Vehicle registration not found."

        print("Original values:", {
            "driverOwner": vehicle_registration.driverOwner,
            "visitPurpose": vehicle_registration.visitPurpose,
            "placeToVisit": vehicle_registration.placeToVisit,
            "personToVisit": vehicle_registration.personToVisit,
            "validityTill": vehicle_registration.validityTill,
            "section": vehicle_registration.section,
        })

        # Map and update fields
        updatable_fields = {
            "driver_owner": "driverOwner",
            "visit_purpose": "visitPurpose",
            "place_to_visit": "placeToVisit",
            "person_to_visit": "personToVisit",
            "validity_till": "validityTill",
            "section": "section"
        }
        for key, field in fields.items():
            if key in updatable_fields:
                new_value = field.text() if isinstance(field, QLineEdit) else field.date().toString("yyyy-MM-dd")
                model_field = updatable_fields[key]
                print(f"Updating {model_field}: Old value = {getattr(vehicle_registration, model_field)}, New value = {new_value}")
                setattr(vehicle_registration, model_field, new_value)

        # Handle validityTill field specifically
        if "calendar" in fields:
            new_validity_till = fields["calendar"].date().toString("yyyy-MM-dd")
            print(f"Updating validityTill: Old value = {vehicle_registration.validityTill}, New value = {new_validity_till}")
            vehicle_registration.validityTill = new_validity_till

        # Commit the changes
        session.commit()
        return True, "Vehicle registration updated successfully."

    except Exception as e:
        session.rollback()
        print(f"Error during update: {str(e)}")
        return False, f"Failed to update vehicle registration: {str(e)}"

    finally:
        session.close()
