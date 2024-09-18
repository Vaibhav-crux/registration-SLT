from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt

def apply_drop_shadow(widget):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(20)
    shadow.setOffset(0, 0)
    shadow.setColor(Qt.black)
    widget.setGraphicsEffect(shadow)
