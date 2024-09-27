from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton
from app.utils.cursor.entry_box import MyLineEdit

def setup_auth_edit_do_ui(dialog):
    layout = QGridLayout()

    # Define the label style
    label_style = "font-size: 14px; font-weight: bold;"

    # Username input
    username_label = QLabel("Username:")
    username_label.setStyleSheet(label_style)  # Apply the style to the label
    dialog.username_input = MyLineEdit()
    layout.addWidget(username_label, 0, 0)
    layout.addWidget(dialog.username_input, 0, 1)

    # Password input
    password_label = QLabel("Password:")
    password_label.setStyleSheet(label_style)  # Apply the style to the label
    dialog.password_input = MyLineEdit()
    layout.addWidget(password_label, 1, 0)
    layout.addWidget(dialog.password_input, 1, 1)

    # DO Number input
    do_number_label = QLabel("DO Number:")
    do_number_label.setStyleSheet(label_style)  # Apply the style to the label
    dialog.do_number_input = MyLineEdit()
    layout.addWidget(do_number_label, 2, 0)
    layout.addWidget(dialog.do_number_input, 2, 1)

    # Confirm and Cancel buttons
    dialog.confirm_button = QPushButton("Confirm")
    dialog.cancel_button = QPushButton("Cancel")

    # Set the same size for both buttons
    button_width = 100
    button_height = 30
    dialog.confirm_button.setFixedSize(button_width, button_height)
    dialog.cancel_button.setFixedSize(button_width, button_height)

    # Add buttons to the layout
    layout.addWidget(dialog.confirm_button, 3, 0)
    layout.addWidget(dialog.cancel_button, 3, 1)

    dialog.setLayout(layout)
    
    return dialog.confirm_button, dialog.cancel_button
