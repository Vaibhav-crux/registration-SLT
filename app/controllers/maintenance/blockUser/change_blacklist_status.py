from sqlalchemy import or_
from app.config.refreshSession import create_session
from app.models.allotedTags import AllotedTags

def change_blacklist_status(rfid_tag, vehicle_no, action):
    session = create_session()
    try:
        # Search for the user by RFID Tag or Vehicle Number
        user_info = session.query(AllotedTags).filter(
            or_(AllotedTags.rfidTag == rfid_tag, AllotedTags.vehicleNumber == vehicle_no)
        ).first()

        if not user_info:
            return "RFID Tag or Vehicle Number not found.", False

        # Determine the desired blacklist status based on action
        if action == "Blacklist":
            desired_status = True
        elif action == "Unblacklist":
            desired_status = False
        else:
            return "Invalid action selected.", False

        # Check if the status is already set
        if user_info.blacklisted == desired_status:
            return f"User is already {'blacklisted' if desired_status else 'unblacklisted'}.", False

        # Update the blacklist status
        user_info.blacklisted = desired_status
        session.commit()
        return "User status updated successfully.", True

    except Exception as e:
        session.rollback()
        return f"An error occurred: {str(e)}", False
    finally:
        session.close()
