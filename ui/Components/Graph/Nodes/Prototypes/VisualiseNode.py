from abc import abstractmethod
from typing import *

from Dewins.ui.Components.Graph.Nodes.Prototypes.CommonNodeProto import PortOut
from Dewins.ui.NodeGraph import (
    BaseNode, Port
)
from Dewins.ui.Components.Graph.Nodes.Prototypes.ProcessNodeProto import ProcessNodePrototype
from Dewins.ui.Components.Qt.VisualiseWinWidgets import WidgetVisualise

from PySide6.QtWidgets import QLabel


class VisualiseNode(ProcessNodePrototype):
    __identifier__ = "Visualise"
    NODE_NAME = "Visualise Window"

    def __init__(self):
        super().__init__()
        self.add_input("Output")
        self._vis_widget: WidgetVisualise = None

    def set_visualise_widget(self, vis: WidgetVisualise):
        self._vis_widget = vis

    def process(self) -> bool:
        data: str = self._data_for_process["Output"]
        self._vis_widget.update_data(data)
        return True

    def load_data_from_output_port_for_input(self, port: PortOut) -> Optional[Any]:
        pass # this is an example of good code.