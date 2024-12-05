# app/services/tools/internalRegistration/internal_rfid_window_service.py
from PyQt5.QtWidgets import QDialog, QLineEdit, QComboBox, QDateEdit, QLabel, QPushButton,QWidget
from PyQt5.QtCore import Qt, QDate
# Import the mode utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window
# Import the UI setup function
from app.ui.toolsWindow.internalRfidTag.internal_rfid_ui import setup_ui
# Import the next entry focus function
# from app.services.tools.internalRegistration.next_entry_box_cursor_services import focus_next_enabled_widget
# Import the vehicle registration data function
from app.controllers.tools.internalRegistration.vehicle_registration_controller import fetch_vehicle_registration_data
# Import the alloted tag check function
from app.controllers.tools.internalRegistration.alloted_tag_controller import check_alloted_and_registered_status
from app.models.vehicleRegistration import VehicleTypeEnum
from datetime import datetime
from app.utils.cursor.entry_box import MyLineEdit

from app.utils.fetchRfidTag.fetchRfidTag import open_com_port,close_com_port

class InternalRegistrationWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Internal Registration")
        self.setGeometry(100, 100, 400, 500)
        apply_window_flags(self)
        apply_mode_styles(self)
        center_window(self)
        apply_drop_shadow(self)
        setup_ui(self)  # Set up UI and initialize widgets

        open_com_port()

        # Assign references to widgets using findChild
        self.rfid_tag = self.findChild(MyLineEdit, "rfid_tag")
        self.vehicle_type = self.findChild(QComboBox, "vehicle_type")
        self.vehicle_no = self.findChild(MyLineEdit, "vehicle_no")
        self.do_number = self.findChild(QComboBox, "do_number")
        self.transporter = self.findChild(MyLineEdit, "transporter")
        self.weighbridge_no = self.findChild(MyLineEdit, "weighbridge_no")
        self.driver_owner = self.findChild(MyLineEdit, "driver_owner")
        self.visit_purpose = self.findChild(MyLineEdit, "visit_purpose")
        self.place_to_visit = self.findChild(MyLineEdit, "place_to_visit")
        self.person_to_visit = self.findChild(MyLineEdit, "person_to_visit")
        self.calendar = self.findChild(QDateEdit, "calendar")
        self.section = self.findChild(MyLineEdit, "section")
        self.status_label = self.findChild(QLabel, "status_label")

        self.new_button = self.findChild(QPushButton, "New")
        self.fetch_button = self.findChild(QPushButton, "Fetch")

        if self.fetch_button:
            self.fetch_button.clicked.connect(self.on_fetch_button_clicked)

        self.show()
        if self.fetch_button:
            self.fetch_button.setFocus()

    def on_fetch_button_clicked(self):
        self.vehicle_type.setFocus()

    def keyPressEvent(self, event):
        def focus_next_enabled_widget(current_widget):
            # Gather all input widgets that are focusable and enabled
            focusable_widgets = [
                widget for widget in self.findChildren((QLineEdit, QComboBox, QDateEdit))
                if widget.isEnabled() and (not isinstance(widget, (QLineEdit, QDateEdit)) or not widget.isReadOnly())
            ]

            # new_button = self.findChild(QPushButton, "New")
            if current_widget in focusable_widgets:
                current_index = focusable_widgets.index(current_widget)

                # Calculate the next widget index TOV - 8 rest =6
                # next_index = (current_index + 1) % (len(focusable_widgets) + 1)  # +1 for the New button
                next_index = current_index + 1

                if next_index == (len(focusable_widgets)):  # If we reach the end of the focusable widgets
                    self.new_button.setFocus()  # Set focus to the New button
                else:
                    focusable_widgets[next_index].setFocus()  # Set focus to the next widget
            else:
                # If the current widget is not in the focusable list, set focus to the New button
                if self.new_button:
                    self.new_button.setFocus()

        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            current_widget = self.focusWidget()
            if isinstance(current_widget, MyLineEdit):
                tag_value = current_widget.text()
                tag_data = fetch_vehicle_registration_data(tag_value)
                
                # Check and update status label
                status, alloted_data = check_alloted_and_registered_status(self.rfid_tag.text(), self.vehicle_no.text())
                self.status_label.setText(f"Status: {status}")

                if alloted_data:
                    # Fill fields with data from AllotedTags if present
                    self.rfid_tag.setText(alloted_data.rfidTag)
                    self.vehicle_type.setCurrentText(alloted_data.typeOfVehicle.value)
                    self.vehicle_no.setText(alloted_data.vehicleNumber)
                elif tag_data:
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
                        print(f"{widget.objectName()}: {value if value else 'Empty'}")

                    set_field_value(self.rfid_tag, tag_data.get("rfidTag"))
                    set_field_value(self.vehicle_type, tag_data.get("typeOfVehicle"))
                    set_field_value(self.vehicle_no, tag_data.get("vehicleNumber"))
                    set_field_value(self.do_number, tag_data.get("doNumber"))
                    set_field_value(self.transporter, tag_data.get("transporter"))
                    set_field_value(self.weighbridge_no, tag_data.get("weighbridgeNo"))
                    set_field_value(self.driver_owner, tag_data.get("driverOwner"))
                    set_field_value(self.visit_purpose, tag_data.get("visitPurpose"))
                    set_field_value(self.place_to_visit, tag_data.get("placeToVisit"))
                    set_field_value(self.person_to_visit, tag_data.get("personToVisit"))
                    set_field_value(self.calendar, tag_data.get("validityTill"))
                    set_field_value(self.section, tag_data.get("section"))

                # Move focus to the next enabled widget
                focus_next_enabled_widget(current_widget)

            elif isinstance(current_widget, QComboBox):
                if current_widget.currentText():  # If there's a selected value, do not reset it
                    current_widget.setCurrentText(current_widget.currentText())  # Keep current value
                current_widget.showPopup()
                focus_next_enabled_widget(current_widget)

            else:
                focus_next_enabled_widget(current_widget)
        else:
            super().keyPressEvent(event)

    def closeEvent(self, event):
        """Handle the window close event."""
        close_com_port()  # Close the COM port
        event.accept() 
