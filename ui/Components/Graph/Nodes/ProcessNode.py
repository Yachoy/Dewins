from abc import abstractmethod
from typing import *

from Dewins.ui.NodeGraph import (
    BaseNode, Port
)
from Dewins.ui.Components.Graph.Nodes.widgets.ProcessWidgets import (
    NodeWrapperCountWordsNodeWidget
)

class ProcessNodePrototype(BaseNode):
    def __init__(self):
        super().__init__()
        self._data_for_process = {}

    _data_for_process: Dict[str, Any]

    def is_can_be_processed(self) -> bool:
        for name, p in self.inputs().items():
            if self._data_for_process.get(name, None) is None:
                return False
        return True

    def put_data_at_port(self, port: Port, data: Any):
        self._data_for_process[port.name()] = data

    @abstractmethod
    def process(self) -> bool: ...

    def get_next_process(self) -> Callable[[], bool]:
        pass

class CountWordNode(ProcessNodePrototype):
    def process(self) -> bool:
        data: str = self._data_for_process["Text"]
        self.node_widget.custom_widget.count_words_label.setText(f"Count: {len(data.split())}")

        return True

    __identifier__ = "Processor"
    NODE_NAME = "Word Counter"

    def __init__(self):
        super().__init__()
        self.add_input("Text")
        self.add_output("Int")

        self.node_widget = NodeWrapperCountWordsNodeWidget(self.view)
        self.add_custom_widget(self.node_widget, tab='Custom')



