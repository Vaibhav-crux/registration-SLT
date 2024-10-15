from PyQt5.QtWidgets import QLineEdit, QComboBox, QDateEdit
from app.style.default_styles import dark_mode_style, light_mode_style
from app.style.disabled_styles import disabled_style
from app.utils.mode_utils import is_dark_mode  # Assume this function checks the current mode

def update_fields_write_access(vehicle_type, fields):
    """
    Update the write access of the fields based on the selected vehicle type.

    :param vehicle_type: The selected type of vehicle.
    :param fields: A dictionary containing field names as keys and their corresponding QLineEdit/QComboBox/QDateEdit objects as values.
    """
    # Determine the current mode dynamically
    dark_mode = is_dark_mode()
    base_style = dark_mode_style if dark_mode else light_mode_style

    # Define the editable fields for each vehicle type
    editable_fields = {
        "TCT": ["rfid_tag", "vehicle_type", "vehicle_no", "do_number", "transporter", "driver_owner", "weighbridge_no", "calendar"],
        "PDV": ["rfid_tag", "vehicle_type", "vehicle_no", "driver_owner", "calendar", "section"],
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
            is_readonly = field_name not in fields_to_edit
            field_widget.setReadOnly(is_readonly)
            # Apply base style, then override with red border if read-only
            field_widget.setStyleSheet(base_style + (disabled_style if is_readonly else ""))
        elif isinstance(field_widget, QComboBox):
            is_enabled = field_name in fields_to_edit
            field_widget.setEnabled(is_enabled)
            # Apply base style and override with red border if disabled
            field_widget.setStyleSheet(base_style + (disabled_style if not is_enabled else ""))
