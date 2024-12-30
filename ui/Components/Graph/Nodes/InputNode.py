from typing import *
from math import *

import cv2

from Dewins.ui.Components.Graph.Nodes.Prototypes.CommonNodeProto import PortOut
from Dewins.ui.Components.Graph.Nodes.Prototypes.InputNodeProto import InputNodePrototype
from Dewins.ui.NodeGraph.base.port import Port
from Dewins.backend.NodeGraph.Nodes import (
    InputBackend
)
from Dewins.ui.Components.Graph.Nodes.widgets.InputWidgets import (
    NodeWrapperTextInputWidget,
    NodeWrapperImageInputWidget
)
from Dewins.backend.file_manager import File


class TextNode(InputNodePrototype):

    __identifier__ = "Input"
    NODE_NAME = "Text Input"

    def __init__(self):
        super().__init__()
        self.add_output("Text")

        self.node_widget = NodeWrapperTextInputWidget(self.view)
        self.add_custom_widget(self.node_widget, tab='Custom')

    def load_data_from_output_port_for_input(self, port: PortOut) -> Optional[Any]:
        if port.name() == "Text":
            return self.node_widget.custom_widget.input_plain_text.toPlainText()


class ImageNode(InputNodePrototype):
    __identifier__ = "Input"
    NODE_NAME = "Image Input"

    def __init__(self):
        super().__init__()
        self.add_output("Image")

        self.node_widget = NodeWrapperImageInputWidget(self.view)
        self.add_custom_widget(self.node_widget, tab='Custom')

    def load_data_from_output_port_for_input(self, port: PortOut) -> Optional[Any]:
        if port.name() == "Image":
            return cv2.imread(self.node_widget.custom_widget.get_last_path_image())


class NumberNode(InputNodePrototype):
    __identifier__ = "Input"
    NODE_NAME = "Number Input"
    _num = 0
    def __init__(self):
        super().__init__()
        self.add_output("Number")
        self.add_text_input("Number[int,float]", '', '0', "" )

    def load_data_from_output_port_for_input(self, port: PortOut) -> Optional[Any]:
        if port.name() == "Number":
            return self.get_widget("Number[int,float]").get_value()
