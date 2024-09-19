# app/ui/mainWindow/main_window_ui.py

from PyQt5.QtWidgets import QLabel, QVBoxLayout, QFrame, QGraphicsDropShadowEffect, QMenu, QAction, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont, QColor
from PyQt5.QtCore import Qt, QPoint
import os
from datetime import datetime
import calendar


class MainWindowUI:
    def setup_ui(self, window):
        window.set_background_image("C:/Users/Vaibhav/Downloads/still-life-ashes-with-charcoal.jpg")
        
        # Create the single frame for displaying time, date, day, and shift information
        window.info_frame = QFrame(window)
        window.info_frame.setStyleSheet("background-color: rgba(0, 51, 102, 150); border-radius: 15px;")
        window.info_frame.setGeometry(window.width() - 380, 100, 350, 360)

        # Fetch the current date and day
        current_date = datetime.now().strftime("%d-%m-%Y")
        current_day = calendar.day_name[datetime.now().weekday()]

        # Create labels for time, date, day, and shift information
        window.time_label = QLabel(datetime.now().strftime("%H:%M:%S"), window.info_frame)
        window.date_label = QLabel(current_date, window.info_frame)
        window.day_label = QLabel(current_day, window.info_frame)
        window.user_label = QLabel("Vaibhav", window.info_frame)
        window.shift_label = QLabel("Shift A", window.info_frame)
        window.id_label = QLabel("2500", window.info_frame)

        # Add shadow effect to labels
        labels = [window.time_label, window.date_label, window.day_label, window.user_label, window.shift_label, window.id_label]
        for label in labels:
            label.setAlignment(Qt.AlignLeft)
            label.setFont(QFont("Roboto", 16, QFont.Bold))
            label.setStyleSheet("color: #d3d3d3; background-color: transparent; padding: 5px;")

            shadow = QGraphicsDropShadowEffect(window)
            shadow.setBlurRadius(10)
            shadow.setXOffset(2)
            shadow.setYOffset(2)
            shadow.setColor(QColor(0, 0, 0, 160))
            label.setGraphicsEffect(shadow)

        # Unified layout for all labels
        vbox = QVBoxLayout(window.info_frame)
        vbox.addWidget(window.time_label)
        vbox.addWidget(window.date_label)
        vbox.addWidget(window.day_label)
        vbox.addSpacing(15)
        vbox.addWidget(window.user_label)
        vbox.addWidget(window.shift_label)
        vbox.addWidget(window.id_label)
        vbox.setSpacing(10)
        vbox.setContentsMargins(20, 20, 20, 20)

        # Create the left-side frame for tools, utilities, and maintenance icons
        window.left_frame = QFrame(window)
        window.left_frame.setGeometry(50, 50, 700, 600)

        vbox_left = QVBoxLayout(window.left_frame)

        # Tools Label and Icons
        tools_label = QLabel("Tools", window)
        tools_label.setFont(QFont("Roboto", 16, QFont.Bold))
        tools_label.setStyleSheet("color: #d3d3d3;")
        vbox_left.addWidget(tools_label)

        tools_layout = QHBoxLayout()
        tools = [("Internal RFID\nRegistration", "C:/Users/Vaibhav/Downloads/Internal RFID.png"),
                 ("External RFID\nRegistration", "C:/Users/Vaibhav/Downloads/External RFID.png")]
        for name, icon in tools:
            window.create_icon_button(name, icon, tools_layout)
        vbox_left.addLayout(tools_layout)

        separator1 = QFrame(window)
        separator1.setFrameShape(QFrame.HLine)
        separator1.setFrameShadow(QFrame.Sunken)
        separator1.setStyleSheet("color: #d3d3d3;")
        vbox_left.addWidget(separator1)

        # Utilities Label and Icons
        utilities_label = QLabel("Utilities", window)
        utilities_label.setFont(QFont("Roboto", 16, QFont.Bold))
        utilities_label.setStyleSheet("color: #d3d3d3;")
        vbox_left.addWidget(utilities_label)

        utilities_layout = QHBoxLayout()
        utilities = [("Report", "C:/Users/Vaibhav/Downloads/chart.png"),
                     ("Shift Timing", "C:/Users/Vaibhav/Downloads/shift.png"),
                     ("Do Maintenance", "C:/Users/Vaibhav/Downloads/monitoring.png")]
        for name, icon in utilities:
            window.create_icon_button(name, icon, utilities_layout)
        vbox_left.addLayout(utilities_layout)

        separator2 = QFrame(window)
        separator2.setFrameShape(QFrame.HLine)
        separator2.setFrameShadow(QFrame.Sunken)
        separator2.setStyleSheet("color: #d3d3d3;")
        vbox_left.addWidget(separator2)

        # Maintenance Label and Icons
        maintenance_label = QLabel("Maintenance", window)
        maintenance_label.setFont(QFont("Roboto", 16, QFont.Bold))
        maintenance_label.setStyleSheet("color: #d3d3d3;")
        vbox_left.addWidget(maintenance_label)

        maintenance_layout = QHBoxLayout()
        maintenance = [("Create User", "C:/Users/Vaibhav/Downloads/add-friend.png"),
                       ("Change Password", "C:/Users/Vaibhav/Downloads/reset-password.png"),
                       ("Block User", "C:/Users/Vaibhav/Downloads/delete-user.png")]
        for name, icon in maintenance:
            window.create_icon_button(name, icon, maintenance_layout)
        vbox_left.addLayout(maintenance_layout)

        # Power button at the top right corner
        window.power_button = QLabel(window)
        window.power_button.setGeometry(window.width() - 60, 20, 40, 40)
        power_icon = QPixmap("C:/Users/Vaibhav/Downloads/switch.png").scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        window.power_button.setPixmap(power_icon)
        window.power_button.setStyleSheet("QLabel { background-color: rgba(255, 0, 0, 0); border-radius: 20px; }")

        # Master button just next to the power button with slight margin
        # window.master_button = QLabel(window)
        # window.master_button.setGeometry(window.width() - 60, 20, 40, 40)  # Slightly to the left of the power button
        # master_icon = QPixmap("C:/Users/Vaibhav/Downloads/scrum.png").scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # window.master_button.setPixmap(master_icon)
        # window.master_button.setStyleSheet("QLabel { background-color: rgba(255, 0, 0, 0); border-radius: 20px; }")

        # Bottom-right image
        window.bottom_right_image = QLabel(window)
        bottom_right_pixmap = QPixmap("C:/Users/Vaibhav/Desktop/Union (2).png")
        window.bottom_right_image.setPixmap(bottom_right_pixmap)
        window.bottom_right_image.setScaledContents(True)

        window.showFullScreen()