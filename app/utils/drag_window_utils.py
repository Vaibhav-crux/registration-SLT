# app/utils/drag_window_utils.py

from PyQt5.QtCore import QPoint

def start_dragging(widget, event):
    """
    Captures the initial mouse position when the dragging starts.
    Should be called in the mousePressEvent.
    
    :param widget: The widget (or window) to be dragged.
    :param event: The mouse press event.
    :return: None
    """
    if event.button() == event.button():
        widget.dragging_position = event.globalPos()

def continue_dragging(widget, event):
    """
    Moves the widget (or window) based on the difference between the current and initial mouse positions.
    Should be called in the mouseMoveEvent.
    
    :param widget: The widget (or window) to be dragged.
    :param event: The mouse move event.
    :return: None
    """
    if widget.dragging_position is not None:
        delta = QPoint(event.globalPos() - widget.dragging_position)
        widget.move(widget.x() + delta.x(), widget.y() + delta.y())
        widget.dragging_position = event.globalPos()

def stop_dragging(widget, event):
    """
    Stops the dragging process by resetting the dragging_position.
    Should be called in the mouseReleaseEvent.
    
    :param widget: The widget (or window) that was being dragged.
    :param event: The mouse release event.
    :return: None
    """
    widget.dragging_position = None
