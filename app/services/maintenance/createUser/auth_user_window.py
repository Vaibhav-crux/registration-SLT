import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from app.ui.maintenance.createUser.auth_user_ui import AuthUserUI
from app.controllers.maintenance.user.check_user import check_user_credentials
from app.services.maintenance.createUser.create_user_window import CreateUserWindow

class AuthUserWindow(AuthUserUI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.resize(400, 100)  # Set the initial window size (width, height)
        self.center_window()  # Center the window on the screen

        self.create_user_window = None  # Initialize as None

        self.confirm_button.clicked.connect(self.confirm_action)
        self.cancel_button.clicked.connect(self.cancel_action)
    
    def confirm_action(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, 'Input Error', 'Please enter both username and password.')
            return
        
        try:
            # Use the utility function to check user credentials
            user = check_user_credentials(username, password)

            if user:
                # Open the CreateUserWindow
                self.create_user_window = CreateUserWindow()
                self.create_user_window.show()
                
                # Close the AuthUserWindow
                self.close()
            else:
                QMessageBox.warning(self, 'Login Failed', 'Invalid username or password.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {str(e)}')
    
    def cancel_action(self):
        self.username_input.clear()
        self.password_input.clear()

    def center_window(self):
        # Move this logic from import to a method for cleaner code
        from app.utils.frame_utils import center_window
        center_window(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthUserWindow()
    window.show()
    sys.exit(app.exec_())
