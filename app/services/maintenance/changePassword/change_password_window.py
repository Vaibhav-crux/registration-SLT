from PyQt5.QtWidgets import QDialog, QMessageBox, QPushButton
from app.ui.maintenance.changePassword.change_password_ui import setup_ui
from app.controllers.maintenance.passwordChange.check_user import check_user_auth
from app.utils.cursor.entry_box import MyLineEdit
from app.services.maintenance.changePassword.editDetails.auth_edit_details_window import AuthEditDetailsWindow

# Correct import paths for utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags,is_dark_mode,set_dark_mode_title_bar
from app.utils.frame_utils import apply_drop_shadow, center_window

dark_mode=is_dark_mode()

class ChangePasswordWindow(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Change Credentials")
        self.setGeometry(100, 100, 400, 300)
        self.parent=parent

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

        # Check if the user exists and is authorized
        exists, is_authorized = check_user_auth(username)

        if not exists:
            msg_box = QMessageBox(self.parent)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("User not found.")
            msg_box.setWindowTitle("Error")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Warning(self, "Error", "User not found.")
            return

        if not is_authorized:
            msg_box = QMessageBox(self.parent)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("User is not authorized to change credentials.")
            msg_box.setWindowTitle("Error")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Warning(self, "Error", "User is not authorized to change credentials.")
            return

        # Close the current ChangePasswordWindow
        self.close()

        # Open the AuthEditDetailsWindow with the username and password
        self.auth_edit_details_window = AuthEditDetailsWindow(username,self.parent)
        self.auth_edit_details_window.exec_()


    def cancel_action(self):
        # Logic to clear fields or close the dialog
        self.username_input.clear()
        self.password_input.clear()
