# app/services/tools/internalRegistration/editServices/edit_window_service.py
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QComboBox, QDateEdit
# Import the mode utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window
# Import the UI setup function
from app.ui.toolsWindow.internalRfidTag.editWindow.edit_window_ui import setup_edit_window_ui
# Import the update function
from app.controllers.tools.internalRegistration.update_registration_controller import update_vehicle_registration

from app.services.tools.internalRegistration.update_fields_write_access import update_edit_fields_write_access

class EditWindow(QDialog):
    def __init__(self, data, enabled_fields):
        super().__init__()
        self.setWindowTitle("Edit Registration")
        self.setGeometry(100, 100, 500, 400)
        
        # Apply window flags to remove the "?" and only show the close button
        apply_window_flags(self)
        # Apply the dark or light mode styles
        apply_mode_styles(self)
        # Center the window using frame_utils
        center_window(self)
        # Apply drop shadow using frame_utils
        apply_drop_shadow(self)
        
        # Set up the UI using the external setup function
        self.fields, self.confirm_button, self.cancel_button = setup_edit_window_ui(self, data, enabled_fields)
        self.enabled_fields = enabled_fields

        # Connect buttons to their respective functions
        self.confirm_button.clicked.connect(self.handle_confirm)
        self.cancel_button.clicked.connect(self.reject)

    def handle_confirm(self):
        updated_data = {key: field.text() if isinstance(field, QLineEdit) else
                        field.currentText() if isinstance(field, QComboBox) else
                        field.date().toString("yyyy-MM-dd") for key, field in self.fields.items() if field.isEnabled()}

        if update_vehicle_registration(updated_data):
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Data has been updated successfully.")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()
            self.accept()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Failed to update the data. Please try again.")
            msg_box.setWindowTitle("Warning")
            msg_box.exec_()

def open_edit_window(data, vehicle_type):
    # Determine the fields that should be enabled for the given vehicle type
    fields = {
        "driver_owner": QLineEdit(),
        "visit_purpose": QLineEdit(),
        "place_to_visit": QLineEdit(),
        "person_to_visit": QLineEdit(),
        "calendar": QDateEdit()
    }
    
    # This will give you the list of fields that can be edited
    update_edit_fields_write_access(vehicle_type, fields)
    enabled_fields = [key for key, field in fields.items() if field.isEnabled()]

    dialog = EditWindow(data, enabled_fields)
    dialog.exec_()
