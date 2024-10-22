# app/services/tools/internalRegistration/newServices/paymentServices/upi_payment_service.py

from PyQt5.QtWidgets import QDialog
from app.ui.toolsWindow.internalRfidTag.newWindow.paymentWindow.upi_payment_ui import setup_upi_payment_ui

def show_upi_payment_dialog(parent=None):
    """
    Function to create and show the UPI payment dialog.
    
    :param parent: The parent widget for the dialog, if any.
    """
    dialog = QDialog(parent)
    dialog.setWindowTitle("UPI Payment")
    dialog.setGeometry(300, 300, 400, 400)

    # Setup the UI for the dialog
    setup_upi_payment_ui(dialog)

    # Execute the dialog as a modal window
    dialog.exec_()
