# app/utils/frame_utils.py

from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainterPath, QColor, QRegion

def apply_drop_shadow(widget):
    """
    Applies a drop shadow effect to the given widget.
    
    :param widget: The widget to which the shadow effect should be applied.
    """
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(20)
    shadow.setOffset(0, 0)
    shadow.setColor(QColor(0, 102, 204))  # RGB for professional blue
    widget.setGraphicsEffect(shadow)

def apply_rounded_corners(widget, corner_radius=15):
    """
    Applies rounded corners to the given widget by setting a mask.
    
    :param widget: The widget to which rounded corners should be applied.
    :param corner_radius: The radius of the corners (default is 15px).
    """
    path = QPainterPath()
    rect_f = QRectF(widget.rect())  # Convert QRect to QRectF
    path.addRoundedRect(rect_f, corner_radius, corner_radius)
    region = QRegion(path.toFillPolygon().toPolygon())
    widget.setMask(region)
