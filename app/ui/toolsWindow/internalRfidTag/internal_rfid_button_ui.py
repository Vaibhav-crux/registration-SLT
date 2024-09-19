from PyQt5.QtWidgets import QHBoxLayout, QPushButton
from app.style.default_styles import button_style

def create_button_layout(window):
    """
    Creates and returns a layout containing the 'New', 'Edit', 'Delete', and 'Clear' buttons.
    
    :param window: The QDialog window to set up the buttons on.
    :return: QHBoxLayout with the buttons.
    """
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

    # Clear Button
    clear_button = QPushButton("Clear", window)
    clear_button.setFixedWidth(100)
    clear_button.setStyleSheet(button_style)
    button_layout.addWidget(clear_button)

    return button_layout
