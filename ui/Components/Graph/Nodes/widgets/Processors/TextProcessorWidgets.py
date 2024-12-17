
import sys
import os

from PySide6.QtCore import Qt, QUrl, QEvent, QObject
from PySide6.QtGui import QPixmap, QColor, QPalette, QDragEnterEvent, QDropEvent, QMouseEvent
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QFileDialog, QVBoxLayout, QLabel)

from Dewins.ui.NodeGraph import NodeBaseWidget


class CountWordsNodeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout = QVBoxLayout(self)
        self.count_words_label = QLabel("")
        self.count_words_label.setStyleSheet("color: white;")
        self._layout.addWidget(self.count_words_label)


class NodeWrapperCountWordsNodeWidget(NodeBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_name('my_widget')
        self.custom_widget = CountWordsNodeWidget()
        self.set_custom_widget(self.custom_widget)

    def get_value(self):
        pass

    def set_value(self, text):
        pass