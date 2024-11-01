from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QComboBox, QDateEdit
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
from app.utils.frame_utils import apply_drop_shadow, center_window
from app.ui.toolsWindow.internalRfidTag.editWindow.edit_window_ui import setup_edit_window_ui
from app.services.tools.internalRegistration.update_fields_write_access import update_edit_fields_write_access
from app.models.vehicleRegistration import VehicleRegistration
from app.config.refreshSession import create_session
from datetime import datetime
# edit_window_service.py
from app.controllers.tools.internalRegistration.update_registration_controller import update_vehicle_registration

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
            QMessageBox.information(self, "Success", message)
            self.accept()
        else:
            QMessageBox.critical(self, "Error", message)


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
