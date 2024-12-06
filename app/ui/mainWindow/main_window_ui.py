# app/ui/mainWindow/main_window_ui.py

from PyQt5.QtWidgets import QLabel, QVBoxLayout, QFrame, QGraphicsDropShadowEffect, QMenu, QAction, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont, QColor
from PyQt5.QtCore import Qt, QPoint
import os
from datetime import datetime
import calendar
import pytz


class MainWindowUI:
    def setup_ui(self, window, full_name, shift_name,due_amount):
        window.set_background_image("app/images/menu/background2.jpg")
        
        # Create the single frame for displaying time, date, day, and shift information
        window.info_frame = QFrame(window)
        window.info_frame.setStyleSheet("background-color: rgba(0, 51, 102, 150); border-radius: 15px;")
        window.info_frame.setGeometry(window.width() - 380, 100, 350, 360)

        # Fetch the current date and day
        timezone = pytz.timezone("Asia/Kolkata")
        current_date = datetime.now(timezone).strftime("%d-%m-%Y")
        current_day = calendar.day_name[datetime.now(timezone).weekday()]

        # Create labels for time, date, day, and shift information
        window.time_label = QLabel(datetime.now(timezone).strftime("%H:%M:%S"), window.info_frame)
        window.date_label = QLabel(current_date, window.info_frame)
        window.day_label = QLabel(current_day, window.info_frame)
        window.user_label = QLabel(full_name, window.info_frame)  # Display the full name passed from the controller
        window.shift_label = QLabel(shift_name, window.info_frame)  # Display the shift name passed from the controller
        window.id_label = QLabel(due_amount, window.info_frame)

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
        tools = [("Internal RFID\nRegistration", "app/images/menu/Internal RFID.png"),
                 ("External RFID\nRegistration", "app/images/menu/External RFID.png")]
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
        utilities = [("Report", "app/images/menu/chart.png"),
                     ("Shift Timing", "app/images/menu/shift.png"),
                     ("Do Maintenance", "app/images/menu/monitoring.png")]
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
        maintenance = [("Create User", "app/images/menu/add-friend.png"),
                       ("Change Password", "app/images/menu/reset-password.png"),
                       ("Block User", "app/images/menu/delete-user.png")]
        for name, icon in maintenance:
            window.create_icon_button(name, icon, maintenance_layout)
        vbox_left.addLayout(maintenance_layout)

        # Power button at the top right corner
        window.power_button = QLabel(window)
        window.power_button.setGeometry(window.width() - 60, 20, 40, 40)
        power_icon = QPixmap("app/images/processed/switch.png").scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
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
        bottom_right_pixmap = QPixmap("app/images/processed/logo.png").scaled(350, 360, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        window.bottom_right_image.setPixmap(bottom_right_pixmap)
        window.bottom_right_image.setAlignment(Qt.AlignCenter)

        # Set the geometry of the image to place it at the bottom-right corner with the correct size
        window.bottom_right_image.setGeometry(window.width() - 380, window.height() - 360 - 20, 350, 360)

        # Add a background and a border to make it stand out
        window.bottom_right_image.setStyleSheet("""
            QLabel {
                background-color: rgba(255, 255, 255, 50);  /* Light translucent background */
                border-radius: 15px;
            }
        """)

        window.showFullScreen()