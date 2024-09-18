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

        # Convert the username to uppercase and update the "Sign In" label
        self.ui.login_prompt.setText(f"Welcome {username.upper()}")

        # Change the placeholder text of the input field to "Password"
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

        # Save the username to a file before opening the MainWindow
        self.save_username_to_file(username)

        # Close the FullScreenWindow
        self.close()

        # Now open the MainWindow
        self.open_main_window(username)

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
