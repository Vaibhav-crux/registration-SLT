from app.config.db_config import SessionLocal
from app.models.userInfo import UserInfo
from sqlalchemy.exc import SQLAlchemyError

def delete_user_by_username(username):
    """
    Delete a user from the database by username.
    
    :param username: The username of the user to be deleted.
    :return: A message indicating success or failure.
    """
    session = SessionLocal()
    try:
        user = session.query(UserInfo).filter(UserInfo.username == username).one_or_none()
        if user:
            session.delete(user)
            session.commit()
            return "User deleted successfully."
        else:
            return "User not found."
    except SQLAlchemyError as e:
        session.rollback()
        return f"An error occurred: {str(e)}"
    finally:
        session.close()
