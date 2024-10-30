# app/ui/toolsWindow/internalRfidTag/deleteWindow/delete_window_ui.py
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFrame
from app.utils.mode_utils import is_dark_mode
from app.style.default_styles import dark_mode_style, light_mode_style, button_style

def setup_delete_window_ui(window, rfid_tag, vehicle_no):
    """
    Set up the UI layout for the delete confirmation window.
    :param window: The QDialog window to set up the UI on.
    :param rfid_tag: The RFID tag to be deleted.
    :param vehicle_no: The vehicle number to be deleted.
    """
    # Create the main layout
    main_layout = QVBoxLayout()

    # Apply the appropriate stylesheet for textboxes
    dark_mode = is_dark_mode()
    common_textbox_style = dark_mode_style if dark_mode else light_mode_style
    label_style = "font-size: 14px; font-weight: 600;"

    # User ID and Password fields
    user_id_label = QLabel("User ID:", window)
    user_id_input = QLineEdit(window)
    user_id_input.setStyleSheet(common_textbox_style)

    password_label = QLabel("Password:", window)
    password_input = QLineEdit(window)
    password_input.setEchoMode(QLineEdit.Password)
    password_input.setStyleSheet(common_textbox_style)

    user_id_input.setFixedWidth(300)
    password_input.setFixedWidth(300)

    # Layout for User ID
    user_id_layout = QHBoxLayout()
    user_id_layout.addWidget(user_id_label)
    user_id_layout.addWidget(user_id_input)

    # Layout for Password
    password_layout = QHBoxLayout()
    password_layout.addWidget(password_label)
    password_layout.addWidget(password_input)

    main_layout.addLayout(user_id_layout)
    main_layout.addLayout(password_layout)

    # Frame for deletion information
    info_frame = QFrame(window)
    info_frame.setStyleSheet("background-color: #ff4c4c; padding: 10px; border-radius: 10px;")
    info_layout = QVBoxLayout(info_frame)

    deleting_label = QLabel("Deleting", window)
    deleting_label.setStyleSheet(label_style)
    rfid_label = QLabel(f"RFID Tag: {rfid_tag}", window)
    rfid_label.setStyleSheet(label_style)
    vehicle_label = QLabel(f"Vehicle Number: {vehicle_no}", window)
    vehicle_label.setStyleSheet(label_style)

    info_layout.addWidget(deleting_label)
    info_layout.addWidget(rfid_label)
    info_layout.addWidget(vehicle_label)

    main_layout.addWidget(info_frame)

    # Confirm and Cancel buttons
    button_layout = QHBoxLayout()
    confirm_button = QPushButton("Confirm", window)
    cancel_button = QPushButton("Cancel", window)

    confirm_button.setStyleSheet(button_style)
    cancel_button.setStyleSheet(button_style)

    button_layout.addWidget(confirm_button)
    button_layout.addWidget(cancel_button)

    main_layout.addLayout(button_layout)

    window.setLayout(main_layout)

    return user_id_input, password_input, confirm_button, cancel_button
