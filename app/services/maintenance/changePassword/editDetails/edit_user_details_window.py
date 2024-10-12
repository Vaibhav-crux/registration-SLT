from PyQt5.QtWidgets import QDialog, QMessageBox
from app.ui.maintenance.changePassword.EditDetails.edit_user_details_ui import setup_ui
from app.utils.frame_utils import center_window
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
from app.style.default_styles import dark_mode_style, light_mode_style, button_style
from app.utils.mode_utils import is_dark_mode
from app.controllers.maintenance.passwordChange.save_updated_details import update_user_details

class EditUserDetailsWindow(QDialog):
    def __init__(self, user):
        super().__init__()
        self.user = user

        # Set the fixed size of the window
        self.setFixedSize(500, 400)

        # Set up the UI
        setup_ui(self)

        # Center the window
        center_window(self)

        # Apply mode styles and window flags
        apply_mode_styles(self)
        apply_window_flags(self)

        # Populate the fields with user data
        self.populate_user_details()

        # Apply styles based on the mode
        self.apply_styles()

        # Connect buttons to their actions
        self.save_button.clicked.connect(self.save_user_details)
        self.cancel_button.clicked.connect(self.reject)

    def apply_styles(self):
        # Determine the mode style
        mode_style = dark_mode_style if is_dark_mode() else light_mode_style

        # Apply styles to text boxes
        self.password_input.setStyleSheet(mode_style)
        self.fullname_input.setStyleSheet(mode_style)
        self.email_input.setStyleSheet(mode_style)
        self.mobile_input.setStyleSheet(mode_style)
        self.address_input.setStyleSheet(mode_style)

        # Apply styles to buttons
        self.save_button.setStyleSheet(button_style)
        self.cancel_button.setStyleSheet(button_style)

    def populate_user_details(self):
        self.password_input.setText(self.user.password)
        self.fullname_input.setText(self.user.fullName or "")
        self.email_input.setText(self.user.email or "")
        self.mobile_input.setText(self.user.mobileNumber or "")
        self.address_input.setText(self.user.Address or "")

    def save_user_details(self):
        # Gather all user details
        password = self.password_input.text().strip()
        fullname = self.fullname_input.text().strip()
        email = self.email_input.text().strip()
        mobile = self.mobile_input.text().strip()
        address = self.address_input.text().strip()

        # Call the function to update user details
        success, message = update_user_details(self.user.id, password, fullname, email, mobile, address)

        if success:
            QMessageBox.information(self, "Success", message)
            self.accept()
        else:
            QMessageBox.warning(self, "Error", message)