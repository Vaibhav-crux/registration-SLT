from PyQt5.QtWidgets import QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QIntValidator
from app.utils.cursor.entry_box import MyLineEdit  # Import the custom line edit class

def setup_ui(window):
    window.setWindowTitle("Edit User Details")
    layout = QGridLayout()

    # Define label style for bold text and 14px font size
    label_style = "font-weight: bold; font-size: 14px;"

    # Create labels and text fields using MyLineEdit
    window.password_label = QLabel("Password:")
    window.password_label.setStyleSheet(label_style)
    window.password_input = MyLineEdit()  # Use custom MyLineEdit
    window.password_input.setEchoMode(MyLineEdit.Password)  # Mask the password input
    
    window.fullname_label = QLabel("Fullname:")
    window.fullname_label.setStyleSheet(label_style)
    window.fullname_input = MyLineEdit()  # Use custom MyLineEdit
    
    window.email_label = QLabel("Email:")
    window.email_label.setStyleSheet(label_style)
    window.email_input = MyLineEdit()  # Use custom MyLineEdit
    
    window.mobile_label = QLabel("Mobile Number:")
    window.mobile_label.setStyleSheet(label_style)
    window.mobile_input = MyLineEdit()  # Use custom MyLineEdit
    window.mobile_input.setValidator(QIntValidator())  # Restrict to integers
    window.mobile_input.setMaxLength(10)
    
    window.address_label = QLabel("Address:")
    window.address_label.setStyleSheet(label_style)
    window.address_input = MyLineEdit()  # Use custom MyLineEdit

    # Create buttons
    window.save_button = QPushButton("Save")
    window.cancel_button = QPushButton("Cancel")

    # Set fixed width for buttons
    button_width = 100  # Adjust the width as needed
    window.save_button.setFixedWidth(button_width)
    window.cancel_button.setFixedWidth(button_width)

    # Add widgets to the grid layout
    layout.addWidget(window.password_label, 0, 0)
    layout.addWidget(window.password_input, 0, 1)
    
    layout.addWidget(window.fullname_label, 1, 0)
    layout.addWidget(window.fullname_input, 1, 1)
    
    layout.addWidget(window.email_label, 2, 0)
    layout.addWidget(window.email_input, 2, 1)
    
    layout.addWidget(window.mobile_label, 3, 0)
    layout.addWidget(window.mobile_input, 3, 1)
    
    layout.addWidget(window.address_label, 4, 0)
    layout.addWidget(window.address_input, 4, 1)

    # Add buttons side by side
    layout.addWidget(window.save_button, 5, 0)
    layout.addWidget(window.cancel_button, 5, 1)

    window.setLayout(layout)
