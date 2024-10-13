from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
# Import mode utility function
from app.utils.mode_utils import is_dark_mode
# Import styles from default_styles
from app.style.default_styles import dark_mode_style, light_mode_style, button_style
# Import custom widget classes
from app.utils.cursor.entry_box import MyLineEdit, MyComboBox

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
    common_textbox_style = dark_mode_style if dark_mode else light_mode_style

    # Helper function to create a label and field in a horizontal layout
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
    rfid_tag = MyLineEdit(window)  # Use MyLineEdit instead of QLineEdit
    rfid_tag.setFixedWidth(300)
    rfid_tag.setStyleSheet(common_textbox_style)
    rfid_tag.setObjectName("RFID Tag")  # Set object name
    add_field(main_layout, "RFID Tag:", rfid_tag)

    # Vehicle Number Tag
    vehicle_no = MyLineEdit(window)  # Use MyLineEdit instead of QLineEdit
    vehicle_no.setFixedWidth(300)
    vehicle_no.setStyleSheet(common_textbox_style)
    vehicle_no.setObjectName("Vehicle No")  # Set object name
    add_field(main_layout, "Vehicle No:", vehicle_no)

    # Action Tag
    action = MyComboBox(window)  # Use MyComboBox instead of QComboBox
    action.addItems(["Blacklist", "Unblacklist"])
    action.setFixedWidth(300)
    action.setStyleSheet(common_textbox_style)
    action.setObjectName("Action")  # Set object name
    add_field(main_layout, "Action:", action)

    # Create buttons
    button_layout = QHBoxLayout()

    # Confirm Button
    confirm_button = QPushButton("Confirm", window)
    confirm_button.setFixedWidth(100)
    confirm_button.setStyleSheet(button_style)
    confirm_button.setObjectName("Confirm")  # Set object name
    button_layout.addWidget(confirm_button)

    # Cancel Button
    cancel_button = QPushButton("Cancel", window)
    cancel_button.setFixedWidth(100)
    cancel_button.setStyleSheet(button_style)
    cancel_button.setObjectName("Cancel")  # Set object name
    button_layout.addWidget(cancel_button)

    # Add button layout to main layout
    main_layout.addLayout(button_layout)

    # Set the main layout
    window.setLayout(main_layout)
