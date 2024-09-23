from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import Qt
from app.ui.utilities.doMaintenance.CreateDo.create_do_maintenance_ui import setup_create_do_ui
from app.utils.mode_utils import apply_mode_styles
from app.controllers.utilities.doMaintenance.save_do_maintenance_controller import save_do_maintenance

class CreateDoMaintenanceWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create DO Maintenance")
        self.setGeometry(200, 200, 400, 450)  # Adjust size for more fields
        self.parent_window = parent

        # Apply dark/light mode styles
        apply_mode_styles(self)

        # Set up UI elements
        (self.do_number_input, self.weighbridge_no_input, self.transporter_input, self.permissido_nameon_input, 
         self.valid_through_input, self.validity_till_input, self.alloted_qty_input, self.released_qty_input, 
         self.left_qty_input, self.do_address_input, self.do_route_input, self.sales_order_input, 
         self.customer_id_input, self.mobile_number_input, self.save_button, self.clear_button) = setup_create_do_ui(self)

        # Connect buttons to methods
        self.save_button.clicked.connect(self.on_save)
        self.clear_button.clicked.connect(self.on_clear)

    def on_save(self):
        # Collect input values
        do_number = self.do_number_input.text()
        weighbridge_no = self.weighbridge_no_input.text()
        transporter = self.transporter_input.text()
        permission_name = self.permissido_nameon_input.text()
        valid_through = self.valid_through_input.text()
        validity_till = self.validity_till_input.text()
        alloted_qty = self.alloted_qty_input.value()
        released_qty = self.released_qty_input.value()
        left_qty = self.left_qty_input.value()
        do_address = self.do_address_input.text()
        do_route = self.do_route_input.text()
        sales_order = self.sales_order_input.text()
        customer_id = self.customer_id_input.text()
        mobile_number = self.mobile_number_input.text()

        # Validate required inputs (example: do_number and transporter)
        if not do_number or not transporter:
            QMessageBox.critical(self, "Input Error", "Both DO Number and Transporter fields are required.")
            return

        # Check if mobile number consists of exactly 10 digits
        if len(mobile_number) != 10 or not mobile_number.isdigit():
            QMessageBox.critical(self, "Input Error", "Mobile Number must consist of exactly 10 digits.")
            return

        # Call the controller to save the data (pass all values)
        success = save_do_maintenance({
            'do_number': do_number,
            'weighbridge_no': weighbridge_no,
            'transporter': transporter,
            'permission_name': permission_name,
            'valid_through': valid_through,
            'validity_till': validity_till,
            'alloted_qty': alloted_qty,
            'released_qty': released_qty,
            'left_qty': left_qty,
            'do_address': do_address,
            'do_route': do_route,
            'sales_order': sales_order,
            'customer_id': customer_id,
            'mobile_number': mobile_number
        }, self)

        # Close the window on success
        if success:
            self.accept()


    def on_clear(self):
        self.do_number_input.clear()
        self.weighbridge_no_input.clear()
        self.transporter_input.clear()
        self.permissido_nameon_input.clear()
        self.valid_through_input.clear()
        self.validity_till_input.clear()
        self.alloted_qty_input.setValue(0.0)  # Reset float fields
        self.released_qty_input.setValue(0.0)
        self.left_qty_input.setValue(0.0)
        self.do_address_input.clear()
        self.do_route_input.clear()
        self.sales_order_input.clear()
        self.customer_id_input.clear()
        self.mobile_number_input.clear()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Close Window', 'Are you sure you want to close this window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            