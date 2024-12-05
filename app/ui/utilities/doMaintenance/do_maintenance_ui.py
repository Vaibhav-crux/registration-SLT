from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
# Import mode utility function
from app.utils.mode_utils import is_dark_mode
# Import styles from default_styles
from app.style.default_styles import dark_mode_style, light_mode_style, button_style
from app.utils.cursor.entry_box import MyLineEdit

def setup_ui(window):
    """
    Set up the UI layout for the DO Maintenance window with fields and buttons.
    
    :param window: The QDialog window to set up the UI on.
    :return: The buttons for further connections.
    """
    # Create the main layout
    main_layout = QVBoxLayout()

    # Check if the current mode is dark or light
    dark_mode = is_dark_mode()

    # Apply the appropriate stylesheet
    common_textbox_style = dark_mode_style if dark_mode else light_mode_style

    # Helper function to create a label and field in a horizontal layout
    def add_field(layout, label_text, widget):
        hbox = QHBoxLayout()
        label = QLabel(label_text, window)
        label.setStyleSheet("""
            font-size: 14px;
            font-weight: 600;  /* Semi-bold */
        """)
        label.setAlignment(Qt.AlignLeft)
        hbox.addWidget(label)
        hbox.addWidget(widget)
        layout.addLayout(hbox)

    # DO Number
    do_number = MyLineEdit(window)
    do_number.setFixedWidth(300)
    do_number.setStyleSheet(common_textbox_style)
    add_field(main_layout, "DO Number:", do_number)

    # Create buttons
    button_layout = QHBoxLayout()

    # New Button
    new_button = QPushButton("New", window)
    new_button.setFixedWidth(100)
    new_button.setStyleSheet(button_style)
    button_layout.addWidget(new_button)

    # Edit Button
    edit_button = QPushButton("Edit", window)
    edit_button.setFixedWidth(100)
    edit_button.setStyleSheet(button_style)
    button_layout.addWidget(edit_button)

    # Delete Button
    delete_button = QPushButton("Delete", window)
    delete_button.setFixedWidth(100)
    delete_button.setStyleSheet(button_style)
    button_layout.addWidget(delete_button)

    # Search Button (renamed from "Clear" to "Search" as per original code)
    search_button = QPushButton("Search", window)
    search_button.setFixedWidth(100)
    search_button.setStyleSheet(button_style)
    button_layout.addWidget(search_button)

    # Add button layout to main layout
    main_layout.addLayout(button_layout)

    # Set the main layout
    window.setLayout(main_layout)

    # Store the widgets as instance variables
    window.do_number_input = do_number
    window.new_button = new_button
    window.edit_button = edit_button
    window.delete_button = delete_button
    window.search_button = search_button

    return new_button, edit_button, delete_button, search_button
