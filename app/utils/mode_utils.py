# app/utils/mode_utils.py

def apply_dark_mode(widget):
    """
    Applies a dark mode stylesheet to the given widget.

    :param widget: The widget to apply the dark mode to.
    """
    dark_mode_stylesheet = """
        QWidget {
            background-color: #2E2E2E;  /* Dark background */
            color: #FFFFFF;  /* Light text */
        }
        QFrame {
            background-color: rgba(46, 46, 46, 240);  /* Semi-transparent dark background for frames */
            border-radius: 15px;  /* Rounded corners for frames */
        }
        QLabel {
            color: #FFFFFF;  /* White text for labels */
            font-size: 24px;  /* Font size for labels */
            padding-top: 10px;  /* Padding for labels */
        }
    """
    # Apply the dark mode stylesheet to the widget
    widget.setStyleSheet(dark_mode_stylesheet)
