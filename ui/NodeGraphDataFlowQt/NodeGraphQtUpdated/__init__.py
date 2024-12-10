#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
**NodeGraphQt** is a node graph framework that can be implemented and re purposed
into applications that supports **PySide2**.

project: https://github.com/jchanvfx/NodeGraphQt
documentation: https://jchanvfx.github.io/NodeGraphQt/api/html/index.html

example code:

.. code-block:: python
    :linenos:

    from NodeGraphQt import QtWidgets, NodeGraph, BaseNode


    class MyNode(BaseNode):

        __identifier__ = 'io.github.jchanvfx'
        NODE_NAME = 'My Node'

        def __init__(self):
            super(MyNode, self).__init__()
            self.add_input('foo', color=(180, 80, 0))
            self.add_output('bar')

    if __name__ == '__main__':
        app = QtWidgets.QApplication([])
        graph = NodeGraph()

        graph.register_node(BaseNode)
        graph.register_node(BackdropNode)

        backdrop = graph.create_node('nodeGraphQt.nodes.Backdrop', name='Backdrop')
        node_a = graph.create_node('io.github.jchanvfx.MyNode', name='Node A')
        node_b = graph.create_node('io.github.jchanvfx.MyNode', name='Node B', color='#5b162f')

        node_a.set_input(0, node_b.output(0))

        viewer = graph.viewer()
        viewer.show()

        app.exec_()
"""

# node graph
from .base.graph import DUNodeGraph
from .widgets.NodeViewer import DUNodeViewer
# nodes & ports

# widgets



__version__ = 1.0
__all__ = [
    'DUNodeGraph',
    "DUNodeViewer",
]
