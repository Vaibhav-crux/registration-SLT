# app\ui\toolsWindow\internalRfidTag\internal_rfid_ui.py

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QPushButton
from PyQt5.QtCore import Qt
# Import mode utility function
from app.utils.mode_utils import is_dark_mode
# Import styles from default_styles
from app.style.default_styles import dark_mode_style, light_mode_style, button_style
from app.utils.cursor.entry_box import MyLineEdit

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
    rfid_tag = MyLineEdit(window)
    rfid_tag.setFixedWidth(300)
    rfid_tag.setStyleSheet(common_textbox_style)
    add_field(main_layout, "RFID Tag:", rfid_tag)

    # Type of Vehicle (ComboBox)
    vehicle_type = QComboBox(window)
    vehicle_type.addItems(["Car", "Truck", "Bus", "Van"])  # Add vehicle types
    vehicle_type.setFixedWidth(300)
    vehicle_type.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Type of Vehicle:", vehicle_type)

    # Vehicle No (TextBox)
    vehicle_no = MyLineEdit(window)
    vehicle_no.setFixedWidth(300)
    vehicle_no.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Vehicle No:", vehicle_no)

    # DO Number (ComboBox)
    do_number = QComboBox(window)
    do_number.addItems(["DO123", "DO456", "DO789"])  # Add dummy DO numbers
    do_number.setFixedWidth(300)
    do_number.setStyleSheet(common_textbox_style)
    add_field(main_layout, "DO Number:", do_number)

    # Transporter (TextBox)
    transporter = MyLineEdit(window)
    transporter.setFixedWidth(300)
    transporter.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Transporter:", transporter)

    # Weighbridge No (TextBox)
    weighbridge_no = MyLineEdit(window)
    weighbridge_no.setFixedWidth(300)
    weighbridge_no.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Weighbridge No:", weighbridge_no)

    # Driver/Owner (TextBox)
    driver_owner = MyLineEdit(window)
    driver_owner.setFixedWidth(300)
    driver_owner.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Driver/Owner:", driver_owner)

    # Visit Purpose (TextBox)
    visit_purpose = MyLineEdit(window)
    visit_purpose.setFixedWidth(300)
    visit_purpose.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Visit Purpose:", visit_purpose)

    # Place to Visit (TextBox)
    place_to_visit = MyLineEdit(window)
    place_to_visit.setFixedWidth(300)
    place_to_visit.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Place to Visit:", place_to_visit)

    # Person to Visit (TextBox)
    person_to_visit = MyLineEdit(window)
    person_to_visit.setFixedWidth(300)
    person_to_visit.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Person to Visit:", person_to_visit)

    # Validity Till (QDateEdit)
    calendar = QDateEdit(window)
    calendar.setFixedWidth(300)
    calendar.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Validity Till:", calendar)

    # Create buttons
    button_layout = QHBoxLayout()

    # New Button
    new_button = QPushButton("New", window)
    new_button.setFixedWidth(100)
    new_button.setStyleSheet(button_style)
    button_layout.addWidget(new_button)

    # Edit Button
    edit_button = QPushButton("Edit", window)
    edit_button.setFixedWidth(100)
    edit_button.setStyleSheet(button_style)
    button_layout.addWidget(edit_button)

    # Delete Button
    delete_button = QPushButton("Delete", window)
    delete_button.setFixedWidth(100)
    delete_button.setStyleSheet(button_style)
    button_layout.addWidget(delete_button)

    # Clear Button
    clear_button = QPushButton("Clear", window)
    clear_button.setFixedWidth(100)
    clear_button.setStyleSheet(button_style)
    button_layout.addWidget(clear_button)

    # Add button layout to main layout
    main_layout.addLayout(button_layout)

    # Set the main layout
    window.setLayout(main_layout)
