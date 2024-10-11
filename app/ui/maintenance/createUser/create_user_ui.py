from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from app.utils.cursor.entry_box import MyLineEdit, MyComboBox  # Import the custom classes
from PyQt5.QtGui import QIntValidator
from app.utils.mode_utils import is_dark_mode
from app.style.default_styles import dark_mode_style, light_mode_style, button_style

def setup_ui(window):
    main_layout = QVBoxLayout()
    dark_mode = is_dark_mode()
    common_textbox_style = dark_mode_style if dark_mode else light_mode_style

    def add_field(layout, label_text, widget):
        hbox = QHBoxLayout()
        label = QLabel(label_text, window)
        label.setStyleSheet("font-size: 14px; font-weight: 600;")
        hbox.addWidget(label)
        hbox.addWidget(widget)
        layout.addLayout(hbox)

    user_name = MyLineEdit(window)
    user_name.setFixedWidth(300)
    user_name.setStyleSheet(common_textbox_style)
    add_field(main_layout, "User Name:", user_name)

    password = MyLineEdit(window)
    password.setEchoMode(MyLineEdit.Password)
    password.setFixedWidth(300)
    password.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Password:", password)

    auth_type = MyComboBox(window)
    auth_type.addItems(["User", "Admin"])
    auth_type.setFixedWidth(300)
    auth_type.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Auth Type:", auth_type)

    employee_id = MyLineEdit(window)
    employee_id.setFixedWidth(300)
    employee_id.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Employee ID:", employee_id)

    full_name = MyLineEdit(window)
    full_name.setFixedWidth(300)
    full_name.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Full Name:", full_name)

    email = MyLineEdit(window)
    email.setFixedWidth(300)
    email.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Email:", email)

    designation = MyLineEdit(window)
    designation.setFixedWidth(300)
    designation.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Designation:", designation)

    address = MyLineEdit(window)
    address.setFixedWidth(300)
    address.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Address:", address)

    mobile_number = MyLineEdit(window)
    mobile_number.setFixedWidth(300)
    mobile_number.setValidator(QIntValidator())  # Restrict to integers
    mobile_number.setMaxLength(10)  # Limit the input to 10 characters
    mobile_number.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Mobile Number:", mobile_number)

    organisation = MyLineEdit(window)
    organisation.setFixedWidth(300)
    organisation.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Organisation:", organisation)

    button_layout = QHBoxLayout()
    submit_button = QPushButton("Submit", window)
    submit_button.setFixedWidth(100)
    submit_button.setStyleSheet(button_style)
    button_layout.addWidget(submit_button)

    clear_button = QPushButton("Clear", window)
    clear_button.setFixedWidth(100)
    clear_button.setStyleSheet(button_style)
    button_layout.addWidget(clear_button)

    delete_button = QPushButton("Delete", window)
    delete_button.setFixedWidth(100)
    delete_button.setStyleSheet(button_style)
    button_layout.addWidget(delete_button)

    main_layout.addLayout(button_layout)
    window.setLayout(main_layout)

    return {
        "user_name": user_name,
        "password": password,
        "auth_type": auth_type,
        "emp_id": employee_id,
        "full_name": full_name,
        "email": email,
        "designation": designation,
        "address": address,
        "mobile_number": mobile_number,
        "organisation": organisation,
        "submit_button": submit_button,
        "clear_button": clear_button,
        "delete_button": delete_button
    }
