from PyQt5.QtWidgets import QDialog, QMessageBox, QPushButton
from app.ui.maintenance.changePassword.change_password_ui import setup_ui
from app.controllers.maintenance.passwordChange.check_user import check_user_auth
from app.utils.cursor.entry_box import MyLineEdit
from app.services.maintenance.changePassword.editDetails.auth_edit_details_window import AuthEditDetailsWindow

# Correct import paths for utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
from app.utils.frame_utils import apply_drop_shadow, center_window

class ChangePasswordWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Change Credentials")
        self.setGeometry(100, 100, 400, 300)

        # Apply utility functions
        apply_window_flags(self)
        apply_mode_styles(self)
        center_window(self)
        apply_drop_shadow(self)

        # Set up the UI
        setup_ui(self)

        # Connect the button actions
        self.confirm_button = self.findChild(QPushButton, "Confirm")
        self.cancel_button = self.findChild(QPushButton, "Cancel")
        self.username_input = self.findChild(MyLineEdit, "user_name")
        self.password_input = self.findChild(MyLineEdit, "password")

        self.confirm_button.clicked.connect(self.confirm_action)
        self.cancel_button.clicked.connect(self.cancel_action)

    def confirm_action(self):
        # Get the username and password from the input fields
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        # Check if the user exists and is authorized
        exists, is_authorized = check_user_auth(username)

        if not exists:
            QMessageBox.warning(self, "Error", "User not found.")
            return

        if not is_authorized:
            QMessageBox.warning(self, "Error", "User is not authorized to change credentials.")
            return

        # Close the current ChangePasswordWindow
        self.close()

        # Open the AuthEditDetailsWindow with the username and password
        self.auth_edit_details_window = AuthEditDetailsWindow(username, password)
        self.auth_edit_details_window.exec_()


    def cancel_action(self):
        # Logic to clear fields or close the dialog
        self.username_input.clear()
        self.password_input.clear()
