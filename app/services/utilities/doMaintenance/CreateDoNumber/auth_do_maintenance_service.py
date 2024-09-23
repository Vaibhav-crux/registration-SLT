from PyQt5.QtWidgets import QDialog, QMessageBox
from app.ui.utilities.doMaintenance.CreateDo.auth_do_maintenance_ui import setup_new_do_ui
from app.utils.mode_utils import apply_mode_styles 
from app.controllers.utilities.doMaintenance.check_user_creds import check_user_credentials
from app.services.utilities.doMaintenance.CreateDoNumber.create_do_maintenance_service import CreateDoMaintenanceWindow

class AuthDoMaintenanceWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create DO Number")
        self.setGeometry(200, 200, 400, 200)
        self.parent_window = parent

        apply_mode_styles(self)

        self.user_name_input, self.password_input, self.confirm_button, self.cancel_button = setup_new_do_ui(self)

        self.confirm_button.clicked.connect(self.on_confirm)
        self.cancel_button.clicked.connect(self.close)

    def showEvent(self, event):
        super().showEvent(event)

    def closeEvent(self, event):
        super().closeEvent(event)

    def on_confirm(self):
        user_name = self.user_name_input.text()
        password = self.password_input.text()

        if not user_name or not password:
            QMessageBox.critical(self, "Input Error", "Both User Name and Password fields are required.")
            return

        if check_user_credentials(user_name, password):            
            self.close()
            create_do_window = CreateDoMaintenanceWindow(parent=self.parent_window)
            create_do_window.show()
        else:
            QMessageBox.critical(self, "Authentication Failed", "Invalid User Name or Password.")