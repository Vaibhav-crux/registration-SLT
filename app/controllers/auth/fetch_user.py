from app.config.refreshSession import create_session
from app.models.userInfo import UserInfo
from sqlalchemy.orm.exc import NoResultFound

def check_username_exists(username):
    """Check if a user with the given username exists in the database."""
    session = create_session()

    try:
        # Check if the username exists
        user = session.query(UserInfo).filter_by(username=username).one_or_none()
        return user is not None  # Return True if user exists, otherwise False

    except Exception as e:
        print(f"Error while checking username: {e}")
        return False  # Return False if any exception occurs

    finally:
        session.close()

def verify_user_credentials(username, password):
    """Check if the username and password match a user in the database."""
    session = create_session()

    try:
        # Check if the username and password match
        user = session.query(UserInfo).filter_by(username=username, password=password).one_or_none()
        return user is not None  # Return True if credentials match, otherwise False

    except Exception as e:
        print(f"Error while verifying credentials: {e}")
        return False  # Return False if any exception occurs

    finally:
        session.close()
