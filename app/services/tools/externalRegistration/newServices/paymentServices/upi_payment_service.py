from PyQt5.QtWidgets import QDialog, QPushButton
from app.ui.toolsWindow.externalRfidTag.newWindow.paymentWindow.upi_payment_ui import setup_upi_payment_ui
from app.utils.frame_utils import apply_drop_shadow, center_window
from app.utils.mode_utils import apply_mode_styles, is_dark_mode,apply_window_flags,set_dark_mode_title_bar

def show_upi_payment_dialog(parent=None, total_amount=None, data=None):
    """
    Function to create and show the UPI payment dialog.

    :param parent: The parent widget for the dialog, if any.
    :param total_amount: Total amount passed from the new window.
    :param data: Data passed from the new window.
    """
    dark_mode = is_dark_mode()
    dialog = QDialog(parent)
    dialog.setWindowTitle("UPI Payment")
    if dark_mode:
        dialog.setStyleSheet("background-color: #2e2e2e; color: white;")
        set_dark_mode_title_bar(dialog)
    apply_window_flags(dialog)
    dialog.setGeometry(300, 300, 400, 400)
    center_window(dialog)

    # Setup the UI for the dialog
    setup_upi_payment_ui(dialog, total_amount, data)

    # Execute the dialog as a modal window
    dialog.exec_()
