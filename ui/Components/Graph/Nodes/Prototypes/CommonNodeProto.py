from abc import abstractmethod
from typing import *
from Dewins.ui.NodeGraph.base.port import Port
from Dewins.ui.NodeGraph import (
    BaseNode
)

class PortOut(Port):
    def __init__(self, node, port):
        super().__init__(node, port)

class PortIn(Port):
    def __init__(self, node, port):
        super().__init__(node, port)


class CommonNodePrototype(BaseNode):

    def __init__(self):
        super().__init__()
        self._data_for_process = {}

    _data_for_process: Dict[str, Any]

    @abstractmethod
    def load_data_from_output_port_for_input(self, port: PortOut) -> Any:
        pass

    def get_data_at_inputs_ports(self): return self._data_for_process
    def put_data_at_input_port(self, port: PortIn, data: Any):
        self._data_for_process[port.name()] = data

    def get_connected_outputs_nodes(self) -> List[Tuple[PortOut, PortIn, "CommonNodePrototype"]]:
        result = []
        for name, port in self.outputs().items():
            port = port
            for port_in in port.connected_ports():
                port_in = port_in
                result.append((port, port_in, port_in.node()))
        return result