from app.models.userInfo import UserInfo
from app.config.refreshSession import create_session

def check_user_credentials(username, password):
    """
    Check if the provided username and password match a record in the UserInfo table.
    
    Args:
        username (str): The username to check.
        password (str): The password to check.
    
    Returns:
        bool: True if the credentials match, False otherwise.
    """
    session = create_session()
    try:
        # Query the database for a matching record
        user = session.query(UserInfo).filter_by(username=username).first()
        
        # Check if a user was found and if the password matches
        if user and user.password == password:
            return True
        
        return False
    
    finally:
        session.close()  # Always close the session after use
