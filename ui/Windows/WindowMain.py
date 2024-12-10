from Qt.QtWidgets import QMainWindow


class EmptySchemeDesign: #TODO when add .ui file with code of ui, replace in project any interactive with this class to Ui
    def setupUi(self, window): pass


class MainWindow(QMainWindow, EmptySchemeDesign):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

