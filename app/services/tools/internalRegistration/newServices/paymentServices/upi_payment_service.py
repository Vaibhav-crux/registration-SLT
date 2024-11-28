from PyQt5.QtWidgets import QDialog, QPushButton
from app.ui.toolsWindow.internalRfidTag.newWindow.paymentWindow.upi_payment_ui import setup_upi_payment_ui
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window

def show_upi_payment_dialog(parent=None, total_amount=None, data=None):
    """
    Function to create and show the UPI payment dialog.

    :param parent: The parent widget for the dialog, if any.
    :param total_amount: Total amount passed from the new window.
    :param data: Data passed from the new window.
    """
    dialog = QDialog(parent)
    dialog.setWindowTitle("UPI Payment")
    dialog.setGeometry(300, 300, 400, 400)
    center_window(dialog)

    # Setup the UI for the dialog
    setup_upi_payment_ui(dialog, total_amount, data)

    # Execute the dialog as a modal window
    dialog.exec_()
