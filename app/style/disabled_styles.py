# Styles for disabled (read-only) widgets, focusing only on the border
disabled_style = """
    QLineEdit[readOnly="true"], QComboBox:disabled, QDateEdit[readOnly="true"], QTimeEdit[readOnly="true"] {
        border-bottom: 2px solid red;  /* Red bottom border for read-only state */
    }
"""
