import os
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from app.utils.mode_utils import is_dark_mode
from app.style.default_styles import dark_mode_style, light_mode_style, button_style

def setup_payment_receipt_ui(dialog, html_file_path, parent_window):
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

    # Print button (placeholder functionality)
    print_button = QPushButton("Print", dialog)
    print_button.setFixedWidth(100)
    print_button.clicked.connect(lambda: print_receipt(dialog))  # Placeholder function for printing

    # Save button (placeholder functionality)
    save_button = QPushButton("Save", dialog)
    save_button.setFixedWidth(100)
    save_button.clicked.connect(lambda: save_receipt(dialog))  # Placeholder function for saving

    # Cancel button
    cancel_button = QPushButton("Cancel", dialog)
    cancel_button.setFixedWidth(100)
    cancel_button.clicked.connect(lambda: cancel_and_delete(dialog, parent_window, absolute_html_file_path))  # Close dialog and parent window, delete file

    # Apply button styles
    print_button.setStyleSheet(button_style)
    save_button.setStyleSheet(button_style)
    cancel_button.setStyleSheet(button_style)

    button_layout.addWidget(print_button)
    button_layout.addWidget(save_button)
    button_layout.addWidget(cancel_button)

    layout.addLayout(button_layout)

    # Apply mode-specific styles
    if is_dark_mode():
        dialog.setStyleSheet(dark_mode_style)
    else:
        dialog.setStyleSheet(light_mode_style)

    dialog.setLayout(layout)

def print_receipt(dialog):
    """
    Placeholder function to handle printing logic.
    Currently just closes the dialog.
    """
    print("Print functionality is not implemented yet.")
    dialog.reject()  # Close the dialog

def save_receipt(dialog):
    """
    Placeholder function to handle saving logic.
    Currently just closes the dialog.
    """
    print("Save functionality is not implemented yet.")
    dialog.reject()  # Close the dialog

def cancel_and_delete(dialog, parent_window, html_file_path):
    """
    Close the dialog, the parent window, and delete the HTML file.
    """
    # Check if the file exists and delete it
    if os.path.exists(html_file_path):
        try:
            os.remove(html_file_path)
            print(f"Deleted HTML file: {html_file_path}")
        except Exception as e:
            print(f"Error deleting HTML file: {e}")

    # Close both the dialog and the parent window
    dialog.reject()  # Close the current dialog
    parent_window.close()  # Close the parent window (open_new_window_ui)
