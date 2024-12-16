from pathlib import Path
from Dewins.ui.NodeGraph import (
    NodeGraph,
    PropertiesBinWidget,
    NodesTreeWidget,
    NodesPaletteWidget
)
from Qt.QtWidgets import QWidget, QVBoxLayout

from Dewins.ui.NodeGraph import BaseNode, BaseNodeCircle


class BasicNodeA(BaseNode):
    """
    A node class with 2 inputs and 2 outputs.
    """

    # unique node identifier.
    __identifier__ = 'nodes'

    # initial default node name.
    NODE_NAME = 'node A'

    def __init__(self):
        super(BasicNodeA, self).__init__()

        # create node inputs.
        self.add_input('in A')
        self.add_input('in B')

        # create node outputs.
        self.add_output('out A')
        self.add_output('out B')


class GraphEditor:
    def __init__(self):
        self.BASE_PATH = Path(__file__).parent.parent.parent.resolve() #TODO parentx3? Грех на душу берешь, грех
        print(self.BASE_PATH)
        self.hotkey_path = Path(self.BASE_PATH, 'hotkeys', 'hotkeys.json')
        self.graph = NodeGraph()

        self.graph.set_context_menu_from_file(self.hotkey_path, 'graph')

        self.graph.widget.resize(1100, 800)
        self.graph.register_nodes([
            BasicNodeA
        ])

        self.n_basic_a = self.graph.create_node(
            'nodes.BasicNodeA', text_color='#feab20')

    def context_menu_open_file(self):
        pass

    def get_nodes_list(self):
        pass
