from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QFrame, QVBoxLayout
from PyQt5.QtCore import Qt, QDate
# Import mode utility function
from app.utils.mode_utils import is_dark_mode
# Import styles from default_styles
from app.style.default_styles import dark_mode_style, light_mode_style
# Import the button layout function
from app.ui.toolsWindow.internalRfidTag.internal_rfid_button_ui import create_button_layout
from app.services.tools.internalRegistration.update_fields_write_access import update_fields_write_access
from app.utils.cursor.entry_box import MyDateEdit

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

    # Type of Vehicle (ComboBox)
    vehicle_type = QComboBox(window)
    vehicle_type.addItems(["TCT", "PDV", "TVV", "TOV", "PCT", "TDBEV", "SCRAPE"])  # Add vehicle types
    vehicle_type.setFixedWidth(300)
    vehicle_type.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Type of Vehicle:", vehicle_type)

    # Vehicle No (TextBox)
    vehicle_no = QLineEdit(window)
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
    transporter = QLineEdit(window)
    transporter.setFixedWidth(300)
    transporter.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Transporter:", transporter)

    # Weighbridge No (TextBox)
    weighbridge_no = QLineEdit(window)
    weighbridge_no.setFixedWidth(300)
    weighbridge_no.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Weighbridge No:", weighbridge_no)

    # Driver/Owner (TextBox)
    driver_owner = QLineEdit(window)
    driver_owner.setFixedWidth(300)
    driver_owner.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Driver/Owner:", driver_owner)

    # Visit Purpose (TextBox)
    visit_purpose = QLineEdit(window)
    visit_purpose.setFixedWidth(300)
    visit_purpose.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Visit Purpose:", visit_purpose)

    # Place to Visit (TextBox)
    place_to_visit = QLineEdit(window)
    place_to_visit.setFixedWidth(300)
    place_to_visit.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Place to Visit:", place_to_visit)

    # Person to Visit (TextBox)
    person_to_visit = QLineEdit(window)
    person_to_visit.setFixedWidth(300)
    person_to_visit.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Person to Visit:", person_to_visit)

    # Validity Till (QDateEdit)
    calendar = MyDateEdit(window)
    calendar.setFixedWidth(300)
    calendar.setStyleSheet(common_textbox_style)
    calendar.setMinimumDate(QDate.currentDate())  # Prevent selecting a past date
    add_field(main_layout, "Validity Till:", calendar)

    # Section (TextBox)
    section = QLineEdit(window)
    section.setFixedWidth(300)
    section.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Section:", section)

    # Create the status frame
    status_frame = QFrame(window)
    status_frame.setFixedHeight(50)  # Set fixed height for the frame
    status_frame.setStyleSheet("""
        QFrame {
            background-color: #3399ff;  /* Light blue background similar to the image */
            border-radius: 12px;  /* Rounded corners */
            border: 2px solid #b3d9ff;  /* Slightly lighter blue border */
        }
    """)

    fields = {
        "rfid_tag": rfid_tag,
        "vehicle_type": vehicle_type,
        "vehicle_no": vehicle_no,
        "do_number": do_number,
        "transporter": transporter,
        "weighbridge_no": weighbridge_no,
        "driver_owner": driver_owner,
        "visit_purpose": visit_purpose,
        "place_to_visit": place_to_visit,
        "person_to_visit": person_to_visit,
        "calendar": calendar,
        "section": section
    }

    # Initial call to set fields based on the default vehicle type
    update_fields_write_access(vehicle_type.currentText(), fields)

    # Connect the vehicle_type ComboBox signal to update fields
    vehicle_type.currentIndexChanged.connect(lambda: update_fields_write_access(vehicle_type.currentText(), fields))

    # Add a layout to the frame to ensure proper text alignment
    status_layout = QVBoxLayout(status_frame)

    # Create the label inside the frame and center the text
    status_label = QLabel("Status: Please Enter Vehicle Number or RFID Tag")
    status_label.setAlignment(Qt.AlignCenter)  # Center the text in the frame
    status_label.setStyleSheet("""
        font-size: 14px;
        font-weight: 600;  /* Semi-bold */
        color: white;  /* White text color */
    """)

    # Add the label to the frame's layout
    status_layout.addWidget(status_label)

    # Add status frame to the main layout
    main_layout.addWidget(status_frame)

    # Add the button layout from the imported function
    button_layout = create_button_layout(window, fields)  # Pass fields as well
    main_layout.addLayout(button_layout)

    # Set the main layout
    window.setLayout(main_layout)
