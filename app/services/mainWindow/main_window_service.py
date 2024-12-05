import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction, QLabel, QFrame, QVBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QColor, QFont
from PyQt5.QtCore import Qt, QTimer, QPoint
from app.services.loginWindow.login_window_service import FullScreenWindow
from datetime import datetime
import os
from app.ui.mainWindow.main_window_ui import MainWindowUI  # Import the UI setup class
from app.services.tools.internalRegistration.internal_rfid_window_service import InternalRegistrationWindow
from app.services.tools.externalRegistration.external_registration_window import ExternalRegistrationWindow
from app.services.utilities.report.report_window import ReportWindow
from app.services.utilities.shiftTiming.shift_timing_window import ShiftTimingWindow
from app.services.utilities.doMaintenance.do_maintenance_window import DoMaintenanceWindow
from app.services.maintenance.createUser.create_user_window import CreateUserWindow
from app.services.maintenance.createUser.auth_user_window import AuthUserWindow
from app.services.maintenance.changePassword.change_password_window import ChangePasswordWindow
from app.services.maintenance.blockUser.auth_user_window import ChangePasswordWindowBlock
from app.controllers.mainWindow.fetch_user_full_name import fetch_user_full_name
from app.controllers.mainWindow.fetch_shift_name import fetch_shift_name
from app.controllers.mainWindow.fetch_due_amount import fetch_due_amount

class MainWindow(QWidget, MainWindowUI):
    def __init__(self):
        super().__init__()
        self.full_screen_window = None  # Track the FullScreenWindow instance
        self.is_logged_out = False  # Track logout state
        self.full_name=fetch_user_full_name()
        self.shift_name=fetch_shift_name()
        self.due_amount=fetch_due_amount()
        self.initUI()

    def initUI(self):
        # Fetch the full name for the active username
        # full_name = fetch_user_full_name()

        # Fetch the shift name based on the current time
        # shift_name = fetch_shift_name()

        # Initialize the inactivity timer
        self.inactivity_timer = QTimer(self)
        self.inactivity_timer.timeout.connect(self.handle_logout_or_inactivity)
        self.inactivity_timer.setSingleShot(True)

        # Setup UI and pass the full name and shift name to be displayed
        self.setup_ui(self, self.full_name, self.shift_name,self.due_amount)

        # Start the timer to update the time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Start the inactivity timer
        self.start_inactivity_timer()

        # Ensure the power button has click functionality
        self.power_button.mousePressEvent = self.show_power_menu  # Fix: Ensure this line is present

    def show_power_menu(self, event):
        """Show the power menu with Logout and Exit options."""
        menu = QMenu(self)

        # Apply custom stylesheet to QMenu
        menu.setStyleSheet("""
            QMenu {
                background-color: rgba(30, 30, 30, 230);
                border: 1px solid #3A3A3A;
                padding: 10px;
            }
            QMenu::item {
                padding: 8px 25px;
                background-color: transparent;
                color: white;
            }
            QMenu::item:selected {
                background-color: rgba(50, 50, 50, 150);
            }
        """)

        # Add shadow effect to the menu
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 180))
        menu.setGraphicsEffect(shadow)

        # Create actions for logout and exit
        logout_action = QAction("Logout", self)
        exit_action = QAction("Exit", self)

        # Connect actions to respective methods
        logout_action.triggered.connect(self.logout)
        exit_action.triggered.connect(self.exit_application)

        # Add actions to the menu
        menu.addAction(logout_action)
        menu.addAction(exit_action)

        # Show the menu at the position of the power button
        menu.exec_(self.power_button.mapToGlobal(QPoint(0, self.power_button.height())))

        self.start_inactivity_timer()  # Restart the inactivity timer on menu interaction

    def start_inactivity_timer(self):
        """Start the inactivity timer."""
        if not self.is_logged_out:
            self.inactivity_timer.start(60000000)  # 5 seconds of inactivity triggers the login window

    def stop_inactivity_timer(self):
        """Stop the inactivity timer."""
        self.remaining_time = self.inactivity_timer.remainingTime()
        # print(f"Inactivity timer stoped. {self.remaining_time}")
        self.inactivity_timer.stop()

    def resume_inactivity_timer(self):
        # Resume the inactivity timer from where it left off
        # print("Inactivity timer resumed.")
        self.start_inactivity_timer()

    def logout(self):
        """Handle the logout action."""
        self.is_logged_out = True
        self.stop_inactivity_timer()
        self.handle_logout_or_inactivity()

    def reopen_login_window(self):
        """Handle inactivity timeout."""
        self.is_logged_out = False
        self.handle_logout_or_inactivity()

    def handle_logout_or_inactivity(self):
        """Common functionality for logout and inactivity timeout."""
        if self.full_screen_window is None or not self.full_screen_window.isVisible():
            self.close()  # Close the MainWindow
            self.full_screen_window = FullScreenWindow()  # Open the FullScreenWindow
            
            # Autofill username from the file
            username = self.read_username_from_file()
            if username:
                # Access username_input through the UI instance
                self.full_screen_window.ui.username_input.setText(username)
                self.clear_username_file()  # Clear the file after reading the username

            self.full_screen_window.show()

    def exit_application(self):
        """Handle the exit action."""
        self.stop_inactivity_timer()
        self.clear_username_file()  # Clear the username file on exit
        QApplication.instance().quit()

    def clear_username_file(self):
        """Clear the content of the activeUsername.txt file."""
        with open("app/data/activeUsername.txt", "w") as file:
            file.write("")

    def read_username_from_file(self):
        """Read the content of the activeUsername.txt file."""
        if os.path.exists("activeUsername.txt"):
            with open("activeUsername.txt", "r") as file:
                return file.read().strip()
        return ""

    def resizeEvent(self, event):
        """Handle the window resize event."""
        # Update the background image when the window is resized
        self.set_background_image("app/images/menu/background2.jpg")

        # Resize and reposition the info frame
        self.info_frame.setGeometry(self.width() - 380, 100, 350, 360)

        # Resize and reposition the power button
        self.power_button.setGeometry(self.width() - 60, 20, 40, 40)

        # Reposition the bottom-right image
        image_width = 300
        image_height = 150
        self.bottom_right_image.setGeometry(self.width() - image_width - 20, self.height() - image_height - 20, image_width, image_height)

        self.start_inactivity_timer()  # Restart the inactivity timer on resize

    def set_background_image(self, image_path):
        """Set the background image for the window."""
        # Load the background image
        pixmap = QPixmap(image_path)

        # Scale the image to the window size
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        # Set the background image to the window
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(scaled_pixmap))
        self.setPalette(palette)

        self.start_inactivity_timer()  # Restart the inactivity timer on background update

    def create_icon_button(self, name, icon_path, layout):
        """Create an icon button with a label."""
        frame = QFrame(self)
        frame.setFixedSize(130, 140)
        frame.setStyleSheet("""
            QFrame { 
                background-color: rgba(0, 0, 0, 0); 
                border-radius: 15px; 
            }
            QFrame:hover {
                background-color: rgba(0, 0, 0, 100);
            }
        """)

        icon_label = QLabel(frame)
        icon = QPixmap(icon_path).scaled(60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(icon)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("QLabel { padding: 5px; background-color: rgba(255, 255, 255, 0); border-radius: 15px; }")

        text_label = QLabel(name, frame)
        text_label.setAlignment(Qt.AlignCenter)
        text_label.setWordWrap(True)
        text_label.setFont(QFont("Roboto", 11, QFont.DemiBold))
        text_label.setStyleSheet("color: #d3d3d3; background-color: transparent;")

        vbox = QVBoxLayout(frame)
        vbox.addWidget(icon_label)
        vbox.addWidget(text_label)
        layout.addWidget(frame)

        # Specific handling for "Internal RFID Registration" button click
        if name == "Internal RFID\nRegistration":
            frame.mousePressEvent = lambda event: self.open_registration_window()
        elif name == "External RFID\nRegistration":
            frame.mousePressEvent = lambda event: self.open_external_registration_window()
        elif name == "Report":
            frame.mousePressEvent = lambda event: self.open_report_window()
        elif name == "Shift Timing":
            frame.mousePressEvent = lambda event: self.open_shift_timing_window()
        elif name == "Do Maintenance":
            frame.mousePressEvent = lambda event: self.open_do_maintenance_window()
        elif name == "Create User":
            frame.mousePressEvent = lambda event: self.open_create_user_window()
        elif name == "Change Password":
            frame.mousePressEvent = lambda event: self.open_change_password_window()
        elif name == "Block User":
            frame.mousePressEvent = lambda event: self.open_block_user_window()
        else:
            # Restart inactivity timer whenever an icon is interacted with
            frame.mousePressEvent = lambda event: self.start_inactivity_timer()

    def open_registration_window(self):
        """Open the internal registration pop-up window."""
        self.stop_inactivity_timer()
        self.registration_window = InternalRegistrationWindow()
        self.registration_window.finished.connect(self.resume_inactivity_timer)
        self.registration_window.show()

    def open_external_registration_window(self):
        """Open the external registration pop-up window."""
        self.stop_inactivity_timer()
        self.external_registration_window = ExternalRegistrationWindow()
        self.external_registration_window.finished.connect(self.resume_inactivity_timer)
        self.external_registration_window.show()
    
    def open_report_window(self):
        """Open the external registration pop-up window."""
        self.stop_inactivity_timer()
        self.report_window = ReportWindow(self)
        self.report_window.show()
    
    def open_shift_timing_window(self):
        """Open the external registration pop-up window."""
        self.stop_inactivity_timer()
        self.shift_timing_window = ShiftTimingWindow()
        self.shift_timing_window.finished.connect(self.resume_inactivity_timer)
        self.shift_timing_window.show()
    
    def open_do_maintenance_window(self):
        """Open the external registration pop-up window."""
        self.stop_inactivity_timer()
        self.do_maintenance_window = DoMaintenanceWindow()
        self.do_maintenance_window.finished.connect(self.resume_inactivity_timer)
        self.do_maintenance_window.show()

    def open_create_user_window (self):
        """Open the external registration pop-up window."""
        self.stop_inactivity_timer()
        self.create_user_window = AuthUserWindow()
        self.create_user_window.finished.connect(self.resume_inactivity_timer)
        self.create_user_window.show()  

    def open_change_password_window (self):
        """Open the external registration pop-up window."""
        self.stop_inactivity_timer()
        self.change_password_window = ChangePasswordWindow()
        self.change_password_window.finished.connect(self.resume_inactivity_timer)
        self.change_password_window.show()

    def open_block_user_window (self):
        """Open the external registration pop-up window."""
        self.stop_inactivity_timer()
        self.change_password_window = ChangePasswordWindowBlock()
        self.change_password_window.finished.connect(self.resume_inactivity_timer)
        self.change_password_window.show()

    def update_time(self):
        """Update the time label with the current time."""
        self.time_label.setText(datetime.now().strftime("%H:%M:%S"))
        shift_name=fetch_shift_name()
        self.shift_label.setText(shift_name)
        due=fetch_due_amount()
        self.id_label.setText(due)

    def mousePressEvent(self, event):
        """Handle mouse press events."""
        super().mousePressEvent(event)
        self.start_inactivity_timer()  # Restart the inactivity timer on mouse press

    def keyPressEvent(self, event):
        """Handle key press events."""
        super().keyPressEvent(event)
        self.start_inactivity_timer()  # Restart the inactivity timer on key press

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
