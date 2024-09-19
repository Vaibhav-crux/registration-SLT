# app\ui\toolsWindow\internalRfidTag\internal_rfid_ui.py

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt

def setup_ui(window):
    """
    Set up the UI layout for the InternalRegistrationWindow.
    
    :param window: The QDialog window to set up the UI on.
    """
    # Create the main layout
    main_layout = QVBoxLayout()

    # Create a horizontal layout for the Name label and text box
    hbox = QHBoxLayout()

    # Create the Name label
    name_label = QLabel("Name:", window)
    name_label.setAlignment(Qt.AlignLeft)
    name_label.setStyleSheet("font-size: 14px;")
    hbox.addWidget(name_label)

    # Create the Name text box with only the bottom border (professional blue)
    name_input = QLineEdit(window)
    name_input.setFixedWidth(300)  # Set width of the input field
    name_input.setStyleSheet("""
        QLineEdit {
            border-top: none;
            border-left: none;
            border-right: none;
            border-bottom: 2px solid #007bff;  /* Professional blue bottom border */
            padding: 2px;
        }
        """)
    hbox.addWidget(name_input)

    # Add the horizontal layout (hbox) to the main layout
    main_layout.addLayout(hbox)

    # Set the layout on the window
    window.setLayout(main_layout)
