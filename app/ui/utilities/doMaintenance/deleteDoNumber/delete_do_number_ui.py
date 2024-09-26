from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from app.services.utilities.doMaintenance.deleteDoNumber.delete_do_number_service import DeleteDoNumberService
from app.utils.frame_utils import apply_drop_shadow, center_window
from app.style.default_styles import dark_mode_style, button_style

class DeleteDoNumberWindow(QDialog):

    def __init__(self, do_number, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Delete DO Number")
        self.setGeometry(100, 100, 400, 200)
        self.do_number = do_number

        # Initialize the UI components
        self.init_ui()

        # Connect buttons to actions
        self.connect_signals()

        # Apply drop shadow effect
        apply_drop_shadow(self)

        # Center the window
        center_window(self)

        # Apply widget styles
        self.apply_widget_styles()

    def init_ui(self):
        """ Initialize the UI components and layout """
        self.main_layout = QVBoxLayout()

        self.add_do_number_label()
        self.add_username_field()
        self.add_password_field()
        self.add_buttons()

        self.setLayout(self.main_layout)

    def add_do_number_label(self):
        """ Add the DO Number label to the layout """
        do_number_label = QLabel(f"You are deleting DO Number: {self.do_number}")
        do_number_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(do_number_label)

    def add_username_field(self):
        """ Add the username input field to the layout """
        username_layout = QHBoxLayout()
        username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        self.main_layout.addLayout(username_layout)

    def add_password_field(self):
        """ Add the password input field to the layout """
        password_layout = QHBoxLayout()
        password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        self.main_layout.addLayout(password_layout)

    def add_buttons(self):
        """ Add the confirm and cancel buttons to the layout """
        button_layout = QHBoxLayout()
        self.confirm_button = QPushButton("Confirm")
        self.cancel_button = QPushButton("Cancel")
        button_layout.addWidget(self.confirm_button)
        button_layout.addWidget(self.cancel_button)
        self.main_layout.addLayout(button_layout)

    def connect_signals(self):
        """ Connect the buttons to their respective slots """
        self.cancel_button.clicked.connect(self.reject)
        self.confirm_button.clicked.connect(self.confirm_delete)

    def confirm_delete(self):
        """ Handle the confirm delete action """
        username = self.username_input.text()
        password = self.password_input.text()

        success, message = DeleteDoNumberService.delete_do_number(self.do_number, username, password)

        if success:
            QMessageBox.information(self, "Success", message)
            self.accept()
        else:
            QMessageBox.warning(self, "Error", message)
            self.clear_inputs()

    def clear_inputs(self):
        """ Clear the username and password input fields and set focus to username input """
        self.username_input.clear()
        self.password_input.clear()
        self.username_input.setFocus()

    def apply_widget_styles(self):
        """ Apply the default dark mode styles to the widgets """
        self.username_input.setStyleSheet(dark_mode_style)
        self.password_input.setStyleSheet(dark_mode_style)
        self.confirm_button.setStyleSheet(button_style)
        self.cancel_button.setStyleSheet(button_style)