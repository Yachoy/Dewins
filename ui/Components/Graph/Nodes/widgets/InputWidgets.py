from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QUrl, QEvent, QObject
from PySide6.QtGui import QPixmap, QColor, QPalette, QDragEnterEvent, QDropEvent, QMouseEvent
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QFileDialog, QVBoxLayout, QLabel, QPlainTextEdit)
from Dewins.ui.NodeGraph import NodeBaseWidget

from typing import *

class TextInputNodeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout = QVBoxLayout(self)
        self.input_plain_text = QPlainTextEdit("Text here...")
        self.input_plain_text.setFont(QFont("Times New Roman", 16))
        self._layout.addWidget(self.input_plain_text)


class NodeWrapperTextInputWidget(NodeBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_name('my_widget')
        self.custom_widget = TextInputNodeWidget()
        self.set_custom_widget(self.custom_widget)

    def get_value(self):
        pass

    def set_value(self, text):
        pass

class ImageInputNodeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.initUI()
        self._last_filepath = None

    def initUI(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Image")
        self.label.setAlignment(Qt.AlignCenter)

        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, Qt.white)
        self.label.setPalette(palette)

        self.label.setStyleSheet("font-size: 16px;")

        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


        # Эффект наведения мыши
        self.label.installEventFilter(self)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if watched == self.label and event.type() == QEvent.Enter:
            palette = self.label.palette()
            palette.setColor(QPalette.WindowText, QColor(200, 200, 200))  # Светлее при наведении
            self.label.setPalette(palette)
        elif watched == self.label and event.type() == QEvent.Leave:
            palette = self.label.palette()
            palette.setColor(QPalette.WindowText, Qt.white)  # Белый, когда мышь уходит
            self.label.setPalette(palette)
        return super().eventFilter(watched, event)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    filepath = url.toLocalFile()
                    self.setImage(filepath)
        else:
            event.ignore()

    def openFileDialog(self, event: QMouseEvent):
        filepath, _ = QFileDialog.getOpenFileName(None, "Выберите изображение", "",
                                                  "Изображения (*.png *.jpg *.jpeg *.bmp *.gif)")
        if filepath:
            self.setImage(filepath)

    def setImage(self, filepath):
        self._last_filepath = filepath
        pixmap = QPixmap(self._last_filepath)

        if not pixmap.isNull():
            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.label.setText("Не удалось загрузить изображение")

    def get_last_path_image(self) -> Optional[str]: return self._last_filepath

class NodeWrapperImageInputWidget(NodeBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_name('my_widget')
        self.custom_widget = ImageInputNodeWidget()
        self.set_custom_widget(self.custom_widget)

        self.mouse_click.connect(self.custom_widget.openFileDialog)
        self.resize(220, 110)

    def get_value(self):
        pass

    def set_value(self, text):
        pass