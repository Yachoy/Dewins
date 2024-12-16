from abc import abstractmethod


from Dewins.ui.NodeGraph import (
    BaseNode
)

from Dewins.backend.NodeGraph.Nodes import (
    InputBackend
)

from Dewins.ui.Components.Graph.Nodes.widgets.InputWidgets import NodeWrapperTextInputWidget, \
    NodeWrapperImageInputWidget


class InputNodePrototype(BaseNode):
    _backend: InputBackend.InputBackend

    def __init__(self, backend):
        super().__init__()
        self._backend = backend

    @property
    def backend(self):
        return self._backend

    @abstractmethod
    def run(self): ...


class TextInputNode(InputNodePrototype):

    __identifier__ = "Input"
    NODE_NAME = "Text Input"

    def __init__(self):
        super().__init__(InputBackend.TextInputBackend())
        self.add_output("Image")

        node_widget = NodeWrapperTextInputWidget(self.view)
        self.add_custom_widget(node_widget, tab='Custom')

    def run(self):
        pass

class ImageInputNode(InputNodePrototype):
    __identifier__ = "Input"
    NODE_NAME = "Image Input"

    def __init__(self):
        super().__init__(InputBackend.ImageInputBackend())
        self.add_output("Image")

        node_widget = NodeWrapperImageInputWidget(self.view)

        self.add_custom_widget(node_widget, tab='Custom')

    def run(self):
        pass
