from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pathlib import Path
from app.services.tools.internalRegistration.newServices.paymentServices.check_img_path_service import check_image_exists
from app.utils.template.html_generator import generate_html
from app.services.tools.internalRegistration.newServices.paymentServices.payment_receipt_service import show_payment_receipt_window

def setup_upi_payment_ui(dialog, total_amount, data):
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
    confirm_button.clicked.connect(lambda: on_confirm_click(dialog, total_amount, data))  # Call on_confirm_click with necessary params
    button_layout.addWidget(confirm_button)

    # Cancel button
    cancel_button = QPushButton("Cancel", dialog)
    cancel_button.setFixedWidth(100)
    cancel_button.clicked.connect(dialog.reject)  # Close dialog with reject
    button_layout.addWidget(cancel_button)

    layout.addLayout(button_layout)

    dialog.setLayout(layout)

def on_confirm_click(dialog, total_amount, data):
    # Add UPI confirmation logic here
    full_data = data.copy()
    full_data["Payment Mode"] = "UPI"
    full_data["Total Amount"] = total_amount
    full_data["Payment Status"] = "Paid"  # Assuming payment was successful

    # Generate the HTML file now, after UPI payment is confirmed
    generate_html(full_data, "rfid_details.html")

    # Close the UPI payment dialog before opening the receipt window
    dialog.reject()

    # Open the payment receipt window after generating the HTML file
    show_payment_receipt_window()
