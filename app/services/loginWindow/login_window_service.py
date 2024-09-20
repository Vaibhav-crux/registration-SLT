from app.controllers.login.fetch_user import check_username_exists, verify_user_credentials
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
from app.ui.loginWindow.login_window_ui import LoginWindowUI
from app.utils.background_utils import set_background_image
from app.utils.frame_utils import apply_drop_shadow

class FullScreenWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = LoginWindowUI(self)
        self.initUI()

    def initUI(self):
        # Set the initial background image
        set_background_image(self, "C:\\Users\\Vaibhav\\Downloads\\truck-digital-art-illustration.jpg")

        # Set up the floating card and the rest of the UI
        self.ui.setup_ui()

        # Show the window in full-screen mode
        self.showFullScreen()

    def close_window(self, event):
        self.close()

    def on_submit_clicked(self):
        # Get the text from the username input field
        username = self.ui.username_input.text().strip()

        # Check if the username is empty
        if not username:
            QApplication.beep()  # Beep sound if no text is provided
            return

        # Check if the username exists in the database
        if not check_username_exists(username):
            QApplication.beep()  # Beep sound if username doesn't exist
            self.ui.username_input.clear()  # Clear the username input field
            return

        # If username exists, prompt for password
        self.ui.login_prompt.setText(f"Welcome {username.upper()}")
        self.ui.username_input.clear()  # Clear the input field
        self.ui.username_input.setPlaceholderText("Password")
        self.ui.username_input.setEchoMode(QLineEdit.Password)  # Set input to password mode (hidden characters)

        # Check for password entry
        self.ui.username_input.returnPressed.disconnect()  # Disconnect previous signal
        self.ui.username_input.returnPressed.connect(lambda: self.on_password_entered(username))

    def on_password_entered(self, username):
        # Get the text from the password input field
        password = self.ui.username_input.text().strip()

        # Check if the password is empty
        if not password:
            QApplication.beep()  # Beep sound if no text is provided
            return

        # Verify the username and password against the database
        if verify_user_credentials(username, password):
            # Credentials are correct, proceed to the main window
            self.save_username_to_file(username)
            self.close()
            self.open_main_window(username)
        else:
            # Credentials are incorrect, beep and clear the password field
            QApplication.beep()
            self.ui.username_input.clear()  # Clear the password input field
            self.ui.username_input.setFocus()  # Set focus back to the password input field
    def save_username_to_file(self, username):
        # Save the username to a file named "activeUsername.txt"
        with open("activeUsername.txt", "w") as file:
            file.write(username)

    def open_main_window(self, username):
        from app.services.mainWindow.main_window_service import MainWindow  # Import here to avoid circular import
        self.main_window = MainWindow()
        self.main_window.show()

    def resizeEvent(self, event):
        # Update the background image when the window is resized
        set_background_image(self, "C:\\Users\\Vaibhav\\Downloads\\truck-digital-art-illustration.jpg")
        self.ui.reposition_frame()
