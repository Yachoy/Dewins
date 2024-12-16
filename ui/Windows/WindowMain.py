from Qt.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from Qt.QtCore import QCoreApplication, QMetaObject

from Dewins.ui.Components.Graph.NodeEditor import GraphEditor

class EmptySchemeDesign(object):#TODO when add .ui file with code of ui, replace in project any interactive with this class to Ui

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.l = QVBoxLayout()
        self.centralwidget.setLayout(self.l)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

class MainWindow(QMainWindow, EmptySchemeDesign):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ---- add graph widget ----
        self.node_editor = GraphEditor()
        self.l.addWidget(self.node_editor.graph.widget)


