from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QTimeEdit, QPushButton
from PyQt5.QtCore import Qt, QTime
# Import mode utility function
from app.utils.mode_utils import is_dark_mode
# Import styles from default_styles
from app.style.default_styles import dark_mode_style, light_mode_style, button_style

def setup_ui(window):
    """
    Set up the UI layout for the Shift Timing window with the A, B, C shifts as shown in the provided image.
    
    :param window: The QDialog window to set up the UI on.
    """
    # Create the main layout
    main_layout = QVBoxLayout()

    # Check if the current mode is dark or light
    dark_mode = is_dark_mode()

    # Apply the appropriate stylesheet for textboxes
    if dark_mode:
        common_textbox_style = dark_mode_style
    else:
        common_textbox_style = light_mode_style

    # Create a horizontal layout for the "From" and "To" labels at the top
    header_layout = QHBoxLayout()

    # Empty space for alignment under "A Shift" column
    empty_label = QLabel("", window)
    empty_label.setFixedWidth(60)  # Adjust to align with the "Shift" labels
    header_layout.addWidget(empty_label)

    # "From" label
    from_label = QLabel("From", window)
    from_label.setStyleSheet("""
        font-size: 14px;
        font-weight: 600;
        color: white;
    """)
    from_label.setAlignment(Qt.AlignLeft | Qt.AlignBottom)  # Align to top-left
    header_layout.addWidget(from_label)

    # Dash space (empty)
    header_layout.addWidget(QLabel("", window))

    # "To" label
    to_label = QLabel("To", window)
    to_label.setStyleSheet("""
        font-size: 14px;
        font-weight: 600;
        color: white;
    """)
    to_label.setAlignment(Qt.AlignLeft | Qt.AlignBottom)  # Align to top-left
    header_layout.addWidget(to_label)

    # Add the header layout to the main layout
    main_layout.addLayout(header_layout)

    # Helper function to create a label and time fields in a horizontal layout
    def add_shift_row(shift_name, from_time, to_time):
        hbox = QHBoxLayout()

        # Shift label
        shift_label = QLabel(shift_name, window)
        shift_label.setStyleSheet("""
            font-size: 14px;
            font-weight: 600;
            color: white;
        """)
        shift_label.setFixedWidth(60)  # Ensure the shift label is aligned
        hbox.addWidget(shift_label)

        # From time edit
        from_time_edit = QTimeEdit(QTime.fromString(from_time, "HH:mm:ss"), window)
        from_time_edit.setFixedWidth(150)
        from_time_edit.setDisplayFormat("HH:mm:ss")
        from_time_edit.setStyleSheet(common_textbox_style)
        hbox.addWidget(from_time_edit)

        # Dash between the From and To fields
        dash_label = QLabel("-", window)
        dash_label.setAlignment(Qt.AlignCenter)
        dash_label.setStyleSheet("""
            font-size: 14px;
            color: white;
        """)
        hbox.addWidget(dash_label)

        # To time edit
        to_time_edit = QTimeEdit(QTime.fromString(to_time, "HH:mm:ss"), window)
        to_time_edit.setFixedWidth(150)
        to_time_edit.setDisplayFormat("HH:mm:ss")
        to_time_edit.setStyleSheet(common_textbox_style)
        hbox.addWidget(to_time_edit)

        return hbox

    # Adding shift rows with default time values
    main_layout.addLayout(add_shift_row("A Shift", "06:00:00", "13:59:59"))
    main_layout.addLayout(add_shift_row("B Shift", "14:00:00", "21:59:59"))
    main_layout.addLayout(add_shift_row("C Shift", "22:00:00", "05:59:59"))

    # Adding the note at the bottom
    note_label = QLabel("Note: Please Enter Time in 24 Hrs Format", window)
    note_label.setAlignment(Qt.AlignCenter)
    note_label.setStyleSheet("""
        font-size: 12px;
        font-weight: 600;
        color: red;
    """)
    main_layout.addWidget(note_label)

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

    # Add the button layout to the main layout, below the note
    main_layout.addLayout(button_layout)

    # Set the main layout
    window.setLayout(main_layout)
