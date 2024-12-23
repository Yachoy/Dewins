from abc import abstractmethod
from typing import *

from Dewins.ui.NodeGraph import (
    BaseNode, Port
)
from Dewins.ui.Components.Graph.Nodes.InputNode import InputNodePrototype

class ProcessNodePrototype(InputNodePrototype):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def process(self) -> bool:
        ...

    def run(self, is_run_input_node: bool = False) -> bool:
        if self.is_can_be_processed():  # if all data already node have - execute
            if not self.process():  # process him
                raise Exception(f"{self.name(), self._data_for_process}. IDK why you return False in process, but you crash your app")
            return True
        return False

    def is_can_be_processed(self) -> bool:
        data = self.get_data_at_inputs_ports()
        for name, p in self.inputs().items():
            if data.get(name, None) is None:
                return False
        return True
