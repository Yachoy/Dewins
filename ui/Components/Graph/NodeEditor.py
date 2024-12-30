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
    ImageNode
)

from Dewins.ui.Components.Graph.Nodes.ProcessNode import (
    CountWordNode,
    CalculatorNode,
    TrigCalcNode,
    ImageTransform
)

from Dewins.ui.Components.Qt.VisualiseWinWidgets import WidgetVisualise


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
            TrigCalcNode,
            ImageTransform
        ])

    def run(self) -> bool:
        inputs = []
        print("Start scheme")
        for node in self.graph.all_nodes():
            if node.__identifier__ == "Input":
                inputs.append(node)
        for i in inputs:
            if not i.run():
                print("Что-то пошло не так....")
                return False
            print("################")
        return True

    wins = []
    def on_node_created(self, node: CommonNodePrototype):
        if isinstance(node, VisualiseNode):
            print("Create win")
            win = WidgetVisualise()
            node.set_visualise_widget(win)
            win.show() #TODO except in future this needs to make mechanism of creating widgets (also may be use QDocker?)
            self.wins.append(win)