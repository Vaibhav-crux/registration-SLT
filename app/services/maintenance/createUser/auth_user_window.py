import sys
from PyQt5.QtWidgets import QApplication, QMessageBox,QDialog,QPushButton
from app.ui.maintenance.createUser.auth_user_ui import setup_ui
from app.utils.cursor.entry_box import MyLineEdit
from app.controllers.maintenance.user.check_user import check_user_credentials
from app.services.maintenance.createUser.create_user_window import CreateUserWindow
from app.utils.mode_utils import is_dark_mode,set_dark_mode_title_bar
# Correct import paths for utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags,is_dark_mode,set_dark_mode_title_bar
from app.utils.frame_utils import apply_drop_shadow, center_window

dark_mode=is_dark_mode()

class AuthUserWindow(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Authorize User")
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
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     self.resize(400, 100)  # Set the initial window size (width, height)
    #     self.center_window()  # Center the window on the screen

    #     self.create_user_window = None  # Initialize as None

    #     self.confirm_button.clicked.connect(self.confirm_action)
    #     self.cancel_button.clicked.connect(self.cancel_action)
    
    def confirm_action(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if not username or not password:
            msg_box = QMessageBox(self.parent)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText('Please enter both username and password.')
            msg_box.setWindowTitle('Input Error')
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Warning(self, 'Input Error', 'Please enter both username and password.')
            return
        
        try:
            # Use the utility function to check user credentials
            user = check_user_credentials(username, password)

            if user:
                # Open the CreateUserWindow
                self.create_user_window = CreateUserWindow(self.parent)
                self.create_user_window.show()
                
                # Close the AuthUserWindow
                self.close()
            else:
                msg_box = QMessageBox(self.parent)
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText('Invalid username or password.')
                msg_box.setWindowTitle('Login Failed')
                if dark_mode:
                    msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                    set_dark_mode_title_bar(msg_box)
                msg_box.exec_()

                # QMessageBox.Warning(self, 'Login Failed', 'Invalid username or password.')
        except Exception as e:
            msg_box = QMessageBox(self.parent)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText(f'An error occurred: {str(e)}')
            msg_box.setWindowTitle("Error")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Critical(self, 'Error', f'An error occurred: {str(e)}')
        self.close()

    def cancel_action(self):
        self.username_input.clear()
        self.password_input.clear()

    # def center_window(self):
    #     # Move this logic from import to a method for cleaner code
    #     from app.utils.frame_utils import center_window
    #     center_window(self)

    # def closeEvent(self, event):
    #     """Override closeEvent to resume the inactivity timer."""
    #     super().closeEvent(event)
    #     self.parent().resume_inactivity_timer()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = AuthUserWindow()
#     window.show()
#     sys.exit(app.exec_())
