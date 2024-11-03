from sqlalchemy.orm import Session
from app.config.refreshSession import create_session
from app.models.vehicleInOut import VehicleInOut

def fetch_vehicle_type_data():
    """Fetch all vehicle data from the vehicle_in_out table."""
    session = create_session()
    try:
        # Fetch all records from the vehicle_in_out table, excluding 'ID', 'Created At', and 'Updated At'
        records = session.query(
            VehicleInOut.rfidTag,
            VehicleInOut.typeOfVehicle,
            VehicleInOut.vehicleNumber,
            VehicleInOut.doNumber,
            VehicleInOut.transporter,
            VehicleInOut.driverOwner,
            VehicleInOut.weighbridgeNo,
            VehicleInOut.visitPurpose,
            VehicleInOut.placeToVisit,
            VehicleInOut.personToVisit,
            VehicleInOut.validityTill,
            VehicleInOut.section,
            VehicleInOut.dateIn,
            VehicleInOut.timeIn,
            VehicleInOut.user,
            VehicleInOut.shift,
            VehicleInOut.dateOut,
            VehicleInOut.timeOut,
            VehicleInOut.gross,
            VehicleInOut.tare,
            VehicleInOut.net,
            VehicleInOut.barrierStatus,
            VehicleInOut.challanNo
        ).all()
        
        # Define the column names you want to display
        column_names = [
            'RFID Tag', 'Vehicle Type', 'Vehicle Number', 'DO Number',
            'Transporter', 'Driver/Owner', 'Weighbridge No', 'Visit Purpose',
            'Place to Visit', 'Person to Visit', 'Validity Till', 'Section',
            'Date In', 'Time In', 'User', 'Shift', 'Date Out', 'Time Out',
            'Gross', 'Tare', 'Net', 'Barrier Status', 'Challan No'
        ]
        
        # Create a list of tuples where each tuple is a row
        data = [
            (
                record.rfidTag, record.typeOfVehicle.value, record.vehicleNumber, record.doNumber,
                record.transporter, record.driverOwner, record.weighbridgeNo,
                record.visitPurpose, record.placeToVisit, record.personToVisit,
                record.validityTill, record.section, record.dateIn, record.timeIn,
                record.user, record.shift, record.dateOut, record.timeOut,
                record.gross, record.tare, record.net, record.barrierStatus.value,
                record.challanNo
            )
            for record in records
        ]
        
        return column_names, data
    finally:
        session.close()
