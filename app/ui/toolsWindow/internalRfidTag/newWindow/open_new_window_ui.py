# app/ui/toolsWindow/internalRfidTag/newWindow/open_new_window_ui.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QComboBox
from app.utils.mode_utils import apply_mode_styles, is_dark_mode
from app.style.default_styles import dark_mode_style, light_mode_style, button_style
from app.style.disabled_styles import disabled_style
from app.services.tools.internalRegistration.newServices.checkbox_status_service import update_due_checkbox_status
from app.services.tools.internalRegistration.newServices.autofill_total_amount_service import calculate_total_amount
from app.services.tools.internalRegistration.newServices.paymentServices.upi_payment_service import show_upi_payment_dialog
from app.utils.template.html_generator import generate_html

def setup_new_window_ui(window, data):
    apply_mode_styles(window)

    dark_mode = is_dark_mode()
    base_style = dark_mode_style if dark_mode else light_mode_style

    layout = QVBoxLayout()

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

    def add_label_and_value(layout, label_text, value, fixed_width=300):
        hbox = QHBoxLayout()
        label = QLabel(label_text + ":", window)
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

    for key, value in data.items():
        if key in key_to_label:
            add_label_and_value(layout, key_to_label[key], value)

    vehicle_type = data.get("vehicle_type", "")
    total_amount = calculate_total_amount(vehicle_type)
    add_label_and_value(layout, "Total Amount", str(total_amount))

    def add_payment_mode_with_due(layout, label_text, items, fixed_width=230):
        hbox = QHBoxLayout()
        label = QLabel(label_text, window)
        label.setAlignment(Qt.AlignLeft)
        label.setStyleSheet("font-size: 14px; font-weight: bold;")
        hbox.addWidget(label)

        combo_box = QComboBox(window)
        combo_box.addItems(items)
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

        def update_due_checkbox(index):
            selected_payment_mode = combo_box.itemText(index)
            checkbox_enabled = update_due_checkbox_status(selected_payment_mode)
            due_checkbox.setEnabled(checkbox_enabled)
            if not checkbox_enabled:
                due_checkbox.setChecked(False)

        combo_box.currentIndexChanged.connect(update_due_checkbox)

        update_due_checkbox(combo_box.currentIndex())

        layout.addLayout(hbox)
        
        return combo_box, due_checkbox

    combo_box, due_checkbox = add_payment_mode_with_due(layout, "Payment Mode:", ["Cash", "UPI"])

    button_layout = QHBoxLayout()

    confirm_button = QPushButton("Confirm", window)
    confirm_button.setFixedWidth(100)
    confirm_button.setStyleSheet(button_style)
    button_layout.addWidget(confirm_button)

    cancel_button = QPushButton("Cancel", window)
    cancel_button.setFixedWidth(100)
    cancel_button.setStyleSheet(button_style)
    button_layout.addWidget(cancel_button)

    layout.addLayout(button_layout)

    # Set focus to the payment mode combo box when the window opens
    combo_box.setFocus()

    # Connect confirm button clicked event to generate HTML or open a dialog
    def on_confirm_clicked():
        if combo_box.currentText() == "Cash":
            full_data = data.copy()
            full_data["Payment Mode"] = "Cash"
            full_data["Total Amount"] = total_amount
            generate_html(full_data, "rfid_details.html")
        elif combo_box.currentText() == "UPI" and not due_checkbox.isChecked():
            show_upi_payment_dialog(window)

    confirm_button.clicked.connect(on_confirm_clicked)

    window.setLayout(layout)
