from pathlib import Path
from Dewins.ui.NodeGraph import (
    NodeGraph,
    PropertiesBinWidget,
    NodesTreeWidget,
    NodesPaletteWidget, NodeObject
)
from Qt.QtWidgets import QWidget, QVBoxLayout
from Dewins.ui.NodeGraph import BaseNode, BaseNodeCircle

from Dewins.ui.Components.Graph.Nodes.InputNode import (
    TextInputNode,
    ImageInputNode,
    InputNodePrototype
)


class GraphEditor:
    def __init__(self):
        self.BASE_PATH = Path(__file__).parent.parent.parent.resolve() #TODO parentx3? Грех на душу берешь, грех
        print(self.BASE_PATH)
        self.hotkey_path = Path(self.BASE_PATH, 'hotkeys', 'hotkeys.json')
        self.graph = NodeGraph()

        self.graph.set_context_menu_from_file(self.hotkey_path, 'graph')

        self.graph.widget.resize(1100, 800)
        self.graph.register_nodes([
            TextInputNode,
            ImageInputNode
        ])

    def run(self):
        inputs = []
        for node in self.graph.all_nodes():
            if isinstance(node, InputNodePrototype):
                inputs.append(node)

    def context_menu_open_file(self):
        pass

    def get_nodes_list(self):
        pass
