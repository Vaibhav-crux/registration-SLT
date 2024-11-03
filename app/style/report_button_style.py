# app/style/report_button_style.py

# Default button style
button_style = """
    QPushButton {
        background-color: transparent;  /* No background color */
        border: none;  /* No borders */
        font-size: 18px;  /* Font size */
        padding: 8px;  /* Padding for better click area */
        margin: 2px;  /* Margin between buttons */
        border-radius: 5px;  /* Rounded corners */
    }
    QPushButton:hover {
        background-color: #007bff;  /* Professional blue on hover */
        border-radius: 10px;  /* More rounded corners on hover */
    }
    QPushButton:pressed {
        background-color: #0056b3;  /* Darker blue when pressed */
        border-radius: 10px;  /* Keep rounded corners when pressed */
    }
"""

# Clicked button style (dark grey color with rounded corners)
clicked_button_style = """
    QPushButton {
        background-color: #4A4A4A;  /* Dark grey color */
        color: white;
        font-size: 18px;
        padding: 8px;
        margin: 2px;
        border: none;
        border-radius: 10px;  /* Rounded corners for selected state */
    }
"""

# Apply styles for professional blue background, curved corners, and 14px font
button_styles = """
    QPushButton {
        background-color: #007bff;  /* Professional blue */
        color: white;               /* Text color */
        border-radius: 8px;         /* Curved corners */
        font-size: 14px;            /* Font size */
        padding: 8px 16px;          /* Padding for a more substantial button appearance */
    }
    QPushButton:hover {
        background-color: #0056b3;  /* Darker blue on hover */
    }
    QPushButton:pressed {
        background-color: #003f7f;  /* Even darker blue when pressed */
    }
"""