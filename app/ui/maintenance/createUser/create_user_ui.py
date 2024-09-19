# app\ui\toolsWindow\internalRfidTag\internal_rfid_ui.py

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
    user_name = QLineEdit(window)
    user_name.setFixedWidth(300)
    user_name.setStyleSheet(common_textbox_style)
    add_field(main_layout, "User Name:", user_name)

    # Password Tag
    password = QLineEdit(window)
    password.setFixedWidth(300)
    password.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Password:", password)

    # Type of Vehicle (ComboBox)
    auth_type = QComboBox(window)
    auth_type.addItems(["User", "Admin"])  # Add vehicle types
    auth_type.setFixedWidth(300)
    auth_type.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Auth Type:", auth_type)

    # Vehicle No (TextBox)
    employe_id = QLineEdit(window)
    employe_id.setFixedWidth(300)
    employe_id.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Employe Id:", employe_id)

    # Transporter (TextBox)
    full_name = QLineEdit(window)
    full_name.setFixedWidth(300)
    full_name.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Full Name:", full_name)

    # Weighbridge No (TextBox)
    email = QLineEdit(window)
    email.setFixedWidth(300)
    email.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Email:", email)

    # Driver/Owner (TextBox)
    designation = QLineEdit(window)
    designation.setFixedWidth(300)
    designation.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Designation:", designation)

    # Visit Purpose (TextBox)
    address = QLineEdit(window)
    address.setFixedWidth(300)
    address.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Address:", address)

    # Place to Visit (TextBox)
    mobile_number = QLineEdit(window)
    mobile_number.setFixedWidth(300)
    mobile_number.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Mobile Number:", mobile_number)

    # Person to Visit (TextBox)
    organisation = QLineEdit(window)
    organisation.setFixedWidth(300)
    organisation.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Organisation:", organisation)

    # Create buttons
    button_layout = QHBoxLayout()

    # New Button
    new_button = QPushButton("Submit", window)
    new_button.setFixedWidth(100)
    new_button.setStyleSheet(button_style)
    button_layout.addWidget(new_button)

    # Clear Button
    clear_button = QPushButton("Clear", window)
    clear_button.setFixedWidth(100)
    clear_button.setStyleSheet(button_style)
    button_layout.addWidget(clear_button)

    # Add button layout to main layout
    main_layout.addLayout(button_layout)

    # Set the main layout
    window.setLayout(main_layout)
