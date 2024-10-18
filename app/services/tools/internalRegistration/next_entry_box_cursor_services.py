# app/services/tools/internalRegistration/next_entry_box_cursor_services.py

from PyQt5.QtWidgets import QLineEdit, QComboBox, QDateEdit, QPushButton

def focus_next_enabled_widget(current_widget, parent_widget):
    # Gather all input widgets that are focusable and enabled
    focusable_widgets = [
        widget for widget in parent_widget.findChildren((QLineEdit, QComboBox, QDateEdit))
        if widget.isEnabled() and (not isinstance(widget, (QLineEdit, QDateEdit)) or not widget.isReadOnly())
    ]

    # Find the "New" button
    new_button = None
    for widget in parent_widget.findChildren(QPushButton):
        if widget.text() == "New":
            new_button = widget
            break

    if current_widget in focusable_widgets:
        current_index = focusable_widgets.index(current_widget)
        # Calculate the next widget index
        next_index = (current_index + 1) % (len(focusable_widgets) + 1)  # +1 for the New button

        if next_index == len(focusable_widgets):  # If we reach the end of the focusable widgets
            new_button.setFocus()  # Set focus to the New button
        else:
            focusable_widgets[next_index].setFocus()  # Set focus to the next widget
    else:
        # If the current widget is not in the focusable list, set focus to the New button
        if new_button:
            new_button.setFocus()
