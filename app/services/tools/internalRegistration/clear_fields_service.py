# app/services/tools/internalRegistration/clear_fields_service.py

from PyQt5.QtWidgets import QLineEdit, QComboBox, QDateEdit
from PyQt5.QtCore import QDate
from app.utils.cursor.entry_box import MyLineEdit

def clear_fields(window,fields):
    """
    Clear all fields except the 'Type of Vehicle' and reset the calendar to the current date.
    
    :param fields: A dictionary containing field names as keys and their corresponding widgets (MyLineEdit/QComboBox/QDateEdit) as values.
    """
    for field_name, field_widget in fields.items():
        if isinstance(field_widget, MyLineEdit):
            if field_name != 'vehicle_type':
                field_widget.clear()  # Clear text fields
        elif isinstance(field_widget, QDateEdit):
            field_widget.setDate(QDate.currentDate())  # Reset calendar to current date
        elif isinstance(field_widget, QComboBox):
            if field_name != 'vehicle_type':
                field_widget.setCurrentIndex(-1)  # Deselect ComboBox items

    window.status_label.setText("Status: Please Enter Vehicle Number or RFID Tag")
