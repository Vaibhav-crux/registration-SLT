from app.models.doMaintenance import DoData
from app.config.refreshSession import create_session
from PyQt5.QtWidgets import QMessageBox

def save_do_maintenance(data: dict, window) -> bool:
    """
    Saves the DO Maintenance data to the database.
    :param data: Dictionary containing all the input values.
    :param window: Reference to the window to display messages.
    :return: bool indicating success or failure.
    """
    session = create_session()

    try:
        # Check if doNumber already exists
        existing_do = session.query(DoData).filter_by(doNumber=data['do_number']).first()
        
        if existing_do:
            # Show error message
            QMessageBox.critical(window, "Error", f"DO Number {data['do_number']} already exists.")
            return False

        # Create a new DoData object with all the provided values
        new_do = DoData(
            doNumber=data['do_number'],
            weighbridgeNo=data['weighbridge_no'],
            transporter=data['transporter'],
            permissidoNameon=data.get('permission_name', None),
            validThrough=data.get('valid_through', None),
            validityTill=data.get('validity_till', None),
            allotedQty=data.get('alloted_qty', 0.0),
            releasedQty=data.get('released_qty', 0.0),
            leftQty=data.get('left_qty', 0.0),
            doAddress=data.get('do_address', None),
            doRoute=data.get('do_route', None),
            salesOrder=data.get('sales_order', None),
            customerId=data.get('customer_id', None),
            mobileNumber=data.get('mobile_number', None)
        )

        # Add the new object to the session
        session.add(new_do)

        # Commit the changes to the database
        session.commit()

        # Show success message
        QMessageBox.information(window, "Success", "DO Maintenance record saved successfully!")
        return True
    except Exception as e:
        # Rollback in case of any error
        session.rollback()

        # Show error message
        QMessageBox.critical(window, "Error", f"Failed to save DO Maintenance record: {str(e)}")
        return False
    finally:
        # Close the session
        session.close()