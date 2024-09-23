from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
# Import mode utility function
from app.utils.mode_utils import is_dark_mode
# Import styles from default_styles
from app.style.default_styles import dark_mode_style, light_mode_style, button_style

def setup_create_do_ui(window):
    """
    Set up the UI layout for the Create DO Maintenance window.
    
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

    # DO Number input
    do_number_input = QLineEdit(window)
    do_number_input.setFixedWidth(300)
    do_number_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "DO Number:", do_number_input)

    # Transporter input
    transporter_input = QLineEdit(window)
    transporter_input.setFixedWidth(300)
    transporter_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Transporter:", transporter_input)

    # Create buttons
    button_layout = QHBoxLayout()

    # Save Button
    save_button = QPushButton("Save", window)
    save_button.setFixedWidth(100)
    save_button.setStyleSheet(button_style)
    button_layout.addWidget(save_button)

    # Clear Button
    clear_button = QPushButton("Clear", window)
    clear_button.setFixedWidth(100)
    clear_button.setStyleSheet(button_style)
    button_layout.addWidget(clear_button)

    # Add button layout to main layout
    main_layout.addLayout(button_layout)

    # Set the main layout
    window.setLayout(main_layout)

    return do_number_input, transporter_input, save_button, clear_button
