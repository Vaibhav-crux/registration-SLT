from app.models.userInfo import UserInfo
from app.config.refreshSession import create_session

def update_user_details(user_id, password, fullname, email, mobile, address):
    session = create_session()
    
    try:
        # Validate mobile number
        if not mobile.isdigit() or len(mobile) != 10:
            return False, "Invalid mobile number. It must contain exactly 10 digits."

        # Validate password
        if not password:
            return False, "Password cannot be empty."

        # Query the user in the database
        user_info = session.query(UserInfo).filter_by(id=user_id).first()

        if not user_info:
            return False, "User not found."

        # Update the user information
        user_info.password = password
        user_info.fullName = fullname
        user_info.email = email
        user_info.mobileNumber = mobile
        user_info.Address = address

        # Commit the changes to the database
        session.commit()
        return True, "User details saved successfully."
        
    except Exception as e:
        # Rollback in case of error
        session.rollback()
        return False, f"An error occurred: {str(e)}"
        
    finally:
        # Close the session
        session.close()
