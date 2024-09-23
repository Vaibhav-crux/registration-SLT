from PyQt5.QtWidgets import QGraphicsBlurEffect

def apply_blur_effect(window):
    blur_effect = QGraphicsBlurEffect()
    blur_effect.setBlurRadius(10)
    window.setGraphicsEffect(blur_effect)

def remove_blur_effect(window):
    window.setGraphicsEffect(None)