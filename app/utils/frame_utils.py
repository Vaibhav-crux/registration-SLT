from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

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

def center_window(widget):
    """
    Centers the given window on the screen.
    
    :param widget: The window or widget to center.
    """
    # Get the geometry of the screen
    screen_geometry = QDesktopWidget().availableGeometry()
    screen_center = screen_geometry.center()

    # Get the geometry of the window
    window_geometry = widget.frameGeometry()

    # Move the window to the center of the screen
    window_geometry.moveCenter(screen_center)
    widget.move(window_geometry.topLeft())
