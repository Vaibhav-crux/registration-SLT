from PyQt5.QtWidgets import QDialog
# Import the mode utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window
# Import the UI setup function
from app.ui.utilities.doMaintenance.do_maintenance_ui import setup_ui
# Import the new window for creating DO number
from app.services.utilities.doMaintenance.CreateDoNumber.new_do_maintenance_service import NewDoMaintenanceWindow

class DoMaintenanceWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DO Maintenance")
        self.setGeometry(100, 100, 400, 200)  # Adjusted geometry for clarity

        # Apply window flags to remove the "?" and only show the close button
        apply_window_flags(self)

        # Apply the dark or light mode styles
        apply_mode_styles(self)

        # Center the window using frame_utils
        center_window(self)

        # Apply drop shadow using frame_utils
        apply_drop_shadow(self)

        # Set up the UI using the external setup function, and retrieve the buttons
        self.new_button, self.edit_button, self.delete_button, self.search_button = setup_ui(self)

        # Connect the "New" button to open the new DO window
        self.new_button.clicked.connect(self.open_new_do_window)

    def open_new_do_window(self):
        """
        Opens the New DO Maintenance window when the "New" button is clicked.
        Pass self as the parent to apply the blur effect to this window.
        """
        new_do_window = NewDoMaintenanceWindow(self)
        new_do_window.exec_()  # Open the window as a modal dialog
