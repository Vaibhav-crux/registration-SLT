from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDateEdit
from app.style.default_styles import button_style
from app.services.tools.internalRegistration.clear_fields_service import clear_fields
from app.services.tools.internalRegistration.newServices.open_new_window_service import open_new_window

def create_button_layout(window, fields):
    """
    Creates and returns a layout containing the 'New', 'Edit', 'Delete', and 'Clear' buttons.
    
    :param window: The QDialog window to set up the buttons on.
    :param fields: A dictionary of field widgets to manage.
    :return: QHBoxLayout with the buttons.
    """
    button_layout = QHBoxLayout()

    # New Button
    new_button = QPushButton("New", window)
    new_button.setFixedWidth(100)
    new_button.setStyleSheet(button_style)
    new_button.clicked.connect(lambda: open_new_window({
        key: (field.text() if isinstance(field, QLineEdit) else 
              field.currentText() if isinstance(field, QComboBox) else 
              field.date().toString("yyyy-MM-dd")) 
        for key, field in fields.items() if field.isEnabled()  # Collect only enabled fields
    }))
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
    clear_button.clicked.connect(lambda: clear_fields(fields))
    button_layout.addWidget(clear_button)

    return button_layout
