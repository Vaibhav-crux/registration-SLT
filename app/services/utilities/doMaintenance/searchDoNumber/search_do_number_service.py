from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel  
from app.models.doMaintenance import DoData
from PyQt5.QtCore import Qt
from app.ui.utilities.doMaintenance.searchDoNumber.search_do_number_ui import show_result_ui
from app.utils.frame_utils import apply_drop_shadow, center_window
from app.controllers.utilities.doMaintenance.fetch_do_details_controller import fetch_do_details

class SearchDoNumberService(QDialog):  
    def __init__(self, result):
        super().__init__()  
        self.setWindowTitle("DO Number Details")

        # Set the width and height of the window
        self.setGeometry(100, 100, 600, 600)  

        # Disable the help button in the taskbar
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # Center the window on the screen
        center_window(self)  

        # Optionally, apply a drop shadow effect
        apply_drop_shadow(self)  

        # Call the show_result_ui to set up the UI with the result
        show_result_ui(result, self)

    @staticmethod
    def search_do_number(do_number: str):
        """
        Searches for the given DO Number in the database.

        :param do_number: The DO Number to search for.
        :return: The formatted result string if found, None otherwise.
        """
        return fetch_do_details(do_number)