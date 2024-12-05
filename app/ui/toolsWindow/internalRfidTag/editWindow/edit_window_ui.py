# edit_window_ui.py
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QPushButton
from PyQt5.QtCore import QDate
from app.utils.mode_utils import is_dark_mode
from app.style.default_styles import dark_mode_style, light_mode_style, button_style
from app.style.disabled_styles import disabled_style
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window
from app.utils.cursor.entry_box import MyLineEdit

def setup_edit_window_ui(window, data, enabled_fields):
    main_layout = QVBoxLayout()
    dark_mode = is_dark_mode()
    common_textbox_style = dark_mode_style if dark_mode else light_mode_style
    label_style = "font-size: 14px; font-weight: 600;"
    combined_style = common_textbox_style + disabled_style

    fields = {}

    for key, value in data.items():
        # Skip the "validity_till" field since it will be handled as "calendar"
        if key == "validity_till":
            continue
        
        # Set label and field according to key
        label_text = "Validity Till:" if key == "calendar" else f"{key.replace('_', ' ').capitalize()}:"
        label = QLabel(label_text, window)
        label.setStyleSheet(label_style)

        field = None
        if key == "vehicle_type":
            field = MyLineEdit(window)
            field.setText(value)
            field.setReadOnly(True)  # Read-only vehicle type
        elif key == "calendar":  # Treat "calendar" as "Validity Till"
            field = QDateEdit(window)
            field.setDate(QDate.fromString(value, "yyyy-MM-dd"))
        else:
            field = MyLineEdit(window)
            field.setText(value)

        # Enable or disable fields based on enabled_fields
        if key not in enabled_fields or key in ["rfid_tag", "vehicle_no", "do_number"]:
            field.setReadOnly(True)
            field.setStyleSheet(combined_style)
        else:
            field.setEnabled(True)
            field.setStyleSheet(common_textbox_style)

        field.setFixedWidth(300)
        fields[key] = field

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(field)
        main_layout.addLayout(layout)

    # Ensure rfid_tag is added to fields
    if "rfid_tag" not in fields:
        rfid_label = QLabel("RFID Tag:", window)
        rfid_label.setStyleSheet(label_style)
        rfid_field = MyLineEdit(window)
        rfid_field.setText(data.get("rfid_tag", ""))
        rfid_field.setReadOnly(True)
        rfid_field.setStyleSheet(combined_style)
        rfid_field.setFixedWidth(300)
        fields["rfid_tag"] = rfid_field

        rfid_layout = QHBoxLayout()
        rfid_layout.addWidget(rfid_label)
        rfid_layout.addWidget(rfid_field)
        main_layout.addLayout(rfid_layout)

    button_layout = QHBoxLayout()
    confirm_button = QPushButton("Confirm", window)
    cancel_button = QPushButton("Cancel", window)

    confirm_button.setStyleSheet(button_style)
    cancel_button.setStyleSheet(button_style)

    button_layout.addWidget(confirm_button)
    button_layout.addWidget(cancel_button)

    main_layout.addLayout(button_layout)
    window.setLayout(main_layout)

    return fields, confirm_button, cancel_button
