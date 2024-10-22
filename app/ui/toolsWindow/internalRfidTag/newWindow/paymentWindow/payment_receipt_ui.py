# app/ui/toolsWindow/internalRfidTag/newWindow/paymentWindow/payment_receipt_ui.py

import os
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

def setup_payment_receipt_ui(dialog, html_file_path):
    layout = QVBoxLayout()

    # Convert relative path to absolute path
    absolute_html_file_path = os.path.abspath(html_file_path)
    print("Absolute HTML File Path:", absolute_html_file_path)  # Debug output

    # Create a frame to hold the HTML content
    html_frame = QFrame(dialog)
    html_frame_layout = QVBoxLayout(html_frame)

    # Create a web view to display the HTML content
    web_view = QWebEngineView(html_frame)
    
    # Set the absolute file path in the URL
    web_view.setUrl(QUrl.fromLocalFile(absolute_html_file_path))
    html_frame_layout.addWidget(web_view)

    layout.addWidget(html_frame)

    # Create button layout
    button_layout = QHBoxLayout()

    # Confirm button
    confirm_button = QPushButton("Confirm", dialog)
    confirm_button.setFixedWidth(100)
    confirm_button.clicked.connect(dialog.accept)  # Close dialog with accept
    button_layout.addWidget(confirm_button)

    # Cancel button
    cancel_button = QPushButton("Cancel", dialog)
    cancel_button.setFixedWidth(100)
    cancel_button.clicked.connect(dialog.reject)  # Close dialog with reject
    button_layout.addWidget(cancel_button)

    layout.addLayout(button_layout)

    dialog.setLayout(layout)
