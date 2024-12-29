from typing import *
from math import *

from Dewins.ui.Components.Graph.Nodes.Prototypes.CommonNodeProto import PortOut
from Dewins.ui.Components.Graph.Nodes.Prototypes.InputNodeProto import InputNodePrototype
from Dewins.ui.Components.Graph.Nodes.Prototypes.TriggerNodePrototype import TriggerNodePrototype
from Dewins.ui.NodeGraph.base.port import Port
from Qt.QtWidgets import QWidget
from Dewins.ui.Components.Graph.Nodes.widgets.TriggerWidgets import *

class OnUserClickTrigger(TriggerNodePrototype):

    def set_window_handler(self, win: QWidget):
        pass

    def tick(self):
        pass

    def run(self, is_input: bool = False) -> bool:
        pass

    __identifier__ = "Trigger"
    NODE_NAME = "On Click Trigger"

    def __init__(self):
        super().__init__()
        self.add_output("X pos")
        self.add_output("Y pos")

    def load_data_from_output_port_for_input(self, port: PortOut) -> Optional[Any]:
        if port.name() == "Text":
            return self.node_widget.custom_widget.input_plain_text.toPlainText()
