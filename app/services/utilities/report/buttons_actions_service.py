from PyQt5.QtWidgets import QLabel, QDateEdit, QTimeEdit, QComboBox, QLineEdit

def reset_all_elements(elements):
    """
    Reset all elements to their default state.
    :param elements: A dictionary of elements to be reset.
    """
    for label in ["from_date_label", "to_date_label", "from_time_label", "to_time_label", "vehicle_type_label", "search_label"]:
        elements[label].show()

    for entry in ["from_date_value", "to_date_value", "from_time_value", "to_time_value", "vehicle_type_value", "search_value"]:
        elements[entry].show()

def handle_button_action(button_text, elements):
    """
    Handle button actions to update the UI elements.
    :param button_text: The text of the clicked button.
    :param elements: A dictionary of UI elements to be updated.
    """
    reset_all_elements(elements)

    if button_text == "Summary":
        elements["vehicle_type_label"].hide()
        elements["vehicle_type_value"].hide()
        elements["search_label"].setText("Vehicle No:")

    elif button_text == "Weighbridge Wise":
        elements["search_label"].setText("Weighbridge No:")

    elif button_text == "Shift Wise":
        elements["search_label"].setText("Vehicle No:")
        elements["from_time_label"].hide()
        elements["from_time_value"].hide()
        elements["to_time_label"].hide()
        elements["to_time_value"].hide()

    elif button_text == "Do Wise":
        elements["search_label"].setText("DO Number:")

    elif button_text == "Vehicle Type":
        elements["search_label"].setText("Vehicle No:")

    elif button_text == "Validity Wise":
        elements["search_label"].setText("Vehicle No:")

    elif button_text == "Registration Details":
        elements["search_label"].setText("Vehicle No:")
        elements["from_date_label"].hide()
        elements["from_date_value"].hide()
        elements["to_date_label"].hide()
        elements["to_date_value"].hide()
        elements["from_time_label"].hide()
        elements["from_time_value"].hide()
        elements["to_time_label"].hide()
        elements["to_time_value"].hide()
