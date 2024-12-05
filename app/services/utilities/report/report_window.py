from PyQt5.QtWidgets import QWidget, QLineEdit, QComboBox, QDateEdit, QTimeEdit, QDoubleSpinBox, QLabel, QFrame, QPushButton
from app.ui.utilities.report.main_window_ui import setup_main_window_ui
from app.utils.mode_utils import apply_mode_styles, apply_window_flags, is_dark_mode
from app.utils.frame_utils import center_window
from app.style.default_styles import dark_mode_style, light_mode_style
from app.style.report_button_style import button_style, clicked_button_style  # Import both styles

class ReportWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)  # Set the size of the window

        # Set up the UI using the external setup function
        setup_main_window_ui(self)

        # Apply overall window styles and flags
        apply_mode_styles(self)
        apply_window_flags(self)
        center_window(self)

        # Apply specific styles to widgets
        self.apply_specific_styles()

        # Apply specific styles to buttons
        self.apply_button_styles()

        # Set the frame color based on the mode
        self.set_frame_color()


    def apply_specific_styles(self):
        # Determine which style to use based on current mode
        specific_stylesheet = dark_mode_style if is_dark_mode() else light_mode_style

        # Apply stylesheet only to specific input widgets, ensuring the overall mode is not affected
        for widget in self.findChildren((QLineEdit, QComboBox, QDateEdit, QTimeEdit, QDoubleSpinBox, QLabel)):
            widget.setStyleSheet(specific_stylesheet)

    def apply_button_styles(self):
        # Apply the button style to all buttons in frame1
        frame1 = self.findChild(QFrame)  # Assuming frame1 is the first frame in the layout
        if frame1:
            for button in frame1.findChildren(QPushButton):
                button.setStyleSheet(button_style)
                button.clicked.connect(lambda _, b=button: self.handle_button_click(b))

    def handle_button_click(self, clicked_button):
        """
        Handle the button click event to apply the dark grey color to the clicked button.
        """
        frame1 = self.findChild(QFrame)
        if frame1:
            for button in frame1.findChildren(QPushButton):
                # Reset style to default button style
                button.setStyleSheet(button_style)

        # Apply dark grey color to the clicked button
        clicked_button.setStyleSheet(clicked_button_style)

    def set_frame_color(self):
        # Set the frame color based on the current mode
        if is_dark_mode():
            self.findChild(QFrame).setStyleSheet("background-color: #5D76A9;")  # Dark gray for dark mode
        else:
            self.findChild(QFrame).setStyleSheet("background-color: #f0f0f0;")  # Light gray for light mode

    def closeEvent(self, event):
        """Override closeEvent to resume the inactivity timer."""
        # Call the parent method to close the window properly
        super().closeEvent(event)

        # Resume the inactivity timer when the window is closed
        self.parent().resume_inactivity_timer()
