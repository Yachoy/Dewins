from abc import abstractmethod
from typing import *

import Qt.QtWidgets

from Dewins.ui.NodeGraph import (
    BaseNode, Port
)
from Dewins.ui.Components.Graph.Nodes.widgets.TriggerWidgets import NodeWrapperTriggerNodeWidget
from Dewins.ui.Components.Graph.Nodes.InputNode import InputNodePrototype, PortOut
from Qt import QtCore

class TriggerNodePrototype(InputNodePrototype):
    __identifier__ = "Trigger"
    trigger_execute = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.custom_widget = NodeWrapperTriggerNodeWidget(self.view)
        self.add_custom_widget(self.custom_widget, tab='Custom')

    @abstractmethod
    def tick(self): raise NotImplementedError

    @abstractmethod
    def set_window_handler(self, win: Qt.QtWidgets.QWidget): raise NotImplementedError
