from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QFrame, QGridLayout, QLabel, QDateEdit, QTimeEdit, QComboBox, QTableWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate, QTime
from app.services.utilities.report.buttons_actions_service import handle_button_action

def setup_main_window_ui(window):
    """
    Set up the UI layout for the main window of the report utility.
    :param window: The QWidget window to set up the UI on.
    """

    # Main layout
    main_layout = QHBoxLayout()

    # Frame 1
    frame1 = QFrame(window)
    frame1_layout = QVBoxLayout()
    frame1_buttons = ["Summary", "Weighbridge Wise", "Shift Wise", "Do Wise", "Vehicle Type", "Validity Wise", "Registration Details"]

    # Create a dictionary to store the buttons
    buttons = {}

    for button_text in frame1_buttons:
        button = QPushButton(button_text, frame1)
        buttons[button_text] = button  # Store button in dictionary
        button.clicked.connect(lambda _, text=button_text: handle_button_action(text, {
            "from_date_label": from_date_label,
            "from_date_value": from_date_value,
            "to_date_label": to_date_label,
            "to_date_value": to_date_value,
            "from_time_label": from_time_label,
            "from_time_value": from_time_value,
            "to_time_label": to_time_label,
            "to_time_value": to_time_value,
            "vehicle_type_label": vehicle_type_label,
            "vehicle_type_value": vehicle_type_value,
            "search_label": search_label,
            "search_value": search_value
        }))
        frame1_layout.addWidget(button)

    frame1.setLayout(frame1_layout)
    frame1.setFrameShape(QFrame.StyledPanel)

    # Frame 2
    frame2 = QFrame(window)
    frame2_layout = QGridLayout()

    # Create a font object for labels
    label_font = QFont()
    label_font.setPointSize(12)

    # Get current date and time
    current_date = QDate.currentDate()
    current_time = QTime.currentTime()
    time_six_hours_back = current_time.addSecs(-12 * 3600)  # Subtract 6 hours

        # Labels and entry boxes
    from_date_label = QLabel("From date:")
    from_date_label.setFont(label_font)

    from_date_value = QDateEdit(frame2)
    from_date_value.setDate(current_date)  # Set current date as default

    to_date_label = QLabel("To date:")
    to_date_label.setFont(label_font)

    to_date_value = QDateEdit(frame2)
    to_date_value.setDate(current_date)  # Set current date as default

    from_time_label = QLabel("From time:")
    from_time_label.setFont(label_font)

    from_time_value = QTimeEdit(frame2)
    from_time_value.setTime(time_six_hours_back)  # Set time 6 hours back
    from_time_value.setDisplayFormat("HH:mm")  # Set to 24-hour format

    to_time_label = QLabel("To time:")
    to_time_label.setFont(label_font)

    to_time_value = QTimeEdit(frame2)
    to_time_value.setTime(current_time)  # Set current time as default
    to_time_value.setDisplayFormat("HH:mm")  # Set to 24-hour format


    vehicle_type_label = QLabel("Vehicle Type:")
    vehicle_type_label.setFont(label_font)

    vehicle_type_value = QComboBox(frame2)
    vehicle_type_value.addItems(["TCT", "PDV", "TVV", "TOV", "PCT", "TDBEV", "SCRAPE"])

    search_label = QLabel("Vehicle No:")
    search_label.setFont(label_font)

    search_value = QLineEdit(frame2)

    # Set a fixed width for all entry boxes
    entry_box_width = 150
    from_date_value.setFixedWidth(entry_box_width)
    to_date_value.setFixedWidth(entry_box_width)
    from_time_value.setFixedWidth(entry_box_width)
    to_time_value.setFixedWidth(entry_box_width)
    vehicle_type_value.setFixedWidth(entry_box_width)
    search_value.setFixedWidth(entry_box_width)

    # Arrange the widgets in a grid layout
    frame2_layout.addWidget(from_date_label, 0, 0)
    frame2_layout.addWidget(from_date_value, 0, 1)
    frame2_layout.addWidget(from_time_label, 0, 2)
    frame2_layout.addWidget(from_time_value, 0, 3)
    frame2_layout.addWidget(vehicle_type_label, 0, 4)
    frame2_layout.addWidget(vehicle_type_value, 0, 5)

    frame2_layout.addWidget(to_date_label, 1, 0)
    frame2_layout.addWidget(to_date_value, 1, 1)
    frame2_layout.addWidget(to_time_label, 1, 2)
    frame2_layout.addWidget(to_time_value, 1, 3)
    frame2_layout.addWidget(search_label, 1, 4)
    frame2_layout.addWidget(search_value, 1, 5)

    frame2.setLayout(frame2_layout)
    frame2.setFrameShape(QFrame.NoFrame)  # Remove the frame border
    frame2.setMaximumHeight(150)  # Decrease the height of Frame 2

    # Separator between frame2 and frame3
    separator = QFrame(window)
    separator.setFrameShape(QFrame.HLine)  # Set as horizontal line
    separator.setFrameShadow(QFrame.Sunken)  # Optional: make it look sunken
    separator.setLineWidth(2)  # Optional: set thickness of the line

    # Frame 3
    frame3 = QFrame(window)
    frame3_layout = QVBoxLayout()
    table = QTableWidget(10, 5, frame3)  # Example table with 10 rows and 5 columns
    table.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3", "Column 4", "Column 5"])

    # Hide both vertical and horizontal headers
    table.verticalHeader().setVisible(False)
    table.horizontalHeader().setVisible(False)

    frame3_layout.addWidget(table)
    frame3.setLayout(frame3_layout)
    frame3.setFrameShape(QFrame.StyledPanel)

    # Arrange frames in the main layout
    main_layout.addWidget(frame1)
    right_layout = QVBoxLayout()
    right_layout.addWidget(frame2)
    right_layout.addWidget(separator)  # Add the separator
    right_layout.addWidget(frame3)
    main_layout.addLayout(right_layout)

    window.setLayout(main_layout)

    # Set the default button state to "Summary" when the window opens
    handle_button_action("Summary", {
        "from_date_label": from_date_label,
        "from_date_value": from_date_value,
        "to_date_label": to_date_label,
        "to_date_value": to_date_value,
        "from_time_label": from_time_label,
        "from_time_value": from_time_value,
        "to_time_label": to_time_label,
        "to_time_value": to_time_value,
        "vehicle_type_label": vehicle_type_label,
        "vehicle_type_value": vehicle_type_value,
        "search_label": search_label,
        "search_value": search_value
    })
    buttons["Summary"].setDefault(True)  # Set the "Summary" button as the default
