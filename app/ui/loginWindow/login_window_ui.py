from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFrame, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from app.utils.frame_utils import apply_drop_shadow

class LoginWindowUI:
    def __init__(self, parent):
        self.parent = parent
        self.frame = None
        self.username_input = None
        self.login_prompt = None

    def setup_ui(self):
        # Create the floating card
        self.create_floating_card()

    def create_floating_card(self):
        # Create a frame that will act as the floating card
        self.frame = QFrame(self.parent)
        self.frame.setFixedSize(500, 350)
        self.frame.setStyleSheet("""
            QFrame {
                background-color: #333333;
                border-radius: 15px;
            }
        """)
        apply_drop_shadow(self.frame)

        # Center the frame in the window and shift slightly to the right
        self.reposition_frame()

        # Create a layout for the frame
        layout = QVBoxLayout()

        # Power button at the top-right corner
        power_button_layout = QHBoxLayout()
        self.power_button = QLabel(self.frame)
        power_icon = QPixmap("app/images/processed/switch.png").scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.power_button.setPixmap(power_icon)
        self.power_button.setStyleSheet("QLabel { background-color: rgba(255, 0, 0, 0); }")
        self.power_button.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.power_button.mousePressEvent = self.parent.close_window
        power_button_layout.addStretch()
        power_button_layout.addWidget(self.power_button)
        layout.addLayout(power_button_layout)

        # Header and input section
        self.add_header(layout)
        self.add_sign_in_section(layout)

        # Set layout to the frame
        self.frame.setLayout(layout)

    def add_header(self, layout):
        # Add a separator (this is optional, you can remove or adjust if needed)
        separator = QFrame(self.frame)
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #d3d3d3;")
        layout.addWidget(separator)

        # Reduce the spacing above the logo
        layout.addSpacing(5)  # Reduced from 15 to 5

        # Load the logo image and add it as a QLabel
        self.logo = QLabel(self.frame)
        logo_pixmap = QPixmap("app/images/processed/logo.png").scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo.setPixmap(logo_pixmap)
        self.logo.setAlignment(Qt.AlignCenter)

        # Add the logo to the layout
        layout.addWidget(self.logo)

        # Reduce the spacing below the logo
        layout.addSpacing(10)  # Reduced from 20 to 10


    def add_sign_in_section(self, layout):
        sign_in_layout = QHBoxLayout()
        self.login_prompt = QLabel("Sign In")
        self.login_prompt.setFont(QFont("Sans-serif", 14, QFont.Bold))
        self.login_prompt.setStyleSheet("color: #E0E0E0;")
        sign_in_layout.addSpacing(50)
        sign_in_layout.addWidget(self.login_prompt, alignment=Qt.AlignLeft)
        sign_in_layout.addStretch()
        layout.addLayout(sign_in_layout)
        layout.addSpacing(0)

        input_layout = QHBoxLayout()
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setFixedWidth(280)
        self.username_input.setFixedHeight(40)
        self.username_input.setStyleSheet("""
            padding: 10px;
            border-radius: 0px;
            border: none;
            border-bottom: 2px solid #007BFF;
            background-color: #444444;
            color: #E0E0E0;
            font-weight: 600;
        """)
        self.username_input.setFont(QFont("Sans-serif", 10, QFont.Medium))
        self.username_input.returnPressed.connect(self.parent.on_submit_clicked)
        input_layout.addSpacing(15)
        input_layout.addWidget(self.username_input)

        self.submit_button = QPushButton("→")
        self.submit_button.setFixedSize(50, 50)
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 25px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.submit_button.clicked.connect(self.parent.on_submit_clicked)
        input_layout.addWidget(self.submit_button)

        layout.addLayout(input_layout)

    def reposition_frame(self):
        right_offset = 350
        self.frame.move(self.parent.width() // 2 - self.frame.width() // 2 + right_offset, self.parent.height() // 2 - self.frame.height() // 2)
