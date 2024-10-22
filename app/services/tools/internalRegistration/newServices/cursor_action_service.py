# app\services\tools\internalRegistration\newServices\cursor_action_service.py

from PyQt5.QtWidgets import QComboBox, QPushButton
from PyQt5.QtCore import Qt

class FocusableComboBox(QComboBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.confirm_button = None  # To store the button to trigger on Enter

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            # Trigger the confirm button's click if it is set
            if isinstance(self.confirm_button, QPushButton):
                self.confirm_button.click()
        else:
            super().keyPressEvent(event)
