from PyQt5.QtWidgets import QDialog
# Import the mode utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window
# Import the UI setup function
from app.ui.utilities.shiftTiming.shift_timing_ui import setup_ui

class ShiftTimingWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shift Timing")
        
        # Adjust the width and height of the window
        self.setGeometry(100, 100, 500, 250)  # Increase width, decrease height

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
