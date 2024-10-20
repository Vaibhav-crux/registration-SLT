from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QCheckBox
from app.utils.mode_utils import apply_mode_styles, is_dark_mode
from app.style.default_styles import dark_mode_style, light_mode_style, button_style
from app.style.disabled_styles import disabled_style
from app.services.tools.internalRegistration.newServices.checkbox_status_service import update_due_checkbox_status
from app.services.tools.internalRegistration.newServices.autofill_total_amount_service import calculate_total_amount  # Import the service

def setup_new_window_ui(window, data):
    """
    Set up the UI for the new window displaying RFID details in a potentially editable format.

    :param window: The new window to set up the UI on.
    :param data: A dictionary containing the data to display.
    """
    # Apply the mode styles to the window
    apply_mode_styles(window)

    # Determine the current mode dynamically
    dark_mode = is_dark_mode()
    base_style = dark_mode_style if dark_mode else light_mode_style

    layout = QVBoxLayout()

    # Define a mapping from internal keys to user-friendly labels
    key_to_label = {
        "rfid_tag": "RFID Tag:",
        "vehicle_type": "Type of Vehicle:",
        "vehicle_no": "Vehicle No:",
        "do_number": "DO Number:",
        "transporter": "Transporter:",
        "weighbridge_no": "Weighbridge No:",
        "driver_owner": "Driver/Owner:",
        "visit_purpose": "Visit Purpose:",
        "place_to_visit": "Place to Visit:",
        "person_to_visit": "Person to Visit:",
        "calendar": "Validity Till:"
    }

    def add_label_and_value(layout, label_text, value, fixed_width=300):
        """Helper to add a non-editable field with styling and fixed width."""
        hbox = QHBoxLayout()
        label = QLabel(label_text, window)
        label.setAlignment(Qt.AlignLeft)
        label.setStyleSheet("font-size: 14px; font-weight: bold;")  # Increase label font size and make bold
        hbox.addWidget(label)

        value_widget = QLineEdit(window)
        value_widget.setText(value)
        value_widget.setReadOnly(True)  # Make the field non-editable
        value_widget.setFixedWidth(fixed_width)  # Set a fixed width
        value_widget.setStyleSheet(base_style + disabled_style)
        hbox.addWidget(value_widget)

        layout.addLayout(hbox)

    # Populate the fields using the data dictionary and the key-to-label mapping
    for key, value in data.items():
        if key in key_to_label:
            add_label_and_value(layout, key_to_label[key], value)

    # Get the vehicle type from the data
    vehicle_type = data.get("vehicle_type", "")

    # Calculate the total amount using the service
    total_amount = calculate_total_amount(vehicle_type)

    # Add 'Total Amount' label and a read-only textbox
    add_label_and_value(layout, "Total Amount:", str(total_amount))

    # Add a non-editable ComboBox for Payment Mode with a 'Due' checkbox
    def add_payment_mode_with_due(layout, label_text, items, fixed_width=230):
        """Helper to add a non-editable combo box for payment mode and a 'Due' checkbox."""
        hbox = QHBoxLayout()
        label = QLabel(label_text, window)
        label.setAlignment(Qt.AlignLeft)
        label.setStyleSheet("font-size: 14px; font-weight: bold;")  # Increase label font size and make bold
        hbox.addWidget(label)

        combo_box = QComboBox(window)
        combo_box.addItems(items)
        combo_box.setEditable(False)  # Ensure the combo box is not writable
        combo_box.setFixedWidth(fixed_width)  # Adjust fixed width to accommodate the checkbox
        combo_box.setStyleSheet(base_style)
        hbox.addWidget(combo_box)

        due_checkbox = QCheckBox("Due", window)
        
        # Add style for normal and disabled states
        due_checkbox.setStyleSheet(base_style + """
            QCheckBox:disabled {
                color: grey;  /* Set the text color to grey when disabled */
            }
        """)
        hbox.addWidget(due_checkbox)

        # Function to enable/disable the checkbox based on selected payment mode
        def update_due_checkbox(index):
            selected_payment_mode = combo_box.itemText(index)
            checkbox_enabled = update_due_checkbox_status(selected_payment_mode)  # Use the service to determine status
            due_checkbox.setEnabled(checkbox_enabled)
            if not checkbox_enabled:
                due_checkbox.setChecked(False)  # Uncheck the checkbox if disabled

        # Connect the signal to the slot
        combo_box.currentIndexChanged.connect(update_due_checkbox)

        # Initialize the checkbox state based on the default selection
        update_due_checkbox(combo_box.currentIndex())

        layout.addLayout(hbox)

    # Example usage for payment mode
    add_payment_mode_with_due(layout, "Payment Mode:  ", ["Cash", "UPI"])

    # Add 'Confirm' and 'Cancel' buttons
    button_layout = QHBoxLayout()

    confirm_button = QPushButton("Confirm", window)
    confirm_button.setFixedWidth(100)
    confirm_button.setStyleSheet(button_style)  # Apply predefined button style
    button_layout.addWidget(confirm_button)

    cancel_button = QPushButton("Cancel", window)
    cancel_button.setFixedWidth(100)
    cancel_button.setStyleSheet(button_style)  # Apply predefined button style
    button_layout.addWidget(cancel_button)

    layout.addLayout(button_layout)

    window.setLayout(layout)
