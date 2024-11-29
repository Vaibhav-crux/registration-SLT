from PyQt5.QtWidgets import QDialog, QMessageBox
from app.ui.utilities.doMaintenance.editDoNumber.edit_do_maintenance_ui import setup_edit_do_maintenance_ui
from app.controllers.utilities.doMaintenance.fetch_do_details_controller import fetch_do_details
from app.style.default_styles import dark_mode_style, button_style  # Import styles
from app.utils.frame_utils import apply_drop_shadow, center_window  # Import utility functions
from app.utils.mode_utils import is_dark_mode,set_dark_mode_title_bar,apply_mode_styles

dark_mode=is_dark_mode()

class EditDoMaintenanceWindow(QDialog):
    def __init__(self, do_number, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit DO Maintenance")
        self.setGeometry(100, 100, 600, 400)

        # Set the overall style for dark mode
        self.setStyleSheet(dark_mode_style)

        # Apply drop shadow effect
        apply_drop_shadow(self)

        apply_mode_styles(self)

        # Center the window on the screen
        center_window(self)

        # Fetch DO details
        do_details = fetch_do_details(do_number)

        if not do_details:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("DO Number not found.")
            msg_box.setWindowTitle("Error")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Warning(self, "Error", "DO Number not found.")
            self.reject()  # Reject the dialog instead of closing it
            return

        # Set up the UI
        self.save_button, self.cancel_button = setup_edit_do_maintenance_ui(self, do_details)

        # Apply button styles
        self.save_button.setStyleSheet(button_style)  # Set button style
        self.cancel_button.setStyleSheet(button_style)  # Set button style

        # Connect the buttons to their actions
        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.cancel)

    def save(self):
        # Logic to save the updated DO details
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("DO details saved successfully.")
        msg_box.setWindowTitle("Success")
        if dark_mode:
            msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
            set_dark_mode_title_bar(msg_box)
        msg_box.exec_()
        # QMessageBox.Information(self, "Success", "DO details saved successfully.")
        self.accept()  # Accept the dialog after saving

    def cancel(self):
        self.reject()  # Reject the dialog when cancelled