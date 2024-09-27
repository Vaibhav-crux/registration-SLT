from PyQt5.QtWidgets import QDialog, QMessageBox
from app.ui.utilities.doMaintenance.editDoNumber.edit_do_maintenance_ui import setup_edit_do_maintenance_ui
from app.controllers.utilities.doMaintenance.fetch_do_detail_edit_controller import fetch_do_details

# Edit window pop-up
class EditDoMaintenanceWindow(QDialog):
    def __init__(self, do_number, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit DO Maintenance")
        self.setGeometry(100, 100, 600, 400)

        # Fetch DO details
        do_details = fetch_do_details(do_number)
        if not do_details:
            QMessageBox.warning(self, "Error", "DO Number not found.")
            self.reject()  # Reject the dialog instead of closing it
            return

        # Set up the UI
        self.save_button, self.cancel_button = setup_edit_do_maintenance_ui(self, do_details)

        # Connect the buttons to their actions
        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.cancel)

    def save(self):
        # Logic to save the updated DO details
        # You will need to implement this based on your application's requirements
        QMessageBox.information(self, "Success", "DO details saved successfully.")
        self.accept()  # Accept the dialog after saving

    def cancel(self):
        self.reject()  # Reject the dialog when cancelled