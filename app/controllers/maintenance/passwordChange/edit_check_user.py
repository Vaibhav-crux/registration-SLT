from app.config.db_config import SessionLocal
from app.models.userInfo import UserInfo

def check_user_credentials(username, password):
    """
    Check if a user with the provided username and password exists.
    
    :param username: The username to check.
    :param password: The password to check.
    :return: The user object if a match is found, otherwise None.
    """
    session = SessionLocal()
    try:
        user = session.query(UserInfo).filter_by(username=username, password=password).first()
        return user
    finally:
        session.close()
