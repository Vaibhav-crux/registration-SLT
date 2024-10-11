from app.config.db_config import SessionLocal
from app.models.userInfo import UserInfo
from sqlalchemy.exc import SQLAlchemyError

def save_user_data(username, password, auth_type, emp_id, full_name, email, designation, address, mobile_number, organisation):
    """
    Save user data to the database.
    
    :param username: User's username
    :param password: User's password
    :param auth_type: User's authentication type
    :param emp_id: Employee ID
    :param full_name: Full name
    :param email: Email address
    :param designation: Designation
    :param address: Address
    :param mobile_number: Mobile number
    :param organisation: Organisation
    :return: A message indicating success or failure.
    """
    session = SessionLocal()
    try:
        new_user = UserInfo(
            username=username,
            password=password,
            authType=auth_type,
            empId=emp_id,
            fullName=full_name,
            email=email,
            desigantion=designation,
            Address=address,
            mobileNumber=mobile_number,
            organisation=organisation
        )
        session.add(new_user)
        session.commit()
        return "User data saved successfully."
    except SQLAlchemyError as e:
        session.rollback()
        return f"An error occurred: {str(e)}"
    finally:
        session.close()
