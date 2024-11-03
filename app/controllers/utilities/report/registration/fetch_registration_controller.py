from sqlalchemy.orm import Session
from app.config.refreshSession import create_session
from app.models.vehicleRegistration import VehicleRegistration

def fetch_all_registration_data():
    """Fetch all vehicle registration data from the vehicle_registration table."""
    session = create_session()
    try:
        # Fetch all records from the vehicle_registration table
        records = session.query(VehicleRegistration).all()
        
        # Define the column names you want to display
        column_names = [
            'RFID Tag', 'Vehicle Type', 'Vehicle Number', 'DO Number',
            'Transporter', 'Driver/Owner', 'Weighbridge No', 'Visit Purpose',
            'Place to Visit', 'Person to Visit', 'Validity Till', 'Section',
            'Register Date', 'Register Time', 'User', 'Shift', 'Loading'
        ]
        
        # Create a list of tuples where each tuple is a row
        data = [
            (
                record.rfidTag, record.typeOfVehicle.value, record.vehicleNumber, record.doNumber,
                record.transporter, record.driverOwner, record.weighbridgeNo,
                record.visitPurpose, record.placeToVisit, record.personToVisit,
                record.validityTill, record.section, record.registerDate, record.registerTime,
                record.user, record.shift, record.loading
            )
            for record in records
        ]
        
        return column_names, data
    finally:
        session.close()
