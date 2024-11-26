from PyQt5.QtWidgets import QLineEdit, QComboBox, QDateEdit
from app.style.default_styles import dark_mode_style, light_mode_style
from app.style.disabled_styles import disabled_style
from app.utils.mode_utils import is_dark_mode
from PyQt5.QtCore import QDate


def clear_field(field_widget):
    """Clear the value of a QLineEdit or QDateEdit widget."""
    if isinstance(field_widget, QLineEdit):
        field_widget.clear()  # Clear text fields
    elif isinstance(field_widget, QDateEdit):
        field_widget.setDate(QDate.currentDate())  # Reset calendar to current date


def apply_style(field_widget, base_style, disabled_style, is_readonly):
    """Apply the base style and disabled style if the field is read-only."""
    field_widget.setStyleSheet(base_style + (disabled_style if is_readonly else ""))


def handle_line_edit(field_name, field_widget, fields_to_edit, base_style):
    """Handle logic for QLineEdit and QDateEdit widgets."""
    is_readonly = field_name not in fields_to_edit
    field_widget.setReadOnly(is_readonly)

    if field_name not in ['rfid_tag', 'vehicle_no', 'vehicle_type']:
        clear_field(field_widget)

    apply_style(field_widget, base_style, disabled_style, is_readonly)


def handle_combo_box(field_name, field_widget, fields_to_edit, base_style):
    """Handle logic for QComboBox widgets."""
    is_enabled = field_name in fields_to_edit
    field_widget.setEnabled(is_enabled)

    if field_name not in ['vehicle_type']:
        field_widget.setCurrentIndex(-1)  # Deselect ComboBox items

    apply_style(field_widget, base_style, disabled_style, not is_enabled)


def update_fields_write_access(vehicle_type, fields):
    """
    Update the write access of the fields based on the selected vehicle type and clear unwanted fields.

    :param vehicle_type: The selected type of vehicle.
    :param fields: A dictionary containing field names as keys and their corresponding QLineEdit/QComboBox/QDateEdit objects as values.
    """
    # Determine the current mode dynamically
    dark_mode = is_dark_mode()
    base_style = dark_mode_style if dark_mode else light_mode_style

    # Define the editable fields for each vehicle type
    editable_fields = {
        "TCT": ["vehicle_type", "vehicle_no", "do_number", "driver_owner", "calendar"],
        "PDV": ["vehicle_type", "vehicle_no", "driver_owner", "calendar", "section"],
        "TVV": ["vehicle_no", "vehicle_type", "driver_owner", "visit_purpose", "place_to_visit", "person_to_visit", "calendar"],
        "TOV": ["vehicle_type", "vehicle_no", "do_number", "visit_purpose", "place_to_visit", "person_to_visit", "calendar"],
        "PCT": ["vehicle_type", "vehicle_no", "do_number", "driver_owner", "calendar"],
        "TDBEV": ["vehicle_type", "vehicle_no", "do_number", "driver_owner", "calendar"],
        "SCRAPE": ["vehicle_type", "vehicle_no", "do_number", "driver_owner", "calendar"],
        # "TCT": ["rfid_tag", "vehicle_type", "vehicle_no", "do_number", "driver_owner", "calendar"],
        # "PDV": ["rfid_tag", "vehicle_type", "vehicle_no", "driver_owner", "calendar", "section"],
        # "TVV": ["rfid_tag", "vehicle_no", "vehicle_type", "driver_owner", "visit_purpose", "place_to_visit", "person_to_visit", "calendar"],
        # "TOV": ["rfid_tag", "vehicle_type", "vehicle_no", "do_number", "visit_purpose", "place_to_visit", "person_to_visit", "calendar"],
        # "PCT": ["rfid_tag", "vehicle_type", "vehicle_no", "do_number", "driver_owner", "calendar"],
        # "TDBEV": ["rfid_tag", "vehicle_type", "vehicle_no", "do_number", "driver_owner", "calendar"],
        # "SCRAPE": ["rfid_tag", "vehicle_type", "vehicle_no", "do_number", "driver_owner", "calendar"],
    }

    # Get the editable fields for the selected vehicle type
    fields_to_edit = editable_fields.get(vehicle_type, [])

    # Iterate through the fields and apply appropriate logic based on the widget type
    for field_name, field_widget in fields.items():
        if isinstance(field_widget, (QLineEdit, QDateEdit)):
            handle_line_edit(field_name, field_widget, fields_to_edit, base_style)
        elif isinstance(field_widget, QComboBox):
            handle_combo_box(field_name, field_widget, fields_to_edit, base_style)

def update_edit_fields_write_access(vehicle_type, fields):
    """
    Update write access for fields based on vehicle type.
    Sets all fields to read-only by default, enabling only those that
    are specified as editable for the selected vehicle type.
    :param vehicle_type: The selected type of vehicle.
    :param fields: A dictionary containing field names as keys and their corresponding QLineEdit/QComboBox/QDateEdit objects as values.
    """
    dark_mode = is_dark_mode()
    base_style = dark_mode_style if dark_mode else light_mode_style

    # Define the editable fields for each vehicle type
    editable_fields = {
        "TCT": ["driver_owner", "calendar"],
        "PDV": ["driver_owner", "calendar", "section"],
        "TVV": ["driver_owner", "visit_purpose", "place_to_visit", "person_to_visit", "calendar"],
        "TOV": ["visit_purpose", "place_to_visit", "person_to_visit", "calendar"],
        "PCT": ["driver_owner", "calendar"],
        "TDBEV": ["driver_owner", "calendar"],
        "SCRAPE": ["driver_owner", "calendar"],
    }

    # Get the list of fields that should be editable for the current vehicle type
    fields_to_edit = editable_fields.get(vehicle_type, [])

    # Iterate over all fields to set their editability
    for field_name, field_widget in fields.items():
        is_editable = field_name in fields_to_edit
        
        # Handle the read-only status and style based on whether the field is editable
        if isinstance(field_widget, (QLineEdit, QDateEdit)):
            field_widget.setReadOnly(not is_editable)
        elif isinstance(field_widget, QComboBox):
            field_widget.setEnabled(is_editable)
        
        # Apply styling based on the field's editability
        apply_style(field_widget, base_style, disabled_style, not is_editable)
