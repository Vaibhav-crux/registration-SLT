from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy
from app.utils.mode_utils import apply_mode_styles, apply_window_flags, is_dark_mode
from app.style.default_styles import dark_mode_style, light_mode_style, button_style

class AuthUserUI(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.initUI()
        self.applyStyles()
        
    def initUI(self):
        # Create a form layout for user input fields
        form_layout = QFormLayout()
        
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        
        form_layout.addRow('Username:', self.username_input)
        form_layout.addRow('Password:', self.password_input)
        
        # Create a horizontal layout for buttons
        button_layout = QHBoxLayout()
        
        self.confirm_button = QPushButton('Confirm')
        self.cancel_button = QPushButton('Cancel')

        # Set a fixed width for the buttons
        button_width = 100  # You can adjust this value as needed
        self.confirm_button.setFixedWidth(button_width)
        self.cancel_button.setFixedWidth(button_width)
        
        button_layout.addWidget(self.confirm_button)
        button_layout.addSpacing(10)  # Add spacing between buttons
        button_layout.addWidget(self.cancel_button)

        # Add a horizontal spacer to push the buttons to the left
        horizontal_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        button_layout.addSpacerItem(horizontal_spacer)
        
        # Combine form layout and button layout in a vertical layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)
        
        # Apply window flags
        apply_window_flags(self)

    def applyStyles(self):
        # Apply mode-specific styles to the entire window
        apply_mode_styles(self)
        
        # Determine the current mode and apply the widget styles
        if is_dark_mode():
            self.username_input.setStyleSheet(dark_mode_style)
            self.password_input.setStyleSheet(dark_mode_style)
            self.confirm_button.setStyleSheet(button_style)
            self.cancel_button.setStyleSheet(button_style)
        else:
            self.username_input.setStyleSheet(light_mode_style)
            self.password_input.setStyleSheet(light_mode_style)
            self.confirm_button.setStyleSheet(button_style)
            self.cancel_button.setStyleSheet(button_style)
