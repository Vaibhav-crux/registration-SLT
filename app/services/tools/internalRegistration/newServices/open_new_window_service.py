from PyQt5.QtWidgets import QDialog
from app.ui.toolsWindow.internalRfidTag.newWindow.open_new_window_ui import setup_new_window_ui
from app.utils.frame_utils import center_window
from app.utils.mode_utils import apply_mode_styles

class NewWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("RFID Details")
        self.setGeometry(150, 150, 400, 500)


        # Set up the UI
        setup_new_window_ui(self, data)
        apply_mode_styles(self)

        # Center the window using frame_utils
        center_window(self)

def open_new_window(data):
    """
    Opens a new window displaying the provided data.

    :param data: A dictionary with details to display in the new window.
    """
    new_window = NewWindow(data)
    new_window.exec_()
