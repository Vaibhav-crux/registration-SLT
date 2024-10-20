# app/services/tools/internalRegistration/clear_fields_service.py

from PyQt5.QtWidgets import QLineEdit, QComboBox, QDateEdit
from PyQt5.QtCore import QDate

def clear_fields(fields):
    """
    Clear all fields except the 'Type of Vehicle' and reset the calendar to the current date.
    
    :param fields: A dictionary containing field names as keys and their corresponding widgets (QLineEdit/QComboBox/QDateEdit) as values.
    """
    for field_name, field_widget in fields.items():
        if isinstance(field_widget, QLineEdit):
            if field_name != 'vehicle_type':
                field_widget.clear()  # Clear text fields
        elif isinstance(field_widget, QDateEdit):
            field_widget.setDate(QDate.currentDate())  # Reset calendar to current date
        elif isinstance(field_widget, QComboBox):
            if field_name != 'vehicle_type':
                field_widget.setCurrentIndex(-1)  # Deselect ComboBox items
