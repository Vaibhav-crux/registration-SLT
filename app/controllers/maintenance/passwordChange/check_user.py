from app.config.db_config import SessionLocal
from app.models.userInfo import UserInfo, AuthTypeEnum
from sqlalchemy.exc import SQLAlchemyError

def check_user_auth(username):
    """
    Check if the user exists and if their authType is Admin or Master.
    
    :param username: The username of the user to check.
    :return: A tuple (exists, is_authorized) where 'exists' is True if the user exists, 
             and 'is_authorized' is True if the user's authType is Admin or Master.
    """
    session = SessionLocal()
    try:
        user = session.query(UserInfo).filter(UserInfo.username == username).one_or_none()
        if user:
            # Compare using the name of the enums
            is_authorized = user.authType.name in [AuthTypeEnum.ADMIN.name, AuthTypeEnum.MASTER.name]
            print(f"Authorization result: {is_authorized}")

            return True, is_authorized
        else:
            print("User not found.")
            return False, False
    except SQLAlchemyError as e:
        print(f"An error occurred: {str(e)}")
        return False, False
    finally:
        session.close()
