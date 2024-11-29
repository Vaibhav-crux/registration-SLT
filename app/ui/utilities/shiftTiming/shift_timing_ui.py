from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QTimeEdit, QPushButton
from PyQt5.QtCore import Qt, QTime
from app.utils.mode_utils import is_dark_mode
from app.style.default_styles import dark_mode_style, light_mode_style, button_style

def setup_ui(window, get_shift_timings, shift_rows):
    """
    Set up the UI layout for the Shift Timing window with the A, B, C shifts.

    :param window: The QDialog window to set up the UI on.
    :param get_shift_timings: Function to fetch the shift timings from the database.
    :param shift_rows: List to store the shift time edits for further processing.
    """
    # Fetch shift timings from the database
    shift_timings = get_shift_timings()

    # Create the main layout
    main_layout = QVBoxLayout()

    # Check if the current mode is dark or light
    dark_mode = is_dark_mode()

    style ="font-size: 14px; font-weight: 600; color: white;"

    # Apply the appropriate stylesheet for textboxes
    common_textbox_style = dark_mode_style if dark_mode else light_mode_style

    # Create a horizontal layout for the "From" and "To" labels at the top
    header_layout = QHBoxLayout()
    empty_label = QLabel("", window)
    empty_label.setFixedWidth(60)
    header_layout.addWidget(empty_label)

    from_label = QLabel("From", window)
    from_label.setStyleSheet(style)
    from_label.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
    header_layout.addWidget(from_label)

    header_layout.addWidget(QLabel("", window))

    to_label = QLabel("To", window)
    to_label.setStyleSheet(style)
    to_label.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
    header_layout.addWidget(to_label)

    main_layout.addLayout(header_layout)

    # Helper function to create a label and time fields in a horizontal layout
    def add_shift_row(shift_name):
        hbox = QHBoxLayout()

        shift_label = QLabel(shift_name.title(), window)
        shift_label.setStyleSheet(style)
        shift_label.setFixedWidth(60)
        hbox.addWidget(shift_label)

        from_time, to_time = shift_timings.get(shift_name, (QTime(0, 0, 0), QTime(0, 0, 0)))

        # from_time_edit = QTimeEdit(QTime.fromString(from_time.strftime('%H:%M:%S'), "HH:mm:ss"), window)
        from_time_edit = QTimeEdit(from_time, window)
        from_time_edit.setFixedWidth(150)
        from_time_edit.setDisplayFormat("HH:mm:ss")
        from_time_edit.setStyleSheet(common_textbox_style)
        hbox.addWidget(from_time_edit)

        dash_label = QLabel("-", window)
        dash_label.setAlignment(Qt.AlignCenter)
        dash_label.setStyleSheet("font-size: 14px; color: white;")
        hbox.addWidget(dash_label)

        # to_time_edit = QTimeEdit(QTime.fromString(to_time.strftime('%H:%M:%S'), "HH:mm:ss"), window)
        to_time_edit = QTimeEdit(to_time, window)
        to_time_edit.setFixedWidth(150)
        to_time_edit.setDisplayFormat("HH:mm:ss")
        to_time_edit.setStyleSheet(common_textbox_style)
        hbox.addWidget(to_time_edit)

        return hbox, from_time_edit, to_time_edit

    # Adding shift rows with values from the database
    for shift_name in ["A shift", "B shift", "C shift"]:
        shift_row, from_time_edit, to_time_edit = add_shift_row(shift_name)
        shift_rows.append((shift_name, from_time_edit, to_time_edit))
        main_layout.addLayout(shift_row)

    note_label = QLabel("Note: Please Enter Time in 24 Hrs Format", window)
    note_label.setAlignment(Qt.AlignCenter)
    note_label.setStyleSheet("font-size: 12px; font-weight: 600; color: red;")
    main_layout.addWidget(note_label)

    button_layout = QHBoxLayout()

    confirm_button = QPushButton("Confirm", window)
    confirm_button.setFixedWidth(100)
    confirm_button.setStyleSheet(button_style)
    button_layout.addWidget(confirm_button)

    cancel_button = QPushButton("Cancel", window)
    cancel_button.setFixedWidth(100)
    cancel_button.setStyleSheet(button_style)
    button_layout.addWidget(cancel_button)

    main_layout.addLayout(button_layout)

    window.setLayout(main_layout)

    # Connect the Confirm button to the click event handler in the window class
    confirm_button.clicked.connect(window.on_confirm_click)
