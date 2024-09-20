from PyQt5.QtWidgets import QDialog, QMessageBox, QGraphicsBlurEffect, QWidget
from PyQt5.QtCore import Qt
from app.ui.utilities.doMaintenance.CreateDo.new_do_maintenance_ui import setup_new_do_ui
from app.utils.mode_utils import apply_mode_styles 
from app.controllers.utilities.doMaintenance.check_user_creds import check_user_credentials

class AuthDoMaintenanceWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create DO Number")
        self.setGeometry(200, 200, 400, 200)
        self.parent_window = parent
        self.overlay = None

        apply_mode_styles(self)

        self.user_name_input, self.password_input, self.confirm_button, self.cancel_button = setup_new_do_ui(self)

        self.confirm_button.clicked.connect(self.on_confirm)
        self.cancel_button.clicked.connect(self.close)

    def showEvent(self, event):
        """
        This function is called when the window is about to be shown. 
        Apply the blur effect to the parent window here and create a transparent overlay.
        """
        if self.parent_window:
            self.apply_blur_effect(self.parent_window, blur_radius=10)  # Apply a blur effect with radius 10
            self.create_overlay(self.parent_window)  # Create a transparent overlay on the parent window
        super().showEvent(event)

    def closeEvent(self, event):
        """
        This function is called when the window is about to be closed.
        Remove the blur effect from the parent window and delete the overlay.
        """
        if self.parent_window:
            self.remove_blur_effect(self.parent_window)  # Remove the blur effect
            self.remove_overlay()  # Remove the overlay
        super().closeEvent(event)

    def apply_blur_effect(self, window, blur_radius=5):
        """
        Apply a blur effect to the given window.
        :param window: The PyQt window to apply the blur effect to.
        :param blur_radius: The radius of the blur (higher values mean more blur).
        """
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(blur_radius)
        window.setGraphicsEffect(blur_effect)

    def remove_blur_effect(self, window):
        """
        Remove the blur effect from the given window.
        :param window: The PyQt window to remove the blur effect from.
        """
        window.setGraphicsEffect(None)

    def create_overlay(self, parent_window):
        """
        Create a semi-transparent overlay on the parent window to enhance the blur effect.
        """
        self.overlay = QWidget(parent_window)
        self.overlay.setGeometry(parent_window.rect())  # Make it cover the entire window
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 120);")  # Semi-transparent black overlay
        self.overlay.setAttribute(Qt.WA_TransparentForMouseEvents)  # Allow clicks to pass through
        self.overlay.show()

    def remove_overlay(self):
        """
        Remove the semi-transparent overlay from the parent window.
        """
        if self.overlay:
            self.overlay.hide()
            self.overlay.deleteLater()  # Remove the widget from memory
            self.overlay = None

    def on_confirm(self):
        """
        Handles the logic when the Confirm button is clicked.
        """
        user_name = self.user_name_input.text()
        password = self.password_input.text()

        if not user_name or not password:
            QMessageBox.critical(self, "Input Error", "Both User Name and Password fields are required.")
            return

        if check_user_credentials(user_name, password):
            QMessageBox.information(self, "Success", "DO Number creation authorized!")
            self.accept()  # Close the window if the credentials are valid
        else:
            QMessageBox.critical(self, "Authentication Failed", "Invalid User Name or Password.")