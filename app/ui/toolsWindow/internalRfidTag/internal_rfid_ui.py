from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QFrame
from PyQt5.QtCore import Qt, QDate
# Import mode utility function
from app.utils.mode_utils import is_dark_mode
# Import styles from default_styles
from app.style.default_styles import dark_mode_style, light_mode_style
# Import the button layout function
from app.ui.toolsWindow.internalRfidTag.internal_rfid_button_ui import create_button_layout
# Import the function to update field write access based on vehicle type
from app.services.tools.internalRegistration.update_fields_write_access import update_fields_write_access
# Import functions to fetch data from the database
from app.controllers.tools.internalRegistration.do_no_controller import fetch_do_numbers, fetch_transport_and_weighbridge
# Import custom date entry box with specific settings
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
    common_textbox_style = dark_mode_style if dark_mode else light_mode_style

    # Create fields
    fields = {
        "rfid_tag": QLineEdit(window),
        "vehicle_type": QComboBox(window),
        "vehicle_no": QLineEdit(window),
        "do_number": QComboBox(window),
        "transporter": QLineEdit(window),
        "weighbridge_no": QLineEdit(window),
        "driver_owner": QLineEdit(window),
        "visit_purpose": QLineEdit(window),
        "place_to_visit": QLineEdit(window),
        "person_to_visit": QLineEdit(window),
        "calendar": MyDateEdit(window),
        "section": QLineEdit(window)
    }
    
    # Set object names
    for name, widget in fields.items():
        widget.setObjectName(name)
        widget.setFixedWidth(300)
        widget.setStyleSheet(common_textbox_style)

    # Add vehicle type options
    fields["vehicle_type"].addItems(["TCT", "PDV", "TVV", "TOV", "PCT", "TDBEV", "SCRAPE"])

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

    # Set UI components properties and add to layout with labels
    components = [
        ("RFID Tag:", fields["rfid_tag"]),
        ("Type of Vehicle:", fields["vehicle_type"]),
        ("Vehicle No:", fields["vehicle_no"]),
        ("DO Number:", fields["do_number"]),
        ("Transporter:", fields["transporter"]),
        ("Weighbridge No:", fields["weighbridge_no"]),
        ("Driver/Owner:", fields["driver_owner"]),
        ("Visit Purpose:", fields["visit_purpose"]),
        ("Place to Visit:", fields["place_to_visit"]),
        ("Person to Visit:", fields["person_to_visit"]),
        ("Validity Till:", fields["calendar"]),
        ("Section:", fields["section"])
    ]

    for label_text, widget in components:
        add_field(main_layout, label_text, widget)

    # Initialize DO numbers in ComboBox
    fields["do_number"].addItems(fetch_do_numbers())

    # Method to update transporter and weighbridge_no based on selected DO Number
    def update_transport_and_weighbridge():
        selected_do_number = fields["do_number"].currentText()
        transporter_value, weighbridge_value = fetch_transport_and_weighbridge(selected_do_number)
        fields["transporter"].setText(transporter_value or "")
        fields["weighbridge_no"].setText(weighbridge_value or "")

    # Update transporter/weighbridge fields when DO Number changes
    fields["do_number"].currentIndexChanged.connect(update_transport_and_weighbridge)

    # Initial call to set fields based on the default vehicle type
    update_fields_write_access(fields["vehicle_type"].currentText(), fields)
    # Connect the vehicle_type ComboBox signal to update fields
    fields["vehicle_type"].currentIndexChanged.connect(lambda: update_fields_write_access(fields["vehicle_type"].currentText(), fields))

    # Status Frame and Layout
    status_frame = QFrame(window)
    status_frame.setFixedHeight(50)
    status_frame.setStyleSheet("""
        QFrame {
            background-color: #3399ff;
            border-radius: 12px;
            border: 2px solid #b3d9ff;
        }
    """)
    status_layout = QVBoxLayout(status_frame)
    status_label = QLabel("Status: Please Enter Vehicle Number or RFID Tag")
    status_label.setObjectName("status_label")
    status_label.setAlignment(Qt.AlignCenter)
    status_label.setStyleSheet("""
        font-size: 14px;
        font-weight: 600;
        color: white;
    """)
    status_layout.addWidget(status_label)

    # Add status frame and button layout to main layout
    main_layout.addWidget(status_frame)
    main_layout.addLayout(create_button_layout(window, fields))

    # Set the main layout on the window
    window.setLayout(main_layout)
