from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pathlib import Path
from app.services.tools.internalRegistration.newServices.paymentServices.check_img_path_service import check_image_exists

def setup_upi_payment_ui(dialog):
    layout = QVBoxLayout()

    # Create a frame to hold the QR code without a border
    qr_frame = QFrame(dialog)
    qr_frame.setFrameShape(QFrame.NoFrame)  # Remove the frame border
    qr_frame_layout = QVBoxLayout(qr_frame)

    # Load and display the QR code image
    qr_label = QLabel(qr_frame)

    # Check if the image exists
    if check_image_exists():
        current_directory = Path(__file__).resolve().parent  # Get current directory of the script
        project_root = current_directory.parents[4]  # Go back four levels to the root of the project ('registration')
        qr_image_path = project_root / 'static' / 'images' / 'upi.png'

        pixmap = QPixmap(str(qr_image_path))
        if not pixmap.isNull():
            qr_label.setPixmap(pixmap)
            qr_label.setAlignment(Qt.AlignCenter)
    else:
        qr_label.setText("QR Code image not available.")
        qr_label.setAlignment(Qt.AlignCenter)

    qr_frame_layout.addWidget(qr_label)
    layout.addWidget(qr_frame)

    # Create button layout
    button_layout = QHBoxLayout()

    # Confirm button
    confirm_button = QPushButton("Confirm", dialog)
    confirm_button.setFixedWidth(100)
    confirm_button.clicked.connect(dialog.accept)  # Close dialog with accept
    button_layout.addWidget(confirm_button)

    # Cancel button
    cancel_button = QPushButton("Cancel", dialog)
    cancel_button.setFixedWidth(100)
    cancel_button.clicked.connect(dialog.reject)  # Close dialog with reject
    button_layout.addWidget(cancel_button)

    layout.addLayout(button_layout)

    dialog.setLayout(layout)
