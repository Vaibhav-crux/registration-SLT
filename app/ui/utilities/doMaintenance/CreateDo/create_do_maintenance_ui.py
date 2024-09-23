from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QDoubleSpinBox, QDateEdit, QApplication
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIntValidator, QKeyEvent
# Import mode utility function
from app.utils.mode_utils import is_dark_mode
# Import styles from default_styles
from app.style.default_styles import dark_mode_style, light_mode_style, button_style

from app.utils.cursor.entry_box import MyLineEdit, MyDoubleSpinBox, MyDateEdit

def setup_create_do_ui(window):
    """
    Set up the UI layout for the Create DO Maintenance window with input restrictions.
    
    :param window: The QDialog window to set up the UI on.
    """
    # Create the main layout
    main_layout = QVBoxLayout()

    # Check if the current mode is dark or light
    dark_mode = is_dark_mode()

    # Apply the appropriate stylesheet
    if dark_mode:
        common_textbox_style = dark_mode_style
    else:
        common_textbox_style = light_mode_style

    # Helper function to create a label and input field in a horizontal layout
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

    # DO Number input (integer only)
    do_number_input = MyLineEdit(window)
    do_number_input.setFixedWidth(300)
    do_number_input.setValidator(QIntValidator())  # Restrict to integers
    do_number_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "DO Number:", do_number_input)

    # Weighbridge Number input (no restrictions)
    weighbridge_no_input = MyLineEdit(window)
    weighbridge_no_input.setFixedWidth(300)
    weighbridge_no_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Weighbridge No:", weighbridge_no_input)

    # Transporter input (no restrictions)
    transporter_input = MyLineEdit(window)
    transporter_input.setFixedWidth(300)
    transporter_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Transporter:", transporter_input)

    # Permission Name input (no restrictions)
    permissido_nameon_input = MyLineEdit(window)
    permissido_nameon_input.setFixedWidth(300)
    permissido_nameon_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Permission Name:", permissido_nameon_input)

    # Valid Through input (no restrictions)
    valid_through_input = MyLineEdit(window)
    valid_through_input.setFixedWidth(300)
    valid_through_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Valid Through:", valid_through_input)

    # Validity Till input (as a date)
    validity_till_input = MyDateEdit(window)
    validity_till_input.setFixedWidth(300)
    validity_till_input.setCalendarPopup(True)  # Enable calendar for easy date selection
    validity_till_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Validity Till:", validity_till_input)

    # Alloted Quantity input (as a float field)
    alloted_qty_input = MyDoubleSpinBox(window)
    alloted_qty_input.setFixedWidth(300)
    alloted_qty_input.setDecimals(2)
    alloted_qty_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Alloted Quantity:", alloted_qty_input)

    # Released Quantity input (as a float field)
    released_qty_input = MyDoubleSpinBox(window)
    released_qty_input.setFixedWidth(300)
    released_qty_input.setDecimals(2)
    released_qty_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Released Quantity:", released_qty_input)

    # Left Quantity input (as a float field)
    left_qty_input = MyDoubleSpinBox(window)
    left_qty_input.setFixedWidth(300)
    left_qty_input.setDecimals(2)
    left_qty_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Left Quantity:", left_qty_input)

    # DO Address input (no restrictions)
    do_address_input = MyLineEdit(window)
    do_address_input.setFixedWidth(300)
    do_address_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "DO Address:", do_address_input)

    # DO Route input (no restrictions)
    do_route_input = MyLineEdit(window)
    do_route_input.setFixedWidth(300)
    do_route_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "DO Route:", do_route_input)

    # Sales Order input (no restrictions)
    sales_order_input = MyLineEdit(window)
    sales_order_input.setFixedWidth(300)
    sales_order_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Sales Order:", sales_order_input)

    # Customer ID input (no restrictions)
    customer_id_input = MyLineEdit(window)
    customer_id_input.setFixedWidth(300)
    customer_id_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Customer ID:", customer_id_input)

    # Mobile Number input
    mobile_number_input = MyLineEdit(window)
    mobile_number_input.setFixedWidth(300)
    mobile_number_input.setValidator(QIntValidator())  # Restrict to integers
    mobile_number_input.setMaxLength(10)  # Limit the input to 10 characters
    mobile_number_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Mobile Number:", mobile_number_input)


    # Create buttons
    button_layout = QHBoxLayout()

    # Save Button
    save_button = QPushButton("Save", window)
    save_button.setFixedWidth(100)
    save_button.setStyleSheet(button_style)
    button_layout.addWidget(save_button)

    # Clear Button
    clear_button = QPushButton("Clear", window)
    clear_button.setFixedWidth(100)
    clear_button.setStyleSheet(button_style)
    button_layout.addWidget(clear_button)

    # Add button layout to main layout
    main_layout.addLayout(button_layout)

    # Set the main layout
    window.setLayout(main_layout)

    return (
        do_number_input, 
        weighbridge_no_input, 
        transporter_input, 
        permissido_nameon_input, 
        valid_through_input, 
        validity_till_input, 
        alloted_qty_input, 
        released_qty_input, 
        left_qty_input, 
        do_address_input, 
        do_route_input, 
        sales_order_input, 
        customer_id_input, 
        mobile_number_input,
        save_button, 
        clear_button
    )
