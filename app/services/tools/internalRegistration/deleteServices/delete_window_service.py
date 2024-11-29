# app/services/tools/internalRegistration/deleteServices/delete_window_service.py
from PyQt5.QtWidgets import QDialog, QMessageBox
# Import the mode utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window
# Import the UI setup function
from app.ui.toolsWindow.internalRfidTag.deleteWindow.delete_window_ui import setup_delete_window_ui
# Import user authentication functions
from app.controllers.auth.fetch_user import verify_user_credentials
# Import the delete function
from app.controllers.tools.internalRegistration.delete_registration_controller import delete_vehicle_registration
# Import mode utility function
from app.utils.mode_utils import is_dark_mode,set_dark_mode_title_bar

class DeleteWindow(QDialog):
    def __init__(self, rfid_tag, vehicle_no):
        super().__init__()
        self.setWindowTitle("Delete Confirmation")
        self.setGeometry(100, 100, 400, 300)
        
        # Apply window flags to remove the "?" and only show the close button
        apply_window_flags(self)
        # Apply the dark or light mode styles
        apply_mode_styles(self)
        # Center the window using frame_utils
        center_window(self)
        # Apply drop shadow using frame_utils
        apply_drop_shadow(self)
        
        # Set up the UI using the external setup function
        self.user_id_input, self.password_input, self.confirm_button, self.cancel_button = setup_delete_window_ui(self, rfid_tag, vehicle_no)
        self.rfid_tag = rfid_tag
        self.vehicle_no = vehicle_no

        # Connect buttons to their respective functions
        self.confirm_button.clicked.connect(self.handle_confirm)
        self.cancel_button.clicked.connect(self.reject)

    def handle_confirm(self):
        # Check if the current mode is dark or light
        dark_mode = is_dark_mode()
        user_id = self.user_id_input.text()
        password = self.password_input.text()
        if user_id and password:
            if verify_user_credentials(user_id, password):
                if delete_vehicle_registration(self.rfid_tag, self.vehicle_no):
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setText("Data has been deleted successfully.")
                    msg_box.setWindowTitle("Success")
                    if dark_mode:
                        msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                        set_dark_mode_title_bar(msg_box)
                    msg_box.exec_()
                    self.accept()
                else:
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Warning)
                    msg_box.setText("Failed to delete the data. Please try again.")
                    msg_box.setWindowTitle("Warning")
                    if dark_mode:
                        msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                        set_dark_mode_title_bar(msg_box)
                    msg_box.exec_()
            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText("Invalid User ID or Password.")
                msg_box.setWindowTitle("Warning")
                if dark_mode:
                    msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                    set_dark_mode_title_bar(msg_box)
                msg_box.exec_()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Please enter both User ID and Password.")
            msg_box.setWindowTitle("Warning")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()

def open_delete_window(rfid_tag, vehicle_no):
    dialog = DeleteWindow(rfid_tag, vehicle_no)
    dialog.exec_()
