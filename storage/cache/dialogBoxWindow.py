# app\services\tools\internalRegistration\internal_registration_window.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit

# Import the mode utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window

class InternalRegistrationWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration")
        self.setGeometry(100, 100, 500, 500)

        # Apply window flags to remove the "?" and only show the close button
        apply_window_flags(self)

        # Apply the dark or light mode styles
        apply_mode_styles(self)

        # Center the window using frame_utils
        center_window(self)

        # Apply drop shadow using frame_utils
        apply_drop_shadow(self)

        # Create the main layout
        main_layout = QVBoxLayout()

        # Create a horizontal layout for the Name label and text box
        hbox = QHBoxLayout()

        # Create the Name label
        name_label = QLabel("Name:", self)
        name_label.setAlignment(Qt.AlignLeft)
        name_label.setStyleSheet("font-size: 14px;")
        hbox.addWidget(name_label)

        # Create the Name text box with only the bottom border (professional blue)
        name_input = QLineEdit(self)
        name_input.setFixedWidth(300)  # Set width of the input field
        name_input.setStyleSheet("""
            QLineEdit {
                border-top: none;
                border-left: none;
                border-right: none;
                border-bottom: 2px solid #007bff;  /* Professional blue bottom border */
                padding: 2px;
            }
            """)
        hbox.addWidget(name_input)

        # Add the horizontal layout (hbox) to the main layout
        main_layout.addLayout(hbox)
        
        self.setLayout(main_layout)
