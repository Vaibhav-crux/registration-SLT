from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from app.utils.cursor.entry_box import MyLineEdit
from app.utils.mode_utils import is_dark_mode
from app.style.default_styles import dark_mode_style, light_mode_style, button_style
from app.controllers.mainWindow.fetch_user_full_name import get_username_from_file

def setup_ui(window):
    """
    Set up the UI layout for the ChangePasswordWindow with additional fields and buttons.
    
    :param window: The QDialog window to set up the UI on.
    """
    # Create the main layout
    main_layout = QVBoxLayout()

    # Check if the current mode is dark or light
    dark_mode = is_dark_mode()
    
    # Apply the appropriate stylesheet
    common_textbox_style = dark_mode_style if dark_mode else light_mode_style

    # Helper function to create a label and field (textbox) in a horizontal layout
    def add_field(layout, label_text, widget):
        hbox = QHBoxLayout()
        label = QLabel(label_text, window)
        label.setStyleSheet("""
          font-size: 14px;
          font-weight: 600; /* Semi-bold */
        """)
        label.setAlignment(Qt.AlignLeft)
        hbox.addWidget(label)
        hbox.addWidget(widget)
        layout.addLayout(hbox)

    # User Name Field
    user_name = MyLineEdit(window)
    user_name.setFixedWidth(300)
    user_name.setStyleSheet(common_textbox_style)
    user_name.setObjectName("user_name")  # Set object name for later retrieval
    user_name.setText(get_username_from_file())
    add_field(main_layout, "User Name:", user_name)

    # Password Field (with hidden characters)
    password = MyLineEdit(window)
    password.setFixedWidth(300)
    password.setEchoMode(MyLineEdit.Password)
    password.setStyleSheet(common_textbox_style)
    password.setObjectName("password")  # Set object name for later retrieval
    add_field(main_layout, "Password:", password)

    # Create buttons
    button_layout = QHBoxLayout()

    # Confirm Button
    confirm_button = QPushButton("Confirm", window)
    confirm_button.setFixedWidth(100)
    confirm_button.setStyleSheet(button_style)
    confirm_button.setObjectName("Confirm")  # Set object name for later retrieval
    button_layout.addWidget(confirm_button)

    # Cancel Button
    cancel_button = QPushButton("Cancel", window)
    cancel_button.setFixedWidth(100)
    cancel_button.setStyleSheet(button_style)
    cancel_button.setObjectName("Cancel")  # Set object name for later retrieval
    button_layout.addWidget(cancel_button)

    # Add button layout to main layout
    main_layout.addLayout(button_layout)

    # Set the main layout
    window.setLayout(main_layout)
