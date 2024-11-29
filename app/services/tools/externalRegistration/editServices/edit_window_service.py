from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QComboBox, QDateEdit
from app.utils.mode_utils import apply_mode_styles, apply_window_flags,is_dark_mode,set_dark_mode_title_bar
from app.utils.frame_utils import apply_drop_shadow, center_window
from app.ui.toolsWindow.externalRfidTag.editWindow.edit_window_ui import setup_edit_window_ui
from app.services.tools.externalRegistration.update_fields_write_access import update_edit_fields_write_access
from app.models.vehicleRegistration import VehicleRegistration
from app.config.refreshSession import create_session
from datetime import datetime
# edit_window_service.py
from app.controllers.tools.internalRegistration.update_registration_controller import update_vehicle_registration

dark_mode=is_dark_mode()

class EditWindow(QDialog):
    def __init__(self, data, enabled_fields):
        super().__init__()
        self.setWindowTitle("Edit Registration")
        self.setGeometry(100, 100, 500, 400)
        
        apply_window_flags(self)
        apply_mode_styles(self)
        center_window(self)
        apply_drop_shadow(self)
        
        self.fields, self.confirm_button, self.cancel_button = setup_edit_window_ui(self, data, enabled_fields)
        self.enabled_fields = enabled_fields
        self.data = data

        self.confirm_button.clicked.connect(self.handle_confirm)
        self.cancel_button.clicked.connect(self.reject)

    def handle_confirm(self):
        """Update vehicle registration by calling the update controller."""
        success, message = update_vehicle_registration(self.data, self.fields)
        
        if success:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(message)
            msg_box.setWindowTitle("Success")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Information(self, "Success", message)
            self.accept()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText(message)
            msg_box.setWindowTitle("Error")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Critical(self, "Error", message)


def open_edit_window(data, vehicle_type):
    fields = {
        "driver_owner": QLineEdit(),
        "visit_purpose": QLineEdit(),
        "place_to_visit": QLineEdit(),
        "person_to_visit": QLineEdit(),
        "calendar": QDateEdit()
    }
    
    update_edit_fields_write_access(vehicle_type, fields)
    enabled_fields = [key for key, field in fields.items() if field.isEnabled()]

    dialog = EditWindow(data, enabled_fields)
    dialog.exec_()
