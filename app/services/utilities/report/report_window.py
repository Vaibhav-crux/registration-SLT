# app/services/mainWindow/report_window.py

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class ReportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Report")
        self.setGeometry(100, 100, 500, 500)  # Set the size of the window

        # Add widgets to the pop-up as needed, here's an example
        layout = QVBoxLayout()
        label = QLabel("This is the report window.", self)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        self.setLayout(layout)