
import sys
import os

from PySide6.QtCore import Qt, QUrl, QEvent, QObject
from PySide6.QtGui import (QPixmap, QColor, QPalette, QDragEnterEvent, QDropEvent, QMouseEvent, QFont)
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QFileDialog, QHBoxLayout, QPushButton, QTextEdit)

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


class CalculatorNodeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__layout = QVBoxLayout(self)
        self.resultLabel = QLabel("")
        self.resultLabel.setStyleSheet("color: white;")
        self.__layout.addWidget(self.resultLabel)
        self._layout = QHBoxLayout()
        self.__layout.addLayout(self._layout)
        self.plusButton = QPushButton(self)
        self.plusButton.setObjectName(u'plusButton')
        self.plusButton.setText("+")
        self._layout.addWidget(self.plusButton)
        self.minButton = QPushButton(self)
        self.minButton.setObjectName(u'minButton')
        self.minButton.setText("-")
        self._layout.addWidget(self.minButton)
        self.divButton = QPushButton(self)
        self.divButton.setObjectName(u'divButton')
        self.divButton.setText("/")
        self._layout.addWidget(self.divButton)
        self.multButton = QPushButton(self)
        self.multButton.setObjectName(u'plusButton')
        self.multButton.setText("*")
        self._layout.addWidget(self.multButton)
        self.__layout.setStretch(0, 20)
        self.__layout.setStretch(1, 80)


class NodeWrapperCalculatorWidget(NodeBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_name("Calculator")
        self.custom_widget = CalculatorNodeWidget()
        self.set_custom_widget(self.custom_widget)

    def get_value(self):
        pass
    def set_value(self, text):
        pass

class TrigCalcNodeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__layout = QVBoxLayout(self)
        self.resultLabel = QLabel("")
        self.resultLabel.setStyleSheet("color: white;")
        self.__layout.addWidget(self.resultLabel)
        self.layout1 = QHBoxLayout()
        self.__layout.addLayout(self.layout1)
        self.sinButton = QPushButton(self)
        self.sinButton.setObjectName(u'sinButton')
        self.sinButton.setText("sin")
        self.layout1.addWidget(self.sinButton)
        self.cosButton = QPushButton(self)
        self.cosButton.setObjectName(u'cosButton')
        self.cosButton.setText("cos")
        self.layout1.addWidget(self.cosButton)
        self.tanButton = QPushButton(self)
        self.tanButton.setObjectName(u'tanButton')
        self.tanButton.setText("tan")
        self.layout1.addWidget(self.tanButton)
        self.cotanButton = QPushButton(self)
        self.cotanButton.setObjectName(u'cotanButton')
        self.cotanButton.setText("cotan")
        self.layout1.addWidget(self.cotanButton)
        self.layout2 = QHBoxLayout()
        self.__layout.addLayout(self.layout2)
        self.degreeButton = QPushButton(self)
        self.degreeButton.setObjectName(u'degreeButton')
        self.degreeButton.setText('Градусы')
        self.layout2.addWidget(self.degreeButton)
        self.radianButton = QPushButton(self)
        self.radianButton.setObjectName(u'radianButton')
        self.radianButton.setText('Радианы')
        self.layout2.addWidget(self.radianButton)

        self.__layout.setStretch(0, 15)
        self.__layout.setStretch(1, 70)
        self.__layout.setStretch(2, 15)


class NodeWrapperTrigCalcWidget(NodeBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_name("TrigCalc")
        self.custom_widget = TrigCalcNodeWidget()
        self.set_custom_widget(self.custom_widget)

    def get_value(self):
        pass
    def set_value(self, text):
        pass

class ImageTransformNodeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout = QVBoxLayout(self)
        self.layout1 = QHBoxLayout()
        self._layout.addLayout(self.layout1)
        self.label1 = QLabel("Разрешение: ")
        self.font = QFont()
        self.font.setPointSize(16)
        self.label1.setFont(self.font)
        self.layout1.addWidget(self.label1)
        self.widthTextEdit = QTextEdit(self)
        self.widthTextEdit.setObjectName(u'widthTextEdit')
        self.widthTextEdit.setFixedHeight(30)
        self.layout1.addWidget(self.widthTextEdit)
        self.label1_1 = QLabel('  X  ')
        self.label1_1.setFont(self.font)
        self.layout1.addWidget(self.label1_1)
        self.heightTextEdit = QTextEdit(self)
        self.heightTextEdit.setObjectName(u'heightTextEdit')
        self.heightTextEdit.setFixedHeight(30)
        self.layout1.addWidget(self.heightTextEdit)
        self.layout1.setSpacing(0)
        self.layout1.setStretch(0, 10)
        self.layout1.setStretch(1, 44)
        self.layout1.setStretch(2, 2)
        self.layout1.setStretch(3, 44)
        self.layout2 = QHBoxLayout()
        self._layout.addLayout(self.layout2)
        self.label2 = QLabel("Поворот, °:   ")
        self.label2.setFont(self.font)
        self.layout2.addWidget(self.label2)
        self.rotationTextEdit = QTextEdit(self)
        self.rotationTextEdit.setObjectName(u'rotationTextEdit')
        self.rotationTextEdit.setFixedHeight(30)
        self.layout2.addWidget(self.rotationTextEdit)
        self.layout2.setSpacing(1)
        self.layout2.setStretch(0, 19)
        self.layout2.setStretch(1, 81)


class NodeWrapperImageTransformWidget(NodeBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_name("ImageTransform")
        self.custom_widget = ImageTransformNodeWidget()
        self.set_custom_widget(self.custom_widget)

    def get_value(self):
        pass
    def set_value(self, text):
        pass

