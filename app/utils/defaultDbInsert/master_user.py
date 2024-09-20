from app.config.refreshSession import create_session
from app.models.userInfo import UserInfo, AuthTypeEnum
from sqlalchemy.orm.exc import NoResultFound
import uuid
from datetime import datetime

def automate_saving_master_user():
    session = create_session()

    try:
        # Check if the user with the same username, password, and authType already exists
        existing_user = session.query(UserInfo).filter_by(
            username="SLT",
            password="123",  # In production, use hashed passwords for security!
            authType=AuthTypeEnum.MASTER
        ).one_or_none()

        if existing_user is None:
            # If the user doesn't exist, insert the new master user
            master_user = UserInfo(
                username="SLT",
                password="123",  # It's recommended to hash the password in a real application
                authType=AuthTypeEnum.MASTER,
                empId=None,
                fullName=None,
                email=None,
                desigantion=None,
                Address=None,
                mobileNumber=None,
                organisation=None,
            )

            session.add(master_user)
            session.commit()
            print("Master user inserted successfully.")
        else:
            print("Master user with the same credentials already exists. Skipping insertion.")

    except Exception as e:
        print(f"An error occurred while checking/inserting the master user: {e}")

    finally:
        session.close()

# Call the function to insert the master user when the module is executed
if __name__ == "__main__":
    automate_saving_master_user()
