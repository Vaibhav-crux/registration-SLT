from PyQt5.QtWidgets import QLineEdit, QDoubleSpinBox, QDateEdit
from app.utils.cursor.next_entry_box_cursor import move_cursor_next, is_enter_key
from PyQt5.QtGui import QKeyEvent

class MyLineEdit(QLineEdit):
    def keyPressEvent(self, event: QKeyEvent):
        if is_enter_key(event.key()):
            move_cursor_next()
        else:
            super().keyPressEvent(event)

class MyDoubleSpinBox(QDoubleSpinBox):
    def keyPressEvent(self, event: QKeyEvent):
        if is_enter_key(event.key()):
            move_cursor_next()
        else:
            super().keyPressEvent(event)

class MyDateEdit(QDateEdit):
    def keyPressEvent(self, event: QKeyEvent):
        if is_enter_key(event.key()):
            move_cursor_next()
        else:
            super().keyPressEvent(event)