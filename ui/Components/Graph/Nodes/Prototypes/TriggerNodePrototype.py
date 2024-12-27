from abc import abstractmethod
from typing import *

from Dewins.ui.NodeGraph import (
    BaseNode, Port
)
from Dewins.ui.Components.Graph.Nodes.InputNode import InputNodePrototype, PortOut
from Qt import QtCore

class TriggerNodePrototype(InputNodePrototype):
    __identifier__ = "Trigger"
    trigger_execute = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.trigger_execute.connect(self.run)

    @abstractmethod
    def run(self, is_input: bool = False) -> bool: raise NotImplementedError
