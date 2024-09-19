# Import the necessary functions from frame_utils and others
from app.utils.frame_utils import apply_drop_shadow, apply_rounded_corners
from app.utils.drag_window_utils import start_dragging, continue_dragging, stop_dragging
from app.utils.mode_utils import apply_dark_mode
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt

class InternalRegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Remove the title bar and make the window frameless
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Set the window modality to block all other windows until this is closed
        self.setWindowModality(Qt.ApplicationModal)

        # Set the window attribute to make the background fully transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set the size of the window
        self.setGeometry(100, 100, 500, 500)

        # Initialize dragging variables
        self.dragging_position = None

        # Create a frame to contain the content, and apply shadow and rounded corners to this frame
        self.container_frame = QFrame(self)
        self.container_frame.setGeometry(10, 10, 480, 480)  # Give some padding to show shadow
        self.container_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(46, 46, 46, 240);  /* Semi-transparent background inside */
                border-radius: 15px;  /* Rounded corners */
            }
        """)

        # Apply shadow effect to the container frame
        apply_drop_shadow(self.container_frame)

        # Apply rounded corners to the container frame
        apply_rounded_corners(self.container_frame, corner_radius=15)

        # Set up layout and widgets inside the frame
        layout = QVBoxLayout(self.container_frame)

        label = QLabel("Registration", self.container_frame)  # Display "Registration" text
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  # Align text to top-center
        layout.addWidget(label)

        # Remove extra margin and spacing inside the frame
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(0)

        self.container_frame.setLayout(layout)

        # Apply dark mode to the window
        apply_dark_mode(self)

    # Override the mousePressEvent to start dragging
    def mousePressEvent(self, event):
        start_dragging(self, event)

    # Override the mouseMoveEvent to continue dragging
    def mouseMoveEvent(self, event):
        continue_dragging(self, event)

    # Override the mouseReleaseEvent to stop dragging
    def mouseReleaseEvent(self, event):
        stop_dragging(self, event)

