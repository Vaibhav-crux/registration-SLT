import os
from PyQt5.QtWidgets import QDialog
from app.ui.toolsWindow.externalRfidTag.newWindow.paymentWindow.payment_receipt_ui import setup_payment_receipt_ui
from app.utils.mode_utils import apply_mode_styles, apply_window_flags

def show_payment_receipt_window(parent_window):
    """
    Opens a dialog to display the payment receipt HTML file.
    Reads the HTML file from the static directory and shows the dialog.
    """
    dialog = QDialog(parent_window)  # Use parent_window as the parent
    dialog.setWindowTitle("Payment Receipt")
    dialog.setGeometry(150, 150, 800, 600)  # Set initial size of the dialog

    # Apply mode (dark or light) to the dialog
    apply_mode_styles(dialog)

    # Apply window flags (remove help button, show close button)
    apply_window_flags(dialog)

    # Path to the generated HTML file
    html_file_path = os.path.join("app", "static", "html", "rfid_details.html")

    # Ensure the path is valid and the file exists before proceeding
    if os.path.exists(html_file_path):
        # Set up the payment receipt UI with the generated HTML file path
        setup_payment_receipt_ui(dialog, html_file_path, parent_window)  # Pass the HTML file path
        # Display the dialog
        dialog.exec_()
    else:
        print(f"Error: HTML file not found at {html_file_path}!")
