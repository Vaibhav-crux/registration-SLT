from PyQt5.QtWidgets import QDialog, QMessageBox
from app.ui.maintenance.changePassword.EditDetails.auth_edit_details_ui import setup_ui
from app.utils.frame_utils import center_window
from app.utils.mode_utils import apply_mode_styles, apply_window_flags, is_dark_mode
from app.style.default_styles import dark_mode_style, light_mode_style, button_style

# Import the necessary function
from app.controllers.maintenance.passwordChange.edit_check_user import check_user_credentials

class AuthEditDetailsWindow(QDialog):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

        # Set up the UI
        setup_ui(self)

        # Clear the fields initially
        self.clear_fields()

        # Center the window
        center_window(self)

        # Apply mode styles to the window
        apply_mode_styles(self)

        # Apply window flags
        apply_window_flags(self)

        # Apply styles to specific widgets based on the mode
        mode_style = dark_mode_style if is_dark_mode() else light_mode_style
        self.username_input.setStyleSheet(mode_style)
        self.password_input.setStyleSheet(mode_style)
        self.confirm_button.setStyleSheet(button_style)
        self.cancel_button.setStyleSheet(button_style)

        # Connect buttons to their actions
        self.confirm_button.clicked.connect(self.confirm_button)
        self.cancel_button.clicked.connect(self.cancel_action)

    def clear_fields(self):
        # Clear the text fields when the window is opened
        self.username_input.clear()
        self.password_input.clear()

    def confirm_button(self):
        # Get the new username and password from the input fields
        new_username = self.username_input.text().strip()
        new_password = self.password_input.text().strip()

        # Check if the user exists
        user = check_user_credentials(self.username, self.password)
        if user:
            # If the user exists, proceed with the update
            success = self.update_user_details(new_username, new_password)

            if success:
                QMessageBox.information(self, "Success", "User details confirmed successfully.")
                self.accept()
            else:
                QMessageBox.warning(self, "Error", "Failed to confirm user details.")
        else:
            # If the user does not exist, show a warning message
            QMessageBox.warning(self, "Error", "User does not exist or incorrect credentials.")

    def cancel_action(self):
        # Simply close the dialog
        self.reject()
