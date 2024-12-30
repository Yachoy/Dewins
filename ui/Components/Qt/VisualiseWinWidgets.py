import PySide6.QtWidgets
import numpy as np
from Qt.QtWidgets import QWidget, QVBoxLayout, QLabel
from Qt.QtCore import Signal

from PySide6.QtGui import QPixmap, QMouseEvent
from typing import *
from Dewins.backend.file_manager import File
from PySide6.QtCore import Qt, QObject
from PySide6.QtGui import QImage, QPixmap
import cv2

class WidgetVisualise(QWidget):
    click_lmb_signal: Signal = Signal(PySide6.QtGui.QMouseEvent)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._l = QVBoxLayout(self)
        self._vis_label = QLabel()
        self._l.addWidget(self._vis_label)
        self._cached_pixmap: QPixmap = None

    def get_label(self):
        return self._vis_label

    def get_cached_pixmap(self):
        return self._cached_pixmap

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.click_lmb_signal.emit(event)

    def update_data(self, data: Any):
        print(f"Set {data if not isinstance(data, np.ndarray) else 'np.ndarray'}")
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
            self._vis_label.setText(f"{str(data)}")
        elif isinstance(data, np.ndarray):
            array_rgb = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
            height, width, channel = array_rgb.shape
            bytes_per_line = channel * width
            q_image = QImage(array_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

            self._cached_pixmap = QPixmap.fromImage(q_image)
            self._vis_label.setPixmap(
                self._cached_pixmap.copy().scaled(
                    self._vis_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
            )
        else:
            print("ERROR что за тип емае Ты передал?", data)

    def resizeEvent(self, event):
        if self._vis_label.pixmap():
            scaled_pixmap = self._cached_pixmap.copy().scaled(self._vis_label.size(),
                                                                              Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation)
            self._vis_label.setPixmap(scaled_pixmap)
        super().resizeEvent(event)
