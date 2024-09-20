import os
from app.config.refreshSession import create_session
from app.models.userInfo import UserInfo
from sqlalchemy.orm.exc import NoResultFound

def get_username_from_file():
    """Read the username from the activeUsername.txt file."""
    try:
        # Define the path to the activeUsername.txt file
        file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'activeUsername.txt')
        file_path = os.path.abspath(file_path)

        # Read the username from the file
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                username = file.read().strip()  # Strip any extra whitespace
                return username if username else None
        else:
            return None  # Return None if the file doesn't exist
    except Exception as e:
        print(f"Error reading username from file: {e}")
        return None

def fetch_user_full_name():
    """Fetch the full name for the username found in activeUsername.txt."""
    username = get_username_from_file()
    unknow_name = "Unknown Full Name"

    if not username:
        return "Unknown User"  # Return default value if username not found

    session = create_session()
    
    try:
        # Query the database to get the user info based on the username
        user = session.query(UserInfo).filter_by(username=username).one_or_none()
        
        if user:
            return user.fullName if user.fullName else unknow_name
        else:
            return "unknow_name"  # Return a default value if the user is not found
    except Exception as e:
        print(f"Error while fetching full name for {username}: {e}")
        return unknow_name  # Return a default value in case of error
    finally:
        session.close()
