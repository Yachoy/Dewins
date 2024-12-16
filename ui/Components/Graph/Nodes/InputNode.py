from abc import abstractmethod


from Dewins.ui.NodeGraph import (
    BaseNode
)

from Dewins.backend.NodeGraph.Nodes import (
    InputBackend
)


class InputNodePrototype(BaseNode):
    _backend: InputBackend.InputBackend

    def __init__(self, backend):
        super().__init__()
        self._backend = backend


class TextInputNode(InputNodePrototype):
    pass

class ImageInputNode(InputNodePrototype):
    pass