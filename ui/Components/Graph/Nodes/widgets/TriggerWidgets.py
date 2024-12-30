
import sys
import os

from PySide6.QtCore import Qt, QUrl, QEvent, QObject
from PySide6.QtGui import (QPixmap, QColor, QPalette, QDragEnterEvent, QDropEvent, QMouseEvent, QFont)
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QFileDialog, QHBoxLayout, QPushButton, QTextEdit)

from Dewins.ui.NodeGraph import NodeBaseWidget


class TriggerOnUserClickNodeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout = QVBoxLayout(self)
        self.l = QLabel("")
        self.l.setStyleSheet("color: white;")
        self._layout.addWidget(self.l)


class NodeWrapperTriggerNodeWidget(NodeBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_name('my_widget')
        self.custom_widget = TriggerOnUserClickNodeWidget()
        self.set_custom_widget(self.custom_widget)

    def get_value(self):
        pass

    def set_value(self, text):
        pass