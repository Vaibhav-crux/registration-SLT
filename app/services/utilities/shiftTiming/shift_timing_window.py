from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QTime
from datetime import datetime, timedelta
# Import the mode utility functions
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window
# Import the UI setup function
from app.ui.utilities.shiftTiming.shift_timing_ui import setup_ui
# Import the controllers for fetching and updating shift timings
from app.controllers.utilities.shiftTiming.fetch_shift_timing import get_shift_timings
from app.controllers.utilities.shiftTiming.insert_shift_timing import update_shift_timing

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

        # Set up the UI using the external setup function, passing the necessary controllers
        self.shift_rows = []
        setup_ui(self, get_shift_timings, self.shift_rows)

    def time_difference_is_valid(self, from_time_str, to_time_str):
        """
        Check if the difference between from_time and to_time is exactly 8 hours.

        :param from_time_str: Time string of format "HH:mm:ss" (e.g., "06:00:00")
        :param to_time_str: Time string of format "HH:mm:ss" (e.g., "13:59:59")
        :return: True if the difference is exactly 8 hours, False otherwise.
        """
        # Convert the time strings to datetime objects
        from_time = datetime.strptime(from_time_str, "%H:%M:%S")
        to_time = datetime.strptime(to_time_str, "%H:%M:%S")

        # Calculate the difference in hours between from and to time
        if to_time < from_time:
            to_time += timedelta(days=1)  # Handle cases where to_time is on the next day (e.g., night shift)

        time_diff = to_time - from_time
        return time_diff == timedelta(hours=8)

    def on_confirm_click(self):
        """
        Handles the logic for confirming shift time updates and interacts with the database.
        """
        for shift_name, from_time_edit, to_time_edit in self.shift_rows:
            from_time = from_time_edit.time().toString("HH:mm:ss")
            to_time = to_time_edit.time().toString("HH:mm:ss")

            # Validate that the time difference between from_time and to_time is 8 hours
            if not self.time_difference_is_valid(from_time, to_time):
                QMessageBox.critical(self, "Invalid Time Difference","The time difference for shifts must be exactly 8 hours.")
                return

            # Update the database with the new values if the validation passes
            success = update_shift_timing(shift_name, from_time, to_time)

            if not success:
                QMessageBox.critical(self, "Error", f"Failed to update {shift_name}. Please try again.")
                return

        # Show success message
        QMessageBox.information(self, "Success", "Shift timings updated successfully!")
