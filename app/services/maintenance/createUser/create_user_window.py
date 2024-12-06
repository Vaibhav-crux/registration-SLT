from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QComboBox
from app.ui.maintenance.createUser.create_user_ui import setup_ui
from app.controllers.maintenance.user.save_user_data import save_user_data
# Import the mode utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window
# Import the UI setup function
from app.ui.maintenance.createUser.create_user_ui import setup_ui
from app.controllers.maintenance.user.delete_user import delete_user_by_username
from app.utils.mode_utils import is_dark_mode,set_dark_mode_title_bar
from app.utils.cursor.entry_box import MyLineEdit

dark_mode=is_dark_mode()

input_error = "Input Error"
class CreateUserWindow(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create User")
        self.setGeometry(100, 100, 400, 500)
        self.parent=parent

        # Apply window flags to remove the "?" and only show the close button
        apply_window_flags(self)

        # Apply the dark or light mode styles
        apply_mode_styles(self)

        # Center the window using frame_utils
        center_window(self)

        # Apply drop shadow using frame_utils
        apply_drop_shadow(self)

        # Store widget references
        widgets = setup_ui(self)

        self.user_name = widgets['user_name']
        self.password = widgets['password']
        self.auth_type = widgets['auth_type']
        self.emp_id = widgets['emp_id']
        self.full_name = widgets['full_name']
        self.email = widgets['email']
        self.designation = widgets['designation']
        self.address = widgets['address']
        self.mobile_number = widgets['mobile_number']
        self.organisation = widgets['organisation']

        # Buttons
        self.submit_button = widgets['submit_button']
        self.clear_button = widgets['clear_button']
        self.delete_button = widgets['delete_button']

        # Connect button actions
        self.submit_button.clicked.connect(self.submit)
        self.clear_button.clicked.connect(self.clear_fields)
        self.delete_button.clicked.connect(self.delete_user)

    def submit(self):
        # Retrieve data from input fields using stored variables
        username = self.user_name.text().strip()
        password = self.password.text().strip()
        full_name = self.full_name.text().strip()
        mobile_number = self.mobile_number.text().strip()
        designation = self.designation.text().strip()

        # Validate essential fields
        if not username or not password or not full_name or not designation:
            msg_box = QMessageBox(self.parent)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Please ensure username, password, designation and full name are filled out.")
            msg_box.setWindowTitle('Input Error')
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Warning(self, input_error, "Please ensure username, password, and full name are filled out.")
            return

        # Validate mobile number for 10 digits
        if len(mobile_number) != 10 or not mobile_number.isdigit():
            msg_box = QMessageBox(self.parent)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Please enter a valid 10-digit mobile number.")
            msg_box.setWindowTitle('Input Error')
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Warning(self, input_error, "Please enter a valid 10-digit mobile number.")
            return

        # If all validations pass, save the data
        message = save_user_data(
            username,
            password,
            self.auth_type.currentText(),
            self.emp_id.text().strip(),
            full_name,
            self.email.text().strip(),
            self.designation.text().strip(),
            self.address.text().strip(),
            mobile_number,
            self.organisation.text().strip()
        )

        # Display message to the user
        msg_box = QMessageBox(self.parent)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(message)
        msg_box.setWindowTitle('Result')
        if dark_mode:
            msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
            set_dark_mode_title_bar(msg_box)
        msg_box.exec_()
        # QMessageBox.Information(self, "Result", message)
        self.clear_fields()  # Clear inputs after successful save

    def clear_fields(self):
        # Clear all input fields
        for widget in [self.user_name, self.password, self.emp_id, self.full_name,
                       self.email, self.designation, self.address, self.mobile_number,
                       self.organisation]:
            widget.clear()

    def delete_user(self):
        username = self.user_name.text()
        if not username:
            msg_box = QMessageBox(self.parent)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Please enter a username to delete.")
            msg_box.setWindowTitle('Input Error')
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Warning(self, input_error, "Please enter a username to delete.")
            return

        # Confirm deletion
        msg_box = QMessageBox(self.parent)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText(f"Are you sure you want to delete the user '{username}'?")
        msg_box.setWindowTitle("Confirm Delete")
        if dark_mode:
            msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
            set_dark_mode_title_bar(msg_box)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm = msg_box.exec_()
        # confirm = QMessageBox.Question(self, "Confirm Delete", f"Are you sure you want to delete the user '{username}'?",
                                    #    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if confirm == QMessageBox.Yes:
            # Call the function to delete user
            message = delete_user_by_username(username)
            msg_box = QMessageBox(self.parent)
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(message)
            msg_box.setWindowTitle('Result')
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Information(self, "Result", message)
            self.clear_fields()  # Clear inputs after successful delete