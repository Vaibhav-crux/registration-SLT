from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt

def set_background_image(window, image_path):
    pixmap = QPixmap(image_path)
    scaled_pixmap = pixmap.scaled(window.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(scaled_pixmap))
    window.setPalette(palette)
