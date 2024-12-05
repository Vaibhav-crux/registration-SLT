from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QFrame, QGridLayout, QLabel, QDateEdit, QTimeEdit, QComboBox, QTableWidget, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate, QTime, Qt
from app.services.utilities.report.buttons_actions_service import handle_button_action, reset_button_action
from app.style.report_button_style import button_styles

def setup_main_window_ui(window: QWidget):
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
        buttons[button_text] = button
        button.clicked.connect(lambda _, text=button_text: handle_button_action(text, ui_elements))
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

    # Labels and entry boxes
    from_date_label = QLabel("From date:")
    from_date_label.setFont(label_font)

    from_date_value = QDateEdit(frame2)
    from_date_value.setDate(current_date.addDays(-1))  # Set previous day's date as default

    to_date_label = QLabel("To date:")
    to_date_label.setFont(label_font)

    to_date_value = QDateEdit(frame2)
    to_date_value.setDate(current_date)  # Set current date as default

    from_time_label = QLabel("From time:")
    from_time_label.setFont(label_font)

    from_time_value = QTimeEdit(frame2)
    from_time_value.setTime(current_time)  # Set time 6 hours back
    from_time_value.setDisplayFormat("HH:mm")  # Set to 24-hour format

    to_time_label = QLabel("To time:")
    to_time_label.setFont(label_font)

    to_time_value = QTimeEdit(frame2)
    to_time_value.setTime(current_time)  # Set current time as default
    to_time_value.setDisplayFormat("HH:mm")  # Set to 24-hour format

    vehicle_type_label = QLabel("Vehicle Type:")
    vehicle_type_label.setFont(label_font)

    vehicle_type_value = QComboBox(frame2)
    vehicle_type_value.addItems(["ALL","TCT", "PDV", "TVV", "TOV", "PCT", "TDBEV", "SCRAPE"])

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
    table = QTableWidget(frame3)  # Ensure the table is created correctly
    frame3_layout.addWidget(table)
    frame3.setLayout(frame3_layout)
    frame3.setFrameShape(QFrame.StyledPanel)

    # Reset and Search buttons
    buttons_layout = QHBoxLayout()
    reset_button = QPushButton("Reset")
    search_button = QPushButton("Search")

    # Set the width of the buttons
    reset_button.setFixedWidth(150)
    search_button.setFixedWidth(150)

    # Set the stylesheet to the buttons
    reset_button.setStyleSheet(button_styles)
    search_button.setStyleSheet(button_styles)

    # Add the buttons to the layout and align them to the right
    buttons_layout.addWidget(reset_button)
    buttons_layout.addWidget(search_button)
    buttons_layout.setAlignment(Qt.AlignRight)

    # Arrange frames in the main layout
    main_layout.addWidget(frame1)
    right_layout = QVBoxLayout()
    right_layout.addWidget(frame2)
    right_layout.addWidget(separator)
    right_layout.addWidget(frame3)
    right_layout.addLayout(buttons_layout)
    main_layout.addLayout(right_layout)

    window.setLayout(main_layout)

    # Set up UI elements dictionary
    ui_elements = {
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
        "search_value": search_value,
        "table": table  # Make sure the table is included
    }

    reset_button.clicked.connect(lambda: reset_button_action(ui_elements))

    # Pass the UI elements dictionary to handle_button_action
    handle_button_action("Summary", ui_elements)
    buttons["Summary"].setDefault(True)
