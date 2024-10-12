from app.config.db_config import SessionLocal
from app.models.userInfo import UserInfo

def check_user_credentials(username):
    """
    Check if a user with the provided username exists.
    
    :param username: The username to check.
    :return: The user object if a match is found, otherwise None.
    """
    session = SessionLocal()
    try:
        user = session.query(UserInfo).filter_by(username=username).first()
        return user  # Return the user if found, otherwise None
    finally:
        session.close()
