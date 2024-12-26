from pathlib import Path
from typing import *

import PySide6.QtWidgets

from Dewins.ui.Components.Graph.Nodes.Prototypes.CommonNodeProto import CommonNodePrototype
from Dewins.ui.Components.Graph.Nodes.Prototypes.VisualiseNode import VisualiseNode
from Dewins.ui.NodeGraph import (
    NodeGraph,
    PropertiesBinWidget,
    NodesTreeWidget,
    NodesPaletteWidget, NodeObject
)
from Qt.QtWidgets import QWidget, QVBoxLayout
from Dewins.ui.NodeGraph import BaseNode, BaseNodeCircle

from Dewins.ui.Components.Graph.Nodes.InputNode import (
    TextNode,
    ImageNode,
    InputNodePrototype,
)

from Dewins.ui.Components.Graph.Nodes.ProcessNode import (
    CountWordNode,
    CalculatorNode,
    TrigCalcNode
)


class GraphEditor:
    def __init__(self):
        self.BASE_PATH = Path(__file__).parent.parent.parent.resolve() #TODO parentx3? Грех на душу берешь, грех
        self.hotkey_path = Path(self.BASE_PATH, 'hotkeys', 'hotkeys.json')
        self.graph = NodeGraph()
        self.graph.set_context_menu_from_file(self.hotkey_path, 'graph')

        self.graph.node_double_clicked.connect(self.run)
        self.graph.node_created.connect(self.on_node_created)

        self.graph.widget.resize(1100, 800)
        self.graph.register_nodes([
            CountWordNode,
            TextNode,
            ImageNode,
            VisualiseNode,
            CalculatorNode,
            TrigCalcNode
        ])

    def run(self):
        inputs = []
        for node in self.graph.all_nodes():
            if isinstance(node, InputNodePrototype):
                inputs.append(node)
        for i in inputs:
            if i.run(): return True
        return False

    wins = []
    def on_node_created(self, node: CommonNodePrototype):
        if isinstance(node, VisualiseNode):
            print("Create win")
            win = QWidget()
            layout = QVBoxLayout(win)
            label = PySide6.QtWidgets.QLabel(win)
            layout.addWidget(label)
            node.set_visualise_label(label)
            win.show()
            self.wins.append(win)