from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QPushButton
from PyQt5.QtCore import Qt
# Import mode utility function
from app.utils.mode_utils import is_dark_mode
# Import styles from default_styles
from app.style.default_styles import dark_mode_style, light_mode_style, button_style

def setup_ui(window):
    """
    Set up the UI layout for the InternalRegistrationWindow with additional fields and buttons.
    
    :param window: The QDialog window to set up the UI on.
    """
    # Create the main layout
    main_layout = QVBoxLayout()

    # Check if the current mode is dark or light
    dark_mode = is_dark_mode()

    # Apply the appropriate stylesheet
    if dark_mode:
        common_textbox_style = dark_mode_style
    else:
        common_textbox_style = light_mode_style

    # Helper function to create a label and field (textbox, combobox, or dateedit) in a horizontal layout
    def add_field(layout, label_text, widget):
        hbox = QHBoxLayout()
        label = QLabel(label_text, window)
        label.setStyleSheet("""
            font-size: 14px;
            font-weight: 600;  /* Semi-bold */
        """)
        label.setAlignment(Qt.AlignLeft)
        hbox.addWidget(label)
        hbox.addWidget(widget)
        layout.addLayout(hbox)

    # RFID Tag
    rfid_tag = QLineEdit(window)
    rfid_tag.setFixedWidth(300)
    rfid_tag.setStyleSheet(common_textbox_style)
    add_field(main_layout, "RFID Tag:", rfid_tag)

    # Vehicle Number Tag
    vehicle_no = QLineEdit(window)
    vehicle_no.setFixedWidth(300)
    vehicle_no.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Vehicle No:", vehicle_no)

    # Action Tag
    action = QComboBox(window)
    action.addItems(["Blacklist", "Unblacklist"])  # Add dummy DO numbers
    action.setFixedWidth(300)
    action.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Action:", action)

    # Create buttons
    button_layout = QHBoxLayout()

    # New Button
    confirm_button = QPushButton("Confirm", window)
    confirm_button.setFixedWidth(100)
    confirm_button.setStyleSheet(button_style)
    button_layout.addWidget(confirm_button)

    # Clear Button
    cancel_button = QPushButton("Cancel", window)
    cancel_button.setFixedWidth(100)
    cancel_button.setStyleSheet(button_style)
    button_layout.addWidget(cancel_button)

    # Add button layout to main layout
    main_layout.addLayout(button_layout)

    # Set the main layout
    window.setLayout(main_layout)
