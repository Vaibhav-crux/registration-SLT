from PyQt5.QtWidgets import QDialog, QMessageBox
from app.utils.mode_utils import apply_mode_styles, apply_window_flags
from app.utils.frame_utils import apply_drop_shadow, center_window
from app.ui.utilities.doMaintenance.do_maintenance_ui import setup_ui
from app.services.utilities.doMaintenance.CreateDoNumber.auth_do_maintenance_service import AuthDoMaintenanceWindow
from app.services.utilities.doMaintenance.searchDoNumber.search_do_number_service import SearchDoNumberService
from app.ui.utilities.doMaintenance.searchDoNumber.search_do_number_ui import show_result_ui
from app.ui.utilities.doMaintenance.deleteDoNumber.delete_do_number_ui import DeleteDoNumberWindow
from app.services.utilities.doMaintenance.deleteDoNumber.delete_do_number_service import DeleteDoNumberService
from app.controllers.utilities.doMaintenance.fetch_do_details_controller import fetch_do_details

class DoMaintenanceWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DO Maintenance")
        self.setGeometry(100, 100, 400, 200)

        # Apply window flags, mode styles, center the window, and add drop shadow
        apply_window_flags(self)
        apply_mode_styles(self)
        center_window(self)
        apply_drop_shadow(self)

        # Set up the UI using the external setup function, and retrieve the buttons
        self.new_button, self.edit_button, self.delete_button, self.search_button = setup_ui(self)

        # Connect the buttons to their actions
        self.new_button.clicked.connect(self.open_new_do_window)
        self.search_button.clicked.connect(self.perform_search)
        self.delete_button.clicked.connect(self.open_delete_do_window)

        # Set focus to the Do Number text box
        self.do_number_input.setFocus()

    def open_new_do_window(self):
        new_do_window = AuthDoMaintenanceWindow(self)
        new_do_window.exec_()  # Open the window as a modal dialog

    def perform_search(self):
        do_number = self.do_number_input.text()

        if not do_number:
            self.show_message("Please enter a DO Number.")
            return

        # Perform the search using the SearchDoNumberService
        result = SearchDoNumberService.search_do_number(do_number)

        if result:
            # Show the result in a new window
            self.show_result(result)
        else:
            self.show_message(f"No record found for DO Number: {do_number}")

        # Set focus back to the Do Number textbox
        self.do_number_input.setFocus()

    def open_delete_do_window(self):
        do_number = self.do_number_input.text()

        if not do_number:
            self.show_message("Please enter a DO Number.")
            return

        # Check if the DO Number exists
        do_details = fetch_do_details(do_number)
        if not do_details:
            self.show_message(f"No record found for DO Number: {do_number}")
            return

        delete_window = DeleteDoNumberWindow(do_number, self)
        delete_window.exec_()

    def show_message(self, message):
        QMessageBox.information(self, "Information", message)

    def show_result(self, result):
        # Displays the search result in a new ResultWindow.
        result_window = SearchDoNumberService(result)
        result_window.exec_()

        # Set focus back to the Do Number textbox
        self.do_number_input.setFocus()