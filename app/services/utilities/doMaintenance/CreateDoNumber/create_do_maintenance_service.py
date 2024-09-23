from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import Qt
from app.ui.utilities.doMaintenance.CreateDo.create_do_maintenance_ui import setup_create_do_ui
from app.utils.mode_utils import apply_mode_styles
from app.models.doMaintenance import DoData  # Import your DoMaintenance model
from app.config.refreshSession import create_session

class CreateDoMaintenanceWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create DO Maintenance")
        self.setGeometry(200, 200, 400, 250)
        self.parent_window = parent

        apply_mode_styles(self)

        self.do_number_input, self.transporter_input, self.save_button, self.clear_button = setup_create_do_ui(self)

        self.save_button.clicked.connect(self.on_save)
        self.clear_button.clicked.connect(self.on_clear)

    def on_save(self):
        """
        Handles the logic when the Save button is clicked.
        """
        do_number = self.do_number_input.text()
        transporter = self.transporter_input.text()

        if not do_number or not transporter:
            QMessageBox.critical(self, "Input Error", "Both DO Number and Transporter fields are required.")
            return

        session = create_session()
        try:
            # Create a new DoMaintenance object
            new_do = DoData(do_number=do_number, transporter=transporter)

            # Add the new object to the session
            session.add(new_do)

            # Commit the changes
            session.commit()

            QMessageBox.information(self, "Success", "DO Maintenance record saved successfully!")
            self.accept()  # Close the window after successful save
        except Exception as e:
            session.rollback()
            QMessageBox.critical(self, "Error", f"Failed to save DO Maintenance record: {str(e)}")
        finally:
            session.close()

    def on_clear(self):
        """
        Clears all input fields when the Clear button is clicked.
        """
        self.do_number_input.clear()
        self.transporter_input.clear()

    def closeEvent(self, event):
        """
        Override closeEvent to prompt user confirmation before closing.
        """
        reply = QMessageBox.question(self, 'Close Window', 'Are you sure you want to close this window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
