from abc import abstractmethod
from typing import *

from Dewins.ui.Components.Graph.Nodes.Prototypes.CommonNodeProto import PortOut
from Dewins.ui.NodeGraph import (
    BaseNode, Port
)
from Dewins.ui.Components.Graph.Nodes.Prototypes.ProcessNodeProto import ProcessNodePrototype

from PySide6.QtWidgets import QLabel

class VisualiseNode(ProcessNodePrototype):
    __identifier__ = "Visualise"
    NODE_NAME = "Visualise Window"

    def __init__(self):
        super().__init__()
        self.add_input("Output")

    def set_visualise_label(self, label: QLabel):
        self.l = label

    def process(self) -> bool:
        data: str = str(self._data_for_process["Output"])
        self.l.setText(data)
        return True

    def load_data_from_output_port_for_input(self, port: PortOut) -> Optional[Any]:
        pass # this is an example of good code.