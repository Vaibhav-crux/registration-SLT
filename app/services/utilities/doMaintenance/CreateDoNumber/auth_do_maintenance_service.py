from PyQt5.QtWidgets import QDialog, QMessageBox
from app.ui.utilities.doMaintenance.CreateDo.auth_do_maintenance_ui import setup_new_do_ui
from app.utils.mode_utils import apply_mode_styles ,is_dark_mode,set_dark_mode_title_bar
from app.controllers.utilities.doMaintenance.check_user_creds import check_user_credentials
from app.services.utilities.doMaintenance.CreateDoNumber.create_do_maintenance_service import CreateDoMaintenanceWindow

dark_mode=is_dark_mode()

class AuthDoMaintenanceWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create DO Number")
        self.setGeometry(200, 200, 400, 200)
        self.parent = parent

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
            msg_box = QMessageBox(self.parent)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Both User Name and Password fields are required.")
            msg_box.setWindowTitle("Input Error")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Critical(self, "Input Error", "Both User Name and Password fields are required.")
            return

        if check_user_credentials(user_name, password):            
            self.close()
            create_do_window = CreateDoMaintenanceWindow(self.parent)
            create_do_window.show()
        else:
            msg_box = QMessageBox(self.parent)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Invalid User Name or Password.")
            msg_box.setWindowTitle("Authentication Failed")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Critical(self, "Authentication Failed", "Invalid User Name or Password.")