from PyQt5.QtWidgets import QLineEdit, QComboBox, QDateEdit

def update_fields_write_access(vehicle_type, fields):
    """
    Update the write access of the fields based on the selected vehicle type.

    :param vehicle_type: The selected type of vehicle.
    :param fields: A dictionary containing field names as keys and their corresponding QLineEdit/QComboBox/QDateEdit objects as values.
    """
    # Define the editable fields for each vehicle type
    editable_fields = {
        "TCT": ["rfid_tag", "vehicle_type", "vehicle_no", "do_number", "transporter", "driver_owner", "weighbridge_no", "calendar"],
        "PDV": ["rfid_tag", "vehicle_type", "vehicle_no", "driver_owner", "calendar"],
        "TVV": ["rfid_tag", "vehicle_no", "vehicle_type", "driver_owner", "visit_purpose", "place_to_visit", "person_to_visit", "calendar"],
        "TOV": ["rfid_tag", "vehicle_type", "vehicle_no", "do_number", "transporter", "visit_purpose", "place_to_visit", "person_to_visit", "calendar"],
        "PCT": ["rfid_tag", "vehicle_type", "vehicle_no", "do_number", "transporter", "driver_owner", "weighbridge_no", "calendar"],
        "TDBEV": ["rfid_tag", "vehicle_type", "vehicle_no", "do_number", "transporter", "driver_owner", "weighbridge_no", "calendar"],
        "SCRAPE": ["rfid_tag", "vehicle_type", "vehicle_no", "do_number", "transporter", "driver_owner", "weighbridge_no", "calendar"],
    }

    # Get the editable fields for the selected vehicle type
    fields_to_edit = editable_fields.get(vehicle_type, [])

    # Enable or disable fields based on the selected vehicle type
    for field_name, field_widget in fields.items():
        if isinstance(field_widget, (QLineEdit, QDateEdit)):
            # Use setReadOnly for QLineEdit and QDateEdit
            field_widget.setReadOnly(field_name not in fields_to_edit)
        elif isinstance(field_widget, QComboBox):
            # Use setEnabled for QComboBox
            field_widget.setEnabled(field_name in fields_to_edit)
