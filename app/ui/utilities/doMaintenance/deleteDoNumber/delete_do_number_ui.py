from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from app.services.utilities.doMaintenance.deleteDoNumber.delete_do_number_service import DeleteDoNumberService
from app.utils.frame_utils import apply_drop_shadow, center_window
from app.style.default_styles import dark_mode_style, button_style, light_mode_style
# Import mode utility function
from app.utils.mode_utils import is_dark_mode,set_dark_mode_title_bar,apply_mode_styles,apply_window_flags

# Check if the current mode is dark or light
dark_mode = is_dark_mode()

# Apply the appropriate stylesheet
if dark_mode:
    common_textbox_style = dark_mode_style
else:
    common_textbox_style = light_mode_style

class DeleteDoNumberWindow(QDialog):

    def __init__(self, do_number, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Delete DO Number")
        self.setGeometry(100, 100, 400, 200)
        apply_window_flags(self)
        apply_mode_styles(self)
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

        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)
        self.add_do_number_label()
        self.add_username_field()
        self.add_password_field()
        self.add_buttons()

        self.setLayout(self.main_layout)

    def add_do_number_label(self):
        """ Add the DO Number label to the layout """
        do_number_label = QLabel(f"You are deleting DO Number: {self.do_number}")
        do_number_label.setStyleSheet("font-size: 14px; font-weight: 600;")
        do_number_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(do_number_label)

    def add_username_field(self):
        """ Add the username input field to the layout """
        username_layout = QHBoxLayout()
        username_label = QLabel("Username:")
        username_label.setStyleSheet("font-size: 14px; font-weight: 600;")
        self.username_input = QLineEdit()
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        self.main_layout.addLayout(username_layout)

    def add_password_field(self):
        """ Add the password input field to the layout """
        password_layout = QHBoxLayout()
        password_label = QLabel("Password:")
        password_label.setStyleSheet("font-size: 14px; font-weight: 600;")
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
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(message)
            msg_box.setWindowTitle("Success")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Information(self, "Success", message)
            self.accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText(message)
            msg_box.setWindowTitle("Error")
            if dark_mode:
                msg_box.setStyleSheet("background-color: #2e2e2e; color: white;")
                set_dark_mode_title_bar(msg_box)
            msg_box.exec_()
            # QMessageBox.Warning(self, "Error", message)
            self.clear_inputs()

    def clear_inputs(self):
        """ Clear the username and password input fields and set focus to username input """
        self.username_input.clear()
        self.password_input.clear()
        self.username_input.setFocus()

    def apply_widget_styles(self):
        """ Apply the default dark mode styles to the widgets """
        self.username_input.setStyleSheet(common_textbox_style)
        self.password_input.setStyleSheet(common_textbox_style)
        self.confirm_button.setStyleSheet(button_style)
        self.cancel_button.setStyleSheet(button_style)