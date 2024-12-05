# app/ui/toolsWindow/internalRfidTag/internal_rfid_button_ui.py
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDateEdit, QMessageBox
from app.style.default_styles import button_style
from app.services.tools.internalRegistration.clear_fields_service import clear_fields
from app.services.tools.internalRegistration.newServices.open_new_window_service import open_new_window
from app.services.tools.internalRegistration.deleteServices.delete_window_service import open_delete_window
from app.services.tools.internalRegistration.editServices.edit_window_service import open_edit_window
from app.controllers.tools.internalRegistration.vehicle_registration_controller import fetch_vehicle_registration_data
from app.utils.fetchRfidTag.fetchRfidTag import fetch_rfid_tag
from app.controllers.tools.internalRegistration.alloted_tag_controller import check_alloted_and_registered_status
from app.models.vehicleRegistration import VehicleTypeEnum
from datetime import datetime
from PyQt5.QtCore import Qt, QDate
from app.utils.cursor.entry_box import MyLineEdit
# Import mode utility function
from app.utils.mode_utils import is_dark_mode,set_dark_mode_title_bar
# Import the function to update field write access based on vehicle type
from app.services.tools.internalRegistration.update_fields_write_access import check_null_fields
from app.controllers.tools.internalRegistration.alloted_tag_controller import get_alloted_tag
from app.services.tools.internalRegistration.newServices.open_new_window_alloted_service import open_new_alloted_window

def create_button_layout(window, fields):
    """
    Creates and returns a layout containing the 'New', 'Edit', 'Delete', and 'Clear' buttons.
    :param window: The QDialog window to set up the buttons on.
    :param fields: A dictionary of field widgets to manage.
    :return: QHBoxLayout with the buttons.
    """

    # Check if the current mode is dark or light
    dark_mode = is_dark_mode()
    button_layout = QHBoxLayout()

    # Function to handle "Fetch" button click
    def handle_fetch_button():
        rfid_tag=fetch_rfid_tag()
        fields["rfid_tag"].setText(rfid_tag)

        rfid_data = fetch_vehicle_registration_data(rfid_tag)

        if rfid_data:
            # Fill fields with data from VehicleRegistration if present
            def set_field_value(widget, value):
                if widget is None:
                    print(f"Warning: Widget not found.")
                    return
                if isinstance(widget, QComboBox):
                    if isinstance(value, VehicleTypeEnum):
                        value = value.value
                    widget.setCurrentText(value)
                elif isinstance(widget, QDateEdit):
                    if isinstance(value, QDate):
                        widget.setDate(value)
                    elif isinstance(value, datetime):
                        widget.setDate(value.date())
                elif isinstance(widget, MyLineEdit):
                    widget.setText(value if value else "")
                # print(f"{widget.objectName()}: {value if value else 'Empty'}")

            set_field_value(fields["vehicle_type"], rfid_data.get("typeOfVehicle"))
            set_field_value(fields["vehicle_no"], rfid_data.get("vehicleNumber"))
            set_field_value(fields["do_number"], rfid_data.get("doNumber"))
            set_field_value(fields["transporter"], rfid_data.get("transporter"))
            set_field_value(fields["weighbridge_no"], rfid_data.get("weighbridgeNo"))
            set_field_value(fields["driver_owner"], rfid_data.get("driverOwner"))
            set_field_value(fields["visit_purpose"], rfid_data.get("visitPurpose"))
            set_field_value(fields["place_to_visit"], rfid_data.get("placeToVisit"))
            set_field_value(fields["person_to_visit"], rfid_data.get("personToVisit"))
            set_field_value(fields["calendar"], rfid_data.get("validityTill"))
            set_field_value(fields["section"], rfid_data.get("section"))

            status, alloted_data = check_alloted_and_registered_status(fields["rfid_tag"].text(), fields["vehicle_no"].text())
            window.status_label.setText(f"Status: {status}")

            if alloted_data:
                # Fill fields with data from AllotedTags if present
                fields["vehicle_type"].setCurrentText(alloted_data.typeOfVehicle.value)
                fields["vehicle_no"].setText(alloted_data.vehicleNumber)

        else:
            for field_name, field_widget in fields.items():
                if isinstance(field_widget, MyLineEdit):
                    if field_name != 'vehicle_type' and field_name != "rfid_tag":
                        field_widget.clear()  # Clear text fields
                elif isinstance(field_widget, QDateEdit):
                    field_widget.setDate(QDate.currentDate())  # Reset calendar to current date
                elif isinstance(field_widget, QComboBox):
                    if field_name != 'vehicle_type':
                        field_widget.setCurrentIndex(-1)

            status, alloted_data = check_alloted_and_registered_status(fields["rfid_tag"].text(), fields["vehicle_no"].text())
            window.status_label.setText(f"Status: {status}")

            if alloted_data:
                # Fill fields with data from AllotedTags if present
                fields["vehicle_type"].setCurrentText(alloted_data.typeOfVehicle.value)
                fields["vehicle_no"].setText(alloted_data.vehicleNumber)

    # Function to handle "New" button click without checking for empty fields
    def handle_new_button():
        rfid_tag = fields["rfid_tag"].text()
        vehicle_no = fields["vehicle_no"].text()

        if not check_null_fields(fields["vehicle_type"].currentText(),fields):
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Please input all necessary fields.")
            msg_box.setWindowTitle("Warning")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()

        else:
            # Fetch data for RFID tag and vehicle number
            alloted_tag=get_alloted_tag(rfid_tag)
            rfid_data = fetch_vehicle_registration_data(rfid_tag)
            vehicle_data = fetch_vehicle_registration_data(vehicle_no)

            if alloted_tag and not rfid_data:
                open_new_alloted_window({
                    key: (field.text() if isinstance(field, MyLineEdit) else
                        field.currentText() if isinstance(field, QComboBox) else
                        field.date().toString("yyyy-MM-dd"))
                    for key, field in fields.items() if field.isEnabled()  # Collect only enabled fields
                })
            # Check if RFID tag exists
            elif alloted_tag and rfid_data:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText("RFID tag already registered.")
                msg_box.setWindowTitle("Warning")
                if dark_mode:
                    msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                    set_dark_mode_title_bar(msg_box)
                msg_box.exec_()
            else:
                open_new_window({
                    key: (field.text() if isinstance(field, MyLineEdit) else
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
            rfid_data = fetch_vehicle_registration_data(rfid_tag)

            if not rfid_data:
                for field_name, field_widget in fields.items():
                    if isinstance(field_widget, MyLineEdit):
                        if field_name != 'vehicle_type':
                            field_widget.clear()  # Clear text fields
                    elif isinstance(field_widget, QDateEdit):
                        field_widget.setDate(QDate.currentDate())  # Reset calendar to current date
                    elif isinstance(field_widget, QComboBox):
                        if field_name != 'vehicle_type':
                            field_widget.setCurrentIndex(-1)
                
                window.status_label.setText("Status: Please Enter Vehicle Number or RFID Tag")
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("The provided RFID tag or Vehicle No is not registered.")
            msg_box.setWindowTitle("Warning")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()

    # Function to handle "Edit" button click
    def handle_edit_button():
        # Gather the current data from the form fields
        data = {
            key: field.text() if isinstance(field, MyLineEdit) else
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

        # Fetch data for RFID tag and vehicle number
        rfid_data = fetch_vehicle_registration_data(data.get("rfid_tag", ""))
        vehicle_data = fetch_vehicle_registration_data(data.get("vehicle_no", ""))

        if rfid_data and vehicle_data:
            # Open the edit window with the complete data dictionary
            open_edit_window(data, vehicle_type)
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("The provided RFID tag or Vehicle No is not registered.")
            msg_box.setWindowTitle("Warning")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()

    # New Button
    fetch_button = QPushButton("Fetch", window)
    fetch_button.setFixedWidth(80)
    fetch_button.setObjectName("Fetch") 
    fetch_button.setStyleSheet(button_style)
    fetch_button.clicked.connect(handle_fetch_button)
    button_layout.addWidget(fetch_button)

    # New Button
    new_button = QPushButton("New", window)
    new_button.setFixedWidth(80)
    new_button.setObjectName("New") 
    new_button.setStyleSheet(button_style)
    new_button.clicked.connect(handle_new_button)
    button_layout.addWidget(new_button)

    # Edit Button
    edit_button = QPushButton("Edit", window)
    edit_button.setFixedWidth(80)
    edit_button.setStyleSheet(button_style)
    edit_button.clicked.connect(handle_edit_button)
    button_layout.addWidget(edit_button)

    # Delete Button
    delete_button = QPushButton("Delete", window)
    delete_button.setFixedWidth(80)
    delete_button.setStyleSheet(button_style)
    delete_button.clicked.connect(handle_delete_button)
    button_layout.addWidget(delete_button)

    # Clear Button
    clear_button = QPushButton("Clear", window)
    clear_button.setFixedWidth(80)
    clear_button.setStyleSheet(button_style)
    clear_button.clicked.connect(lambda: clear_fields(window,fields))
    button_layout.addWidget(clear_button)

    return button_layout

# E200470A93606821112F010E
# E2000020240502071950BA03