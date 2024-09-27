from PyQt5.QtWidgets import QDialog, QMessageBox
from app.ui.utilities.doMaintenance.editDoNumber.auth_edit_do_ui import setup_auth_edit_do_ui
from app.utils.frame_utils import apply_drop_shadow, center_window
from app.style.default_styles import dark_mode_style, button_style  # Import styles
from app.controllers.utilities.doMaintenance.check_user_creds import check_user_credentials  # Import credential check
from app.controllers.utilities.doMaintenance.fetch_do_details_controller import fetch_do_details  # Import fetch function
from app.services.utilities.doMaintenance.editDoNumber.edit_do_maintenance_service import EditDoMaintenanceWindow

class AuthEditDoWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit DO Authentication")
        self.setGeometry(100, 100, 400, 200)

        # Apply drop shadow and center the window
        apply_drop_shadow(self)
        center_window(self)

        # Set up the UI using the external setup function, and retrieve the buttons
        self.confirm_button, self.cancel_button = setup_auth_edit_do_ui(self)

        # Apply styles
        self.setStyleSheet(dark_mode_style)
        self.confirm_button.setStyleSheet(button_style)
        self.cancel_button.setStyleSheet(button_style)

        # Connect the buttons to their actions
        self.confirm_button.clicked.connect(self.confirm)
        self.cancel_button.clicked.connect(self.cancel)

    def confirm(self):
        username = self.username_input.text()
        password = self.password_input.text()
        do_number = self.do_number_input.text()  # Get the DO number

        # Perform authentication using the check_user_credentials function
        if check_user_credentials(username, password):
            # Fetch DO details before creating the EditDoMaintenanceWindow
            do_details = fetch_do_details(do_number)
            if do_details:
                self.accept()  # Close the dialog with an "Accepted" status
                # Open the Edit DO Maintenance window
                self.edit_do_window = EditDoMaintenanceWindow(do_number)
                self.edit_do_window.exec_()
            else:
                self.show_message("DO Number not found.")
        else:
            self.show_message("Authentication failed. Please try again.")

    def cancel(self):
        self.reject()  # Close the dialog with a "Rejected" status

    def show_message(self, message):
        QMessageBox.information(self, "Information", message)