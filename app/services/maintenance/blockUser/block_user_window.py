from PyQt5.QtWidgets import QDialog, QMessageBox, QComboBox, QLineEdit, QPushButton

# Import the mode utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window
# Import the UI setup function
from app.ui.maintenance.blacklistedUser.blacklisted_user_ui import setup_ui
# Import the change_blacklist_status function
from app.controllers.maintenance.blockUser.change_blacklist_status import change_blacklist_status

class BlockUserWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blacklist User")
        self.setGeometry(100, 100, 400, 300)

        # Apply utility functions
        apply_window_flags(self)
        apply_mode_styles(self)
        center_window(self)
        apply_drop_shadow(self)

        # Set up the UI using the external setup function
        setup_ui(self)

        # Get UI elements
        self.confirm_button = self.findChild(QPushButton, "Confirm")
        self.cancel_button = self.findChild(QPushButton, "Cancel")
        self.rfid_tag_input = self.findChild(QLineEdit, "RFID Tag")
        self.vehicle_no_input = self.findChild(QLineEdit, "Vehicle No")
        self.action_combo = self.findChild(QComboBox, "Action")

        # Connect button actions
        self.confirm_button.clicked.connect(self.confirm_action)
        self.cancel_button.clicked.connect(self.cancel_action)

    def confirm_action(self):
        rfid_tag = self.rfid_tag_input.text().strip()
        vehicle_no = self.vehicle_no_input.text().strip()
        action = self.action_combo.currentText()

        # Perform the blacklist status change
        message, success = change_blacklist_status(rfid_tag, vehicle_no, action)

        # Show the appropriate message box
        if success:
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.warning(self, "Error", message)

    def cancel_action(self):
        self.close()
