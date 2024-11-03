from app.controllers.utilities.report.summary.fetch_all_data_controller import fetch_all_vehicle_data
from app.controllers.utilities.report.registration.fetch_registration_controller import fetch_all_registration_data
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QFrame, QGridLayout, QLabel, QDateEdit, QTimeEdit, QComboBox, QTableWidget
# Import other data-fetching functions as needed
from app.controllers.utilities.report.weighbridge.fetch_weighbridge_data import fetch_weighbridge_data
from app.controllers.utilities.report.shift.fetch_shift_data import fetch_shift_data
from app.controllers.utilities.report.do.fetch_do_data import fetch_do_data
from app.controllers.utilities.report.vehicle_type.fetch_vehicle_type_data import fetch_vehicle_type_data
from app.controllers.utilities.report.validity.fetch_validity_data import fetch_validity_data
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QFont

# Define constants for commonly used strings
VEHICLE_NO_LABEL = "Vehicle No:"
WEIGHBRIDGE_NO_LABEL = "Weighbridge No:"
DO_NUMBER_LABEL = "DO Number:"

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
    reset_all_elements(elements) # Reset UI elements if needed

    # Update UI elements based on the button pressed
    if button_text == "Summary":
        elements["vehicle_type_label"].hide()
        elements["vehicle_type_value"].hide()
        elements["search_label"].setText(VEHICLE_NO_LABEL)
        
        # Fetch the data
        column_names, data = fetch_all_vehicle_data()
        
    elif button_text == "Weighbridge Wise":
        elements["search_label"].setText(WEIGHBRIDGE_NO_LABEL)
        # Fetch the relevant data (implement this function as needed)
        column_names, data = fetch_weighbridge_data()

    elif button_text == "Shift Wise":
        elements["search_label"].setText(VEHICLE_NO_LABEL)
        elements["from_time_label"].hide()
        elements["from_time_value"].hide()
        elements["to_time_label"].hide()
        elements["to_time_value"].hide()
        # Fetch the relevant data (implement this function as needed)
        column_names, data = fetch_shift_data()

    elif button_text == "Do Wise":
        elements["search_label"].setText(DO_NUMBER_LABEL)
        # Fetch the relevant data (implement this function as needed)
        column_names, data = fetch_do_data()

    elif button_text == "Vehicle Type":
        elements["search_label"].setText(VEHICLE_NO_LABEL)
        # Fetch the relevant data (implement this function as needed)
        column_names, data = fetch_vehicle_type_data()

    elif button_text == "Validity Wise":
        elements["search_label"].setText(VEHICLE_NO_LABEL)
        # Fetch the relevant data (implement this function as needed)
        column_names, data = fetch_validity_data()

    elif button_text == "Registration Details":
        elements["search_label"].setText(VEHICLE_NO_LABEL)
        elements["from_date_label"].hide()
        elements["from_date_value"].hide()
        elements["to_date_label"].hide()
        elements["to_date_value"].hide()
        elements["from_time_label"].hide()
        elements["from_time_value"].hide()
        elements["to_time_label"].hide()
        elements["to_time_value"].hide()
        
        # Fetch the registration data
        column_names, data = fetch_all_registration_data()

    # After updating UI and fetching data, update the table
    table = elements.get("table")
    update_table(table, column_names, data)

def update_table(table, column_names, data):
    """
    Update the table widget with the fetched data.
    :param table: The QTableWidget to update.
    :param column_names: The list of column names to be displayed in the first row.
    :param data: The list of data tuples.
    """
    # Set the number of columns
    table.setColumnCount(len(column_names))

    # Set the number of rows (1 for column names + number of data rows)
    table.setRowCount(len(data) + 1)

    # Set the font for the first row to bold
    bold_font = QFont()
    bold_font.setBold(True)

    # Populate the first row with column names
    for column_index, column_name in enumerate(column_names):
        item = QTableWidgetItem(column_name)
        item.setFont(bold_font) # Set the font to bold
        table.setItem(0, column_index, item)

    # Populate the table with data starting from the second row
    for row_index, row_data in enumerate(data):
        for column_index, item in enumerate(row_data):
            table.setItem(row_index + 1, column_index, QTableWidgetItem(str(item)))

    # Hide the headers
    table.horizontalHeader().setVisible(False)
    table.verticalHeader().setVisible(False)

    # Make the table read-only
    table.setEditTriggers(QTableWidget.NoEditTriggers) # Disable editing
