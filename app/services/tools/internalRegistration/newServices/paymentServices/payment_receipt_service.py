import os
from PyQt5.QtWidgets import QDialog
from app.ui.toolsWindow.internalRfidTag.newWindow.paymentWindow.payment_receipt_ui import setup_payment_receipt_ui

def show_payment_receipt_window():
    """
    Opens a dialog to display the payment receipt HTML file.
    Reads the HTML file from the static directory and shows the dialog.
    """
    dialog = QDialog()
    dialog.setWindowTitle("Payment Receipt")
    dialog.setGeometry(150, 150, 800, 600)  # Set initial size of the dialog

    # Path to the generated HTML file
    html_file_path = os.path.join("app", "static", "html", "rfid_details.html")
    
    # Debug print to check the file path
    print(f"Reading HTML file from: {html_file_path}")
    
    # Ensure the path is valid and the file exists before proceeding
    if os.path.exists(html_file_path):
        # Set up the payment receipt UI with the generated HTML file path
        setup_payment_receipt_ui(dialog, html_file_path)
        # Display the dialog
        dialog.exec_()
    else:
        print(f"Error: HTML file not found at {html_file_path}!")
