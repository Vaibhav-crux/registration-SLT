from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit, QPushButton

def setup_edit_do_maintenance_ui(dialog, do_details):
    layout = QGridLayout()

    # Define the label style
    label_style = "font-size: 14px; font-weight: bold;"

    # Create labels and line edits for each DO detail
    fields = [
        ("DO Number", "doNumber"),
        ("Weighbridge No", "weighbridgeNo"),
        ("Transporter", "transporter"),
        ("Permissido Nameon", "permissidoNameon"),
        ("Valid Through", "validThrough"),
        ("Validity Till", "validityTill"),
        ("Alloted Qty", "allotedQty"),
        ("Released Qty", "releasedQty"),
        ("Left Qty", "leftQty"),
        ("DO Address", "doAddress"),
        ("DO Route", "doRoute"),
        ("Sales Order", "salesOrder"),
        ("Customer ID", "customerId"),
        ("Mobile Number", "mobileNumber"),
    ]

    dialog.line_edits = {}

    for row, (label_text, field_name) in enumerate(fields):
        label = QLabel(label_text + ":")
        label.setStyleSheet(label_style)
        line_edit = QLineEdit()
        line_edit.setText(str(getattr(do_details, field_name, "")))  # Ensure the value is a string
        layout.addWidget(label, row, 0)
        layout.addWidget(line_edit, row, 1)
        dialog.line_edits[field_name] = line_edit

    # Save and Cancel buttons
    dialog.save_button = QPushButton("Save")
    dialog.cancel_button = QPushButton("Cancel")
    layout.addWidget(dialog.save_button, len(fields), 0)
    layout.addWidget(dialog.cancel_button, len(fields), 1)

    dialog.setLayout(layout)

    return dialog.save_button, dialog.cancel_button