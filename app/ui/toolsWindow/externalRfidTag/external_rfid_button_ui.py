# app/ui/toolsWindow/externalRfidTag/external_rfid_button_ui.py
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDateEdit, QMessageBox
from app.style.default_styles import button_style
from app.services.tools.externalRegistration.clear_fields_service import clear_fields
from app.services.tools.externalRegistration.newServices.open_new_window_service import open_new_window
from app.services.tools.externalRegistration.deleteServices.delete_window_service import open_delete_window
from app.services.tools.externalRegistration.editServices.edit_window_service import open_edit_window
from app.controllers.tools.internalRegistration.vehicle_registration_controller import fetch_vehicle_registration_data
from app.utils.mode_utils import is_dark_mode,set_dark_mode_title_bar

dark_mode=is_dark_mode()

def create_button_layout(window, fields):
    """
    Creates and returns a layout containing the 'New', 'Edit', 'Delete', and 'Clear' buttons.
    :param window: The QDialog window to set up the buttons on.
    :param fields: A dictionary of field widgets to manage.
    :return: QHBoxLayout with the buttons.
    """
    button_layout = QHBoxLayout()

    # Function to handle "New" button click without checking for empty fields
    def handle_new_button():
        rfid_tag = fields["rfid_tag"].text()
        vehicle_no = fields["vehicle_no"].text()

        # Fetch data for RFID tag and vehicle number
        rfid_data = fetch_vehicle_registration_data(rfid_tag)
        vehicle_data = fetch_vehicle_registration_data(vehicle_no)

        # Check if RFID tag exists
        if rfid_data:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("RFID tag already registered.")
            msg_box.setWindowTitle("Warning")
            if dark_mode:
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
        else:
            open_new_window({
                key: (field.text() if isinstance(field, QLineEdit) else
                      field.currentText() if isinstance(field, QComboBox) else
                      field.date().toString("yyyy-MM-dd"))
                for key, field in fields.items() if field.isEnabled()  # Collect only enabled fields
            })

    # Function to handle "Delete" button click
    def handle_delete_button():
        rfid_tag = fields["rfid_tag"].text()
        vehicle_no = fields["vehicle_no"].text()

        # Fetch data for RFID tag and vehicle number
        rfid_data = fetch_vehicle_registration_data(rfid_tag)
        vehicle_data = fetch_vehicle_registration_data(vehicle_no)

        # Check if both RFID tag and vehicle number exist
        if rfid_data and vehicle_data:
            open_delete_window(rfid_tag, vehicle_no)
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("The provided RFID tag or Vehicle No is not registered.")
            msg_box.setWindowTitle("Warning")
            set_dark_mode_title_bar(msg_box)
            msg_box.exec_()

    # Function to handle "Edit" button click
    def handle_edit_button():
        # Gather the current data from the form fields
        data = {
            key: field.text() if isinstance(field, QLineEdit) else
                field.currentText() if isinstance(field, QComboBox) else
                field.date().toString("yyyy-MM-dd")  # Format the date correctly for "calendar" field
            for key, field in fields.items()
        }

        # Ensure vehicle_type is correctly formatted as a string
        vehicle_type = data.get("vehicle_type", "")

        if isinstance(vehicle_type, list):  # Just to ensure it's not a list
            vehicle_type = vehicle_type[0] if vehicle_type else ""

        # Add the "calendar" field's current date in a format expected by the edit window
        data["validity_till"] = fields["calendar"].date().toString("yyyy-MM-dd")

        # Open the edit window with the complete data dictionary
        open_edit_window(data, vehicle_type)



    # New Button
    new_button = QPushButton("New", window)
    new_button.setFixedWidth(100)
    new_button.setStyleSheet(button_style)
    new_button.clicked.connect(handle_new_button)
    button_layout.addWidget(new_button)

    # Edit Button
    edit_button = QPushButton("Edit", window)
    edit_button.setFixedWidth(100)
    edit_button.setStyleSheet(button_style)
    edit_button.clicked.connect(handle_edit_button)
    button_layout.addWidget(edit_button)

    # Delete Button
    delete_button = QPushButton("Delete", window)
    delete_button.setFixedWidth(100)
    delete_button.setStyleSheet(button_style)
    delete_button.clicked.connect(handle_delete_button)
    button_layout.addWidget(delete_button)

    # Clear Button
    clear_button = QPushButton("Clear", window)
    clear_button.setFixedWidth(100)
    clear_button.setStyleSheet(button_style)
    clear_button.clicked.connect(lambda: clear_fields(fields))
    button_layout.addWidget(clear_button)

    return button_layout
