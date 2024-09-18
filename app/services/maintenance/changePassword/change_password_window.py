# app/services/mainWindow/report_window.py

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class ChangePasswordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Change Password")
        self.setGeometry(100, 100, 500, 500)  # Set the size of the window

        # Add widgets to the pop-up as needed, here's an example
        layout = QVBoxLayout()
        label = QLabel("This is the change password window.", self)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        self.setLayout(layout)
