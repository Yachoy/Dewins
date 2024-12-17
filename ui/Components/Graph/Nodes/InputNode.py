from abc import abstractmethod
from typing import *

from Dewins.ui.Components.Graph.Nodes.ProcessNode import ProcessNodePrototype
from Dewins.ui.NodeGraph.base.port import Port
from Dewins.ui.NodeGraph import (
    BaseNode
)

from Dewins.backend.NodeGraph.Nodes import (
    InputBackend
)

from Dewins.ui.Components.Graph.Nodes.widgets.InputWidgets import (
    NodeWrapperTextInputWidget,
    NodeWrapperImageInputWidget
)


class InputNodePrototype(BaseNode):
    _backend: InputBackend.InputBackend

    def __init__(self, backend):
        super().__init__()
        self._backend = backend

    @property
    def backend(self):
        return self._backend

    @abstractmethod
    def load_data_to_port(self, port: Port) -> Any:
        pass

    def run(self):
        for name, p in self.outputs().items():
            for port_where_accept_data in p.connected_ports():
                port_where_accept_data: Port = port_where_accept_data
                node: ProcessNodePrototype = port_where_accept_data.node() #TODO Or ProcessNodePrototype or VisualizeNodePrototype, in future need to handle
                # if isinstance(node, ProcessNodePrototype):
                # elif isinstance(node, VisualizeNodePrototype):
                node.put_data_at_port(
                    port_where_accept_data, self.load_data_to_port(p)
                )
                if node.is_can_be_processed(): # if all data already node have - execute
                    if not node.process(): # process him
                        raise Exception("IDK why you return False in process, but you crash your app")
                    process = node.get_next_process() #get next node process funcion
                    process()

class TextInputNode(InputNodePrototype):

    __identifier__ = "Input"
    NODE_NAME = "Text Input"

    def __init__(self):
        super().__init__(InputBackend.TextInputBackend())
        self.add_output("Text")

        self.node_widget = NodeWrapperTextInputWidget(self.view)
        self.add_custom_widget(self.node_widget, tab='Custom')

    def load_data_to_port(self, port: Port):
        if port.name() == "Text":
            return self.node_widget.custom_widget.input_plain_text.toPlainText()

class ImageInputNode(InputNodePrototype):
    __identifier__ = "Input"
    NODE_NAME = "Image Input"

    def __init__(self):
        super().__init__(InputBackend.ImageInputBackend())
        self.add_output("Image")

        node_widget = NodeWrapperImageInputWidget(self.view)
        self.add_custom_widget(node_widget, tab='Custom')
    def load_data_to_port(self, port: Port):
        pass