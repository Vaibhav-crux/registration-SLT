import sys
from PyQt5.QtWidgets import QApplication
from app.services.loginWindow.login_window_service import FullScreenWindow
from app.config.db_config import init_db
from app.utils.defaultDbInsert.shift_timing import automate_saving_default_shifts
from app.utils.defaultDbInsert.master_user import automate_saving_master_user

def main():
    # Initialize the database connection and create tables if they don't exist
    try:
        init_db()  # Initialize and create tables
        print("Database connection established successfully!")

        # Insert default shift timings if not already present
        automate_saving_default_shifts()

        # Insert the master user if not already present
        automate_saving_master_user()

    except Exception as e:
        print(f"Error establishing database connection: {e}")
        sys.exit(1)  # Exit the program if the connection fails

    # Start the PyQt5 application
    app = QApplication(sys.argv)

    # Start with the FullScreenWindow (Login Window)
    login_window = FullScreenWindow()
    login_window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
