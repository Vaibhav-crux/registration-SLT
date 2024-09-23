# Styles for widgets in dark and light modes

# Textbox, ComboBox, QDateEdit, and QTimeEdit styles
dark_mode_style = """
    QLineEdit, QComboBox, QDateEdit, QTimeEdit, QDoubleSpinBox {
        border-top: none;
        border-left: none;
        border-right: none;
        border-bottom: 2px solid #007bff;  /* Professional blue bottom border */
        background-color: #505050;  /* Professional grey for dark mode */
        padding: 2px;
        border-radius: 4px;
        color: white;
        font-size: 14px;  /* Same size as label */
    }
    QComboBox::drop-down, QDateEdit::drop-down, QTimeEdit::drop-down {
        border: none;  /* No borders around the drop-down button */
    }
    QComboBox::down-arrow, QDateEdit::down-arrow, QTimeEdit::down-arrow {
        image: url(app/images/processed/down-arrow.png);  /* Set downward arrow image */
        width: 10px;
        height: 10px;
    }
    QDateEdit::up-arrow, QTimeEdit::up-arrow {
        image: url(app/images/processed/up-arrow.png);  /* Set upward arrow image */
        width: 10px;
        height: 10px;
    }
    QComboBox QAbstractItemView, QDateEdit QAbstractItemView, QTimeEdit QAbstractItemView {
        background-color: #505050;
        color: white;
    }
"""

light_mode_style = """
    QLineEdit, QComboBox, QDateEdit, QTimeEdit, QDoubleSpinBox {
        border-top: none;
        border-left: none;
        border-right: none;
        border-bottom: 2px solid #007bff;  /* Professional blue bottom border */
        background-color: #C0C0C0;  /* Silver color for light mode */
        padding: 2px;
        border-radius: 4px;
        color: black;
        font-size: 14px;  /* Same size as label */
    }
    QComboBox::drop-down, QDateEdit::drop-down, QTimeEdit::drop-down {
        border: none;  /* No borders around the drop-down button */
    }
    QComboBox::down-arrow, QDateEdit::down-arrow, QTimeEdit::down-arrow {
        image: url(app/images/processed/down-arrow.png);  /* Set downward arrow image */
        width: 10px;
        height: 10px;
    }
    QDateEdit::up-arrow, QTimeEdit::up-arrow {
        image: url(app/images/processed/up-arrow.png);  /* Set upward arrow image */
        width: 10px;
        height: 10px;
    }
    QComboBox QAbstractItemView, QDateEdit QAbstractItemView, QTimeEdit QAbstractItemView {
        background-color: #C0C0C0;
        color: black;
    }
"""

# Button style
button_style = """
    QPushButton {
        background-color: #007bff;  /* Professional blue background */
        color: white;
        border-radius: 8px;  /* Curved corners */
        font-size: 14px;  /* Increase text size */
        font-weight: bold;  /* Bold text */
        padding: 8px 16px;  /* Increase padding to make button larger */
    }
    QPushButton:pressed {
        background-color: #0056b3;  /* Darker blue when pressed */
    }
"""
