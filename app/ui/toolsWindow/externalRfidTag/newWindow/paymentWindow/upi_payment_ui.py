from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pathlib import Path
from app.services.tools.externalRegistration.newServices.paymentServices.check_img_path_service import check_image_exists
from app.utils.template.html_generator import generate_html
from app.services.tools.externalRegistration.newServices.paymentServices.payment_receipt_service import show_payment_receipt_window
from app.utils.random_string_generator import generate_sales_order_no, generate_transaction_id
from app.controllers.tools.internalRegistration.save_into_alloted_tag import save_alloted_tag
from app.controllers.tools.internalRegistration.save_into_registration import save_vehicle_registration
from datetime import datetime
from app.style.default_styles import button_style
from app.utils.frame_utils import apply_drop_shadow, center_window

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
    confirm_button.setStyleSheet(button_style)
    confirm_button.clicked.connect(lambda: on_confirm_click(dialog, total_amount, data))  # Call on_confirm_click with necessary params
    button_layout.addWidget(confirm_button)

    # Cancel button
    cancel_button = QPushButton("Cancel", dialog)
    cancel_button.setFixedWidth(100)
    cancel_button.setStyleSheet(button_style)
    cancel_button.clicked.connect(dialog.reject)  # Close dialog with reject
    button_layout.addWidget(cancel_button)

    layout.addLayout(button_layout)

    dialog.setLayout(layout)

    center_window(dialog)

def on_confirm_click(dialog, total_amount, data):
    # Prepare full data with the necessary keys
    full_data = data.copy()
    full_data["SALES ORDER NO."] = full_data.get("SALES ORDER NO.", generate_sales_order_no())
    full_data["TRANSACTION ID"] = full_data.get("TRANSACTION ID", generate_transaction_id(data.get("vehicle_no", "")))
    full_data["User id"] = "VAIBHAV"  # Assuming a static user id
    full_data["Create date"] = datetime.now().strftime("%d-%m-%Y")
    full_data["Create Time"] = datetime.now().strftime("%H:%M:%S HRS")
    full_data["BARRIER GATE"] = "NCL BINA PROJECT MAIN BARRIER"
    full_data["SALES TYPE"] = "RFID ALLOCATION"
    full_data["RFID EPC"] = data.get("rfid_tag", "")
    full_data["VEHICLE NO."] = data.get("vehicle_no", "")
    full_data["VEHICLE TYPE"] = data.get("vehicle_type", "")
    full_data["PAYMENT MODE"] = "UPI"
    full_data["STATUS"] = "Paid"  # Assuming payment was successful
    full_data["TOTAL"] = str(total_amount)

    # Save to AllotedTags
    alloted_tag = save_alloted_tag(
        rfidTag=full_data["RFID EPC"],
        typeOfVehicle=full_data["VEHICLE TYPE"],
        vehicleNumber=full_data["VEHICLE NO."],
        regDate=full_data["Create date"],
        regTime=full_data["Create Time"],
        salesOrder=full_data["SALES ORDER NO."],
        transationId=full_data["TRANSACTION ID"],
        userid=full_data["User id"],
        barrierGate=full_data["BARRIER GATE"],
        salesType=full_data["SALES TYPE"],
        quantity="1",
        total=full_data["TOTAL"],
        due=True,
        blacklisted=False
    )

    if alloted_tag:
        # Save to VehicleRegistration if AllotedTags save was successful
        save_vehicle_registration(
            rfidTag=full_data["RFID EPC"],
            typeOfVehicle=full_data["VEHICLE TYPE"],
            vehicleNumber=full_data["VEHICLE NO."],
            doNumber=data.get("do_number", ""),
            transporter=data.get("transporter", ""),
            driverOwner=data.get("driver_owner", ""),
            weighbridgeNo=data.get("weighbridge_no", ""),
            visitPurpose=data.get("visit_purpose", ""),
            placeToVisit=data.get("place_to_visit", ""),
            personToVisit=data.get("person_to_visit", ""),
            validityTill=data.get("calendar", ""),
            section=data.get("section", ""),
            registerDate=full_data["Create date"],
            registerTime=full_data["Create Time"],
            user=full_data["User id"],
            shift=data.get("shift", ""),
            loading=data.get("loading", "")
        )

        # Generate the HTML file after UPI payment is confirmed
        generate_html(full_data, "rfid_details.html")

        # Open the payment receipt window after generating the HTML file
        show_payment_receipt_window(dialog.parent())  # Pass the original parent window
    
    # Close the UPI payment dialog
    dialog.reject()