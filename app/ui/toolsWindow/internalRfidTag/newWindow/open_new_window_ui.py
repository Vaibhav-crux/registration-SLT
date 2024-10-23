from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QComboBox, QMessageBox
from app.utils.mode_utils import apply_mode_styles, is_dark_mode
from app.style.default_styles import dark_mode_style, light_mode_style, button_style
from app.style.disabled_styles import disabled_style
from app.services.tools.internalRegistration.newServices.checkbox_status_service import update_due_checkbox_status
from app.services.tools.internalRegistration.newServices.autofill_total_amount_service import calculate_total_amount
from app.services.tools.internalRegistration.newServices.paymentServices.upi_payment_service import show_upi_payment_dialog
from app.utils.template.html_generator import generate_html
from app.services.tools.internalRegistration.newServices.paymentServices.payment_receipt_service import show_payment_receipt_window

# Define constants
TOTAL_AMOUNT_LABEL = "Total Amount"
PAYMENT_STATUS_LABEL = "Payment Status"
PAID_STATUS = "Paid"
NOT_PAID_STATUS = "Not Paid"
RFID_DETAILS_FILE = "rfid_details.html"

def setup_new_window_ui(window, data):
    apply_mode_styles(window)
    layout = QVBoxLayout()

    dark_mode = is_dark_mode()
    base_style = dark_mode_style if dark_mode else light_mode_style

    # Add details to layout
    add_data_fields(window, layout, data, base_style)
    vehicle_type = data.get("vehicle_type", "")
    total_amount = add_total_amount(layout, vehicle_type, base_style)

    # Payment mode
    combo_box, due_checkbox = add_payment_mode_with_due(layout, window, base_style)

    # Add buttons
    add_buttons(window, layout, combo_box, due_checkbox, total_amount, data)

    window.setLayout(layout)

def add_data_fields(window, layout, data, base_style):
    key_to_label = {
        "rfid_tag": "RFID Tag",
        "vehicle_type": "Type of Vehicle",
        "vehicle_no": "Vehicle No",
        "do_number": "DO Number",
        "transporter": "Transporter",
        "weighbridge_no": "Weighbridge No",
        "driver_owner": "Driver/Owner",
        "visit_purpose": "Visit Purpose",
        "place_to_visit": "Place to Visit",
        "person_to_visit": "Person to Visit",
        "calendar": "Validity Till",
    }
    
    for key, value in data.items():
        if key in key_to_label:
            add_label_and_value(window, layout, key_to_label[key], value, base_style)

def add_label_and_value(window, layout, label_text, value, base_style, fixed_width=300):
    hbox = QHBoxLayout()
    label = QLabel(f"{label_text}:", window)
    label.setAlignment(Qt.AlignLeft)
    label.setStyleSheet("font-size: 14px; font-weight: bold;")
    hbox.addWidget(label)

    value_widget = QLineEdit(window)
    value_widget.setText(value)
    value_widget.setReadOnly(True)
    value_widget.setFixedWidth(fixed_width)
    value_widget.setStyleSheet(base_style + disabled_style)
    hbox.addWidget(value_widget)

    layout.addLayout(hbox)

def add_total_amount(layout, vehicle_type, base_style):
    total_amount = calculate_total_amount(vehicle_type)
    add_label_and_value(None, layout, TOTAL_AMOUNT_LABEL, str(total_amount), base_style)  # Pass base_style here
    return total_amount


def add_payment_mode_with_due(layout, window, base_style, fixed_width=230):
    hbox = QHBoxLayout()
    label = QLabel("Payment Mode:", window)
    label.setAlignment(Qt.AlignLeft)
    label.setStyleSheet("font-size: 14px; font-weight: bold;")
    hbox.addWidget(label)

    combo_box = QComboBox(window)
    combo_box.addItems(["Cash", "UPI"])
    combo_box.setEditable(False)
    combo_box.setFixedWidth(fixed_width)
    combo_box.setStyleSheet(base_style)
    hbox.addWidget(combo_box)

    due_checkbox = QCheckBox("Due", window)
    due_checkbox.setStyleSheet(base_style + """
      QCheckBox:disabled {
        color: grey;
      }
    """)
    hbox.addWidget(due_checkbox)

    combo_box.currentIndexChanged.connect(lambda: update_due_checkbox(combo_box, due_checkbox))
    update_due_checkbox(combo_box, due_checkbox)

    layout.addLayout(hbox)
    return combo_box, due_checkbox

def update_due_checkbox(combo_box, due_checkbox):
    selected_payment_mode = combo_box.currentText()
    checkbox_enabled = update_due_checkbox_status(selected_payment_mode)
    due_checkbox.setEnabled(checkbox_enabled)
    if not checkbox_enabled:
        due_checkbox.setChecked(False)

def add_buttons(window, layout, combo_box, due_checkbox, total_amount, data):
    button_layout = QHBoxLayout()

    confirm_button = QPushButton("Confirm", window)
    confirm_button.setFixedWidth(100)
    confirm_button.setStyleSheet(button_style)
    button_layout.addWidget(confirm_button)

    cancel_button = QPushButton("Cancel", window)
    cancel_button.setFixedWidth(100)
    cancel_button.setStyleSheet(button_style)
    button_layout.addWidget(cancel_button)

    confirm_button.clicked.connect(lambda: on_confirm_clicked(window, combo_box, due_checkbox, total_amount, data))

    layout.addLayout(button_layout)

def on_confirm_clicked(window, combo_box, due_checkbox, total_amount, data):
    payment_mode = combo_box.currentText()
    
    if payment_mode == "Cash" or (payment_mode == "UPI" and due_checkbox.isChecked()):
        # Show confirmation message box for Cash or UPI with Due
        if show_confirmation_messagebox(window):
            handle_confirm_click(window, payment_mode, due_checkbox.isChecked(), total_amount, data)
    else:
        # For UPI without Due, skip HTML generation and open the UPI payment dialog
        show_upi_payment_dialog(window, total_amount, data)


def show_confirmation_messagebox(window):
    msg_box = QMessageBox(window)
    msg_box.setIcon(QMessageBox.Question)
    msg_box.setText("Are you sure you want to proceed with this payment?")
    msg_box.setWindowTitle("Confirm Payment")
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    return msg_box.exec_() == QMessageBox.Yes

def handle_confirm_click(window, payment_mode, due_checked, total_amount, data):
    full_data = data.copy()
    full_data["Payment Mode"] = payment_mode
    full_data[TOTAL_AMOUNT_LABEL] = total_amount
    full_data[PAYMENT_STATUS_LABEL] = NOT_PAID_STATUS if due_checked else PAID_STATUS
    generate_html(full_data, RFID_DETAILS_FILE)

    if payment_mode == "Cash" or (payment_mode == "UPI" and due_checked):
        show_payment_receipt_window(window)  # Pass the new window as parent
    else:
        show_upi_payment_dialog(window, total_amount, data)  # Keep the new window as parent


