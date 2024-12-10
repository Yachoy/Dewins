from Dewins.ui.NodeGraph import (
    NodeGraph,
    PropertiesBinWidget,
    NodesTreeWidget,
    NodesPaletteWidget
)
from Qt.QtWidgets import QWidget

class EditorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def open_file(self):
        pass
