import sys
from PyQt5.QtWidgets import QApplication
from app.services.loginWindow.login_window_service import FullScreenWindow

def main():
    app = QApplication(sys.argv)

    # Start with the FullScreenWindow (Login Window)
    login_window = FullScreenWindow()
    login_window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
