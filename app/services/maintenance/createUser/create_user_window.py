from PyQt5.QtWidgets import QDialog, QMessageBox
from app.controllers.maintenance.user.save_user_data import save_user_data
# Import the mode utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window
# Import the UI setup function
from app.ui.maintenance.createUser.create_user_ui import setup_ui

class CreateUserWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create User")
        self.setGeometry(100, 100, 400, 500)

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

    def submit(self):
        # Retrieve data from input fields using stored variables
        message = save_user_data(
            self.user_name.text(),
            self.password.text(),
            self.auth_type.currentText(),
            self.emp_id.text(),
            self.full_name.text(),
            self.email.text(),
            self.designation.text(),
            self.address.text(),
            self.mobile_number.text(),
            self.organisation.text()
        )

        # Display message to the user
        QMessageBox.information(self, "Result", message)

    def clear_fields(self):
        # Clear all input fields
        for widget in [self.user_name, self.password, self.emp_id, self.full_name,
                       self.email, self.designation, self.address, self.mobile_number,
                       self.organisation]:
            widget.clear()
