# app/services/tools/internalRegistration/internal_rfid_window_service.py

from PyQt5.QtWidgets import QDialog, QLineEdit, QComboBox, QDateEdit
from PyQt5.QtCore import Qt

# Import the mode utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window
# Import the UI setup function
from app.ui.toolsWindow.internalRfidTag.internal_rfid_ui import setup_ui
# Import the new function
from app.services.tools.internalRegistration.next_entry_box_cursor_services import focus_next_enabled_widget

class InternalRegistrationWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration")
        self.setGeometry(100, 100, 400, 500)

        # Apply window flags to remove the "?" and only show the close button
        apply_window_flags(self)

        # Apply the dark or light mode styles
        apply_mode_styles(self)

        # Center the window using frame_utils
        center_window(self)

        # Apply drop shadow using frame_utils
        apply_drop_shadow(self)

        # Set up the UI using the external setup function
        setup_ui(self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # Use the imported function to focus the next enabled widget
            focus_next_enabled_widget(self.focusWidget(), self)
        else:
            super().keyPressEvent(event)
