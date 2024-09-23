# app\utils\next_entry_box_cursor.py
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

def move_cursor_next():
    tab_event = QKeyEvent(QEvent.KeyPress, Qt.Key_Tab, Qt.NoModifier)
    QApplication.postEvent(QApplication.focusWidget(), tab_event)

def is_enter_key(key):
    return key == Qt.Key_Return or key == Qt.Key_Enter