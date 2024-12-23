from abc import abstractmethod
from typing import *

from Dewins.ui.Components.Graph.Nodes.Prototypes.CommonNodeProto import PortOut
from Dewins.ui.NodeGraph import (
    BaseNode, Port
)
from Dewins.ui.Components.Graph.Nodes.Prototypes.ProcessNodeProto import ProcessNodePrototype
from Dewins.ui.Components.Graph.Nodes.widgets.ProcessWidgets import (
    NodeWrapperCountWordsNodeWidget
)

class CountWordNode(ProcessNodePrototype):
    __identifier__ = "Processor"
    NODE_NAME = "Word Counter"

    def __init__(self):
        super().__init__()
        self.add_input("Text")
        self.add_output("Int")

        self.node_widget = NodeWrapperCountWordsNodeWidget(self.view)
        self.add_custom_widget(self.node_widget, tab='Custom')

    _last_arg_int: int = 0

    def load_data_from_output_port_for_input(self, port: PortOut) -> Any:
        if port.name() == "Int":
            return self._last_arg_int

    def process(self) -> bool:
        data: str = self.get_data_at_inputs_ports()["Text"]
        self._last_arg_int = len(data.split())
        self.node_widget.custom_widget.count_words_label.setText(f"Count: {self._last_arg_int}")

        return True