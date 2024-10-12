from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton, QLineEdit

def setup_ui(dialog):
    dialog.setWindowTitle("Edit User Details")
    dialog.setGeometry(100, 100, 400, 200)

    layout = QGridLayout(dialog)
    layout.setHorizontalSpacing(0)  # Minimize horizontal spacing between label and text box
    layout.setVerticalSpacing(10)   # Set vertical spacing between rows

    # Create and style the Username label
    dialog.username_label = QLabel("Username:")
    dialog.username_label.setStyleSheet("font-size: 14px;")  # Increase font size to 14px
    dialog.username_input = QLineEdit()
    dialog.username_input.setFixedWidth(200)
    layout.addWidget(dialog.username_label, 0, 0)
    layout.addWidget(dialog.username_input, 0, 1, 1, 2)  # Span across two columns

    # Confirm and Cancel buttons on the third row
    dialog.confirm_button = QPushButton("Confirm")
    dialog.cancel_button = QPushButton("Cancel")

    # Set both buttons to be the same size and within the text box width
    button_width = (dialog.username_input.width() - 10) // 2
    dialog.confirm_button.setFixedWidth(button_width)
    dialog.cancel_button.setFixedWidth(button_width)

    # Add buttons to grid, positioned in columns 1 and 2 to fit under the text boxes
    layout.addWidget(dialog.confirm_button, 2, 1)
    layout.addWidget(dialog.cancel_button, 2, 2)

    # Stretch the second column to occupy extra space and push buttons to the right
    layout.setColumnStretch(0, 1)
    layout.setColumnStretch(1, 1)
    layout.setColumnStretch(2, 1)

    dialog.setLayout(layout)
