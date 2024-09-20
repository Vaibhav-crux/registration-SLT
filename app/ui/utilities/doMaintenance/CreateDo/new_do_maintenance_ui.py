from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
# Import mode utility function
from app.utils.mode_utils import is_dark_mode
# Import styles from default_styles
from app.style.default_styles import dark_mode_style, light_mode_style, button_style

def setup_new_do_ui(window):
    """
    Set up the UI layout for the New DO Maintenance window to ask for User Name and Password.
    
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

    # Helper function to create a label and input field in a horizontal layout
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

    # User Name input
    user_name_input = QLineEdit(window)
    user_name_input.setFixedWidth(300)
    user_name_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "User Name:", user_name_input)

    # Password input (as password field)
    password_input = QLineEdit(window)
    password_input.setFixedWidth(300)
    password_input.setEchoMode(QLineEdit.Password)
    password_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Password:", password_input)

    # Create buttons
    button_layout = QHBoxLayout()

    # Confirm Button
    confirm_button = QPushButton("Confirm", window)
    confirm_button.setFixedWidth(100)
    confirm_button.setStyleSheet(button_style)
    button_layout.addWidget(confirm_button)

    # Cancel Button
    cancel_button = QPushButton("Cancel", window)
    cancel_button.setFixedWidth(100)
    cancel_button.setStyleSheet(button_style)
    button_layout.addWidget(cancel_button)

    # Add button layout to main layout
    main_layout.addLayout(button_layout)

    # Set the main layout
    window.setLayout(main_layout)

    return user_name_input, password_input, confirm_button, cancel_button
