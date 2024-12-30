import PySide6.QtWidgets
from Qt.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from typing import *
from Dewins.backend.file_manager import File
from PySide6.QtCore import Qt

class WidgetVisualise(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._l = QVBoxLayout(self)
        self._vis_label = QLabel()
        self._l.addWidget(self._vis_label)
        self._cached_pixmap: QPixmap = None

    def update_data(self, data: Any):
        print(f"Set {data}")
        if isinstance(data, File):
            if data.extension in ["jpg", "png", "bmp", "gif"] and data.path is not None:
                self._cached_pixmap = QPixmap(data.path)
                self._vis_label.setPixmap(
                    self._cached_pixmap.copy().scaled(
                        self._vis_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                    )
                )

        elif isinstance(data, str):
            self._vis_label.setText(data)
        elif isinstance(data, int) or isinstance(data, float):
            self._vis_label.setText(f"{str(data):.2f}")
        else:
            print("ERROR что за тип емае Ты передал?", data)

    def resizeEvent(self, event):
        if self._vis_label.pixmap():
            scaled_pixmap = self._cached_pixmap.copy().scaled(self._vis_label.size(),
                                                                              Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation)
            self._vis_label.setPixmap(scaled_pixmap)
        super().resizeEvent(event)