import traceback
from abc import abstractmethod
from typing import *
from Dewins.ui.NodeGraph.base.port import Port
from Dewins.ui.NodeGraph import (
    BaseNode
)
from Dewins.ui.Components.Graph.Nodes.Prototypes.CommonNodeProto import CommonNodePrototype, PortOut


class InputNodePrototype(CommonNodePrototype):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def load_data_from_output_port_for_input(self, port: PortOut) -> Optional[Any]:
        pass

    def run(self, is_run_input_node: bool = True) -> bool:
        print(f"Start process {self.name()}")

        def run_node(parent, current: Union[List, Union[InputNodePrototype, CommonNodePrototype]], is_input: bool):
            if isinstance(current, list):
                for n in current:
                    if not run_node(parent, n, False):
                        return False

            elif isinstance(current, BaseNode):
                result_run = None
                if not is_input:
                    result_run = current.run()
                    print(f"[{parent.name()}->{current.name()}] Execute node {current.name()}({current.get_data_at_inputs_ports()})")

                ### prepare inputs of executing nodes ###
                nodes = current.get_connected_outputs_nodes()
                next_execute_nodes = []
                for current_output, next_input, child_node in nodes:
                    try:
                        data = current.load_data_from_output_port_for_input(current_output)
                        child_node.put_data_at_input_port(next_input, data)
                    except:
                        traceback.print_exc()
                        print(f"At parsing output arg in Node[{current.name()}] Port[{next_input.name()}] catch a error. Is this port reader was realise?")
                        return False
                    next_execute_nodes.append(child_node)

                #TODO Is need to be classified like this a error occur in process node, or that is answer of im not ready?
                if len(next_execute_nodes) == 0:
                    print(f"Done executing at node {current.name()}[{current.get_data_at_inputs_ports()}]: next {len(next_execute_nodes)}")
                else:
                    print(f"Done run {current.name()}[{current.get_data_at_inputs_ports()}]: next {len(next_execute_nodes)}")
                if not run_node(current, next_execute_nodes, False):
                    return False
                return True

            else:
                print(f"Whata heck bro? How do you put here not a node? [parent:{parent}, current:{current}]")
                return False

            return True

        return run_node(self, self, is_input=is_run_input_node)
