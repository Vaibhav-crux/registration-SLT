from PyQt5.QtWidgets import QVBoxLayout, QLabel, QScrollArea, QWidget, QHBoxLayout
from PyQt5.QtGui import QFont
from app.utils.mode_utils import apply_mode_styles  # Import the mode utility function

def show_result_ui(result, parent):
    """
    Sets up the result window UI to display the search results.

    :param result: The formatted result string.
    :param parent: The parent widget (result window).
    """
    # Apply the correct mode styles to the parent window
    apply_mode_styles(parent)

    layout = QVBoxLayout()
    parent.setLayout(layout)

    scroll_area = QScrollArea()
    layout.addWidget(scroll_area)

    content_widget = QWidget()
    scroll_area.setWidget(content_widget)
    scroll_area.setWidgetResizable(True)

    content_layout = QVBoxLayout()
    content_widget.setLayout(content_layout)

    lines = result.split('\n')
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key_label = QLabel(key.strip())
            value_label = QLabel(value.strip())

            key_font = QFont()
            key_font.setBold(True)
            key_font.setPointSize(12)
            key_label.setFont(key_font)

            value_font = QFont()
            value_font.setPointSize(12)
            value_label.setFont(value_font)

            hbox = QHBoxLayout()
            hbox.addWidget(key_label)
            hbox.addWidget(value_label)
            content_layout.addLayout(hbox)
        else:
            label = QLabel(line.strip())
            font = QFont()
            font.setPointSize(12)
            label.setFont(font)
            content_layout.addWidget(label)
