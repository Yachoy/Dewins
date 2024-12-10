from NodeGraphQt import NodeGraph, SubGraph
from Dewins.ui.NodeGraphDataFlowQt.NodeGraphQtUpdated.widgets.node_graph import DUSubGraphWidget
import copy
from NodeGraphQt.nodes.group_node import GroupNode


class DUNodeGraph(NodeGraph):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

    def toggle_node_search(self):
        self._viewer.tab_search_set_nodes(self._node_factory.names)
        self._viewer.tab_search_toggle()

    def expand_group_node(self, node):
        """
        Expands a group node session in a new tab.

        Args:
            node (NodeGraphQt.GroupNode): group node.

        Returns:
            SubGraph: sub node graph used to manage the group node session.
        """
        if not isinstance(node, GroupNode):
            return
        if self._widget is None:
            raise RuntimeError('NodeGraph.widget not initialized!')

        self.viewer().clear_key_state()
        self.viewer().clearFocus()

        if node.id in self._sub_graphs:
            sub_graph = self._sub_graphs[node.id]
            tab_index = self._widget.indexOf(sub_graph.widget)
            self._widget.setCurrentIndex(tab_index)
            return sub_graph

        # build new sub graph.
        node_factory = copy.deepcopy(self.node_factory)
        layout_direction = self.layout_direction()
        kwargs = {
            'layout_direction': self.layout_direction(),
            'pipe_style': self.pipe_style(),
        }
        sub_graph = DUSubGraph(self,
                             node=node,
                             node_factory=node_factory,
                             **kwargs)

        # populate the sub graph.
        session = node.get_sub_graph_session()
        sub_graph.deserialize_session(session)

        # store reference to expanded.
        self._sub_graphs[node.id] = sub_graph

        # open new tab at root level.
        self.widget.add_viewer(sub_graph.widget, node.name(), node.id)

        return sub_graph


class DUSubGraph(SubGraph):
    def __init__(self, parent=None, node=None, node_factory=None, **kwargs):
        super().__init__(parent=parent, node=node, node_factory=node_factory, **kwargs)

    @property
    def widget(self):
        """
        The sub graph widget from the top most sub graph.

        Returns:
            SubGraphWidget: node graph widget.
        """
        if self.parent_graph.is_root:
            if self._widget is None:
                self._widget = DUSubGraphWidget()
                self._widget.add_viewer(self.subviewer_widget,
                                        self.node.name(),
                                        self.node.id)
                # connect the navigator widget signals.
                navigator = self._widget.navigator
                navigator.navigation_changed.connect(
                    self._on_navigation_changed
                )
            return self._widget
        return self.parent_graph.widget