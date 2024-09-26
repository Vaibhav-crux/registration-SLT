from app.controllers.utilities.doMaintenance.check_user_creds import check_user_credentials
from app.controllers.utilities.doMaintenance.delete_do_number_controller import delete_do_number_from_db

class DeleteDoNumberService:

    @staticmethod

    def delete_do_number(do_number, username, password):
        # Check user credentials
        if not check_user_credentials(username, password):
            return False, "Invalid credentials"

        # If credentials are valid, proceed to delete the DO Number
        return delete_do_number_from_db(do_number)