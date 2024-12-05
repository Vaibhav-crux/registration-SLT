from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtCore import Qt
from app.utils.mode_utils import is_dark_mode
from app.style.default_styles import dark_mode_style, light_mode_style, button_style
from app.utils.cursor.entry_box import MyLineEdit
# Import the frame utility functions
from app.utils.frame_utils import apply_drop_shadow, center_window
from app.controllers.mainWindow.fetch_user_full_name import get_username_from_file

def setup_new_do_ui(window):
    main_layout = QVBoxLayout()
    dark_mode = is_dark_mode()
    common_textbox_style = dark_mode_style if dark_mode else light_mode_style

    def add_field(layout, label_text, widget):
        hbox = QHBoxLayout()
        label = QLabel(label_text, window)
        label.setStyleSheet("""
            font-size: 14px;
            font-weight: 600;  
        """)
        label.setAlignment(Qt.AlignLeft)
        hbox.addWidget(label)
        hbox.addWidget(widget)
        layout.addLayout(hbox)

    user_name_input = MyLineEdit(window)
    user_name_input.setFixedWidth(300)
    user_name_input.setStyleSheet(common_textbox_style)
    user_name_input.setText(get_username_from_file())
    add_field(main_layout, "User Name:", user_name_input)

    password_input = MyLineEdit(window)
    password_input.setFixedWidth(300)
    password_input.setEchoMode(MyLineEdit.Password)
    password_input.setStyleSheet(common_textbox_style)
    add_field(main_layout, "Password:", password_input)

    button_layout = QHBoxLayout()

    confirm_button = QPushButton("Confirm", window)
    confirm_button.setFixedWidth(100)
    confirm_button.setStyleSheet(button_style)
    button_layout.addWidget(confirm_button)

    cancel_button = QPushButton("Cancel", window)
    cancel_button.setFixedWidth(100)
    cancel_button.setStyleSheet(button_style)
    button_layout.addWidget(cancel_button)

    main_layout.addLayout(button_layout)
    window.setLayout(main_layout)

    center_window(window)

    QWidget.setTabOrder(user_name_input, password_input)
    QWidget.setTabOrder(password_input, confirm_button)
    QWidget.setTabOrder(confirm_button, cancel_button)

    return user_name_input, password_input, confirm_button, cancel_button