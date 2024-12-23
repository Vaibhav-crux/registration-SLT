from PyQt5.QtWidgets import QDialog, QMessageBox
from app.ui.maintenance.changePassword.EditDetails.auth_edit_details_ui import setup_ui
from app.utils.frame_utils import center_window
from app.utils.mode_utils import apply_mode_styles, apply_window_flags, is_dark_mode,set_dark_mode_title_bar
from app.style.default_styles import dark_mode_style, light_mode_style, button_style

from app.services.maintenance.changePassword.editDetails.edit_user_details_window import EditUserDetailsWindow
from app.controllers.maintenance.passwordChange.edit_check_user import check_user_credentials
from app.controllers.mainWindow.fetch_user_full_name import get_username_from_file

dark_mode=is_dark_mode()

class AuthEditDetailsWindow(QDialog):
    def __init__(self, username,parent=None):
        super().__init__(parent)
        self.username = username
        self.parent=parent

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
        self.confirm_button.setStyleSheet(button_style)
        self.cancel_button.setStyleSheet(button_style)

        # Connect buttons to their actions
        self.confirm_button.clicked.connect(self.confirm_action)  # Connect to the correct method
        self.cancel_button.clicked.connect(self.cancel_action)

    def clear_fields(self):
        # Clear the text fields when the window is opened
        self.username_input.clear()
        self.username_input.setText(get_username_from_file())

    def confirm_action(self):
        # Get the new username
        new_username = self.username_input.text().strip()

        # Check user credentials
        user = check_user_credentials(new_username)
        if user:
            # Open the EditUserDetailsWindow with the user object
            edit_window = EditUserDetailsWindow(user,self.parent)
            if edit_window.exec_() != QDialog.Accepted:
                msg_box = QMessageBox(self.parent)
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText("User detail update was cancelled.")
                msg_box.setWindowTitle("Error")
                if dark_mode:
                    msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                    set_dark_mode_title_bar(msg_box)
                msg_box.exec_()
                # QMessageBox.Warning(self, "Cancelled", "User detail update was cancelled.")

        else:
            # User credentials are incorrect
            msg_box = QMessageBox(self.parent)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("User does not exist.")
            msg_box.setWindowTitle("Error")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Warning(self, "Error", "User does not exist.")


    def cancel_action(self):
        # Simply close the dialog
        self.reject()
