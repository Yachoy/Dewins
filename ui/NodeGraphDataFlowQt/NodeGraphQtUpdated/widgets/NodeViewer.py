import math
from distutils.version import LooseVersion

from Qt import QtGui, QtCore, QtWidgets

from NodeGraphQt.base.menu import BaseMenu
from NodeGraphQt.constants import (
    LayoutDirectionEnum,
    PortTypeEnum,
    PipeEnum,
    PipeLayoutEnum,
    ViewerEnum,
    Z_VAL_PIPE,
)
from NodeGraphQt.qgraphics.node_abstract import AbstractNodeItem
from NodeGraphQt.qgraphics.node_backdrop import BackdropNodeItem
from NodeGraphQt.qgraphics.pipe import PipeItem, LivePipeItem
from NodeGraphQt.qgraphics.port import PortItem
from NodeGraphQt.qgraphics.slicer import SlicerPipeItem
from NodeGraphQt.widgets.dialogs import BaseDialog, FileDialog
from NodeGraphQt.widgets.scene import NodeScene
from NodeGraphQt.widgets.tab_search import TabSearchMenuWidget

from NodeGraphQt.widgets.viewer import NodeViewer


class DUNodeViewer(NodeViewer):
    def __init__(self, undo_stack=None):
        super().__init__(undo_stack=undo_stack)

    def mouseMoveEvent(self, event):
        if self.ALT_state and self.SHIFT_state:
            if self.pipe_slicing:
                if self.LMB_state and self._SLICER_PIPE.isVisible():
                    p1 = self._SLICER_PIPE.path().pointAtPercent(0)
                    p2 = self.mapToScene(self._previous_pos)
                    self._SLICER_PIPE.draw_path(p1, p2)
                    self._SLICER_PIPE.show()
            self._previous_pos = event.pos()
            super(NodeViewer, self).mouseMoveEvent(event)
            return

        if self.MMB_state and self.ALT_state:
            pos_x = (event.x() - self._previous_pos.x())
            zoom = 0.1 if pos_x > 0 else -0.1
            self._set_viewer_zoom(zoom, 0.05, pos=event.pos())
        elif self.MMB_state or (self.LMB_state and self.ALT_state):
            previous_pos = self.mapToScene(self._previous_pos)
            current_pos = self.mapToScene(event.pos())
            delta = previous_pos - current_pos
            self._set_viewer_pan(delta.x(), delta.y())

        if not self.ALT_state:
            if self.SHIFT_state or self.CTRL_state:
                if not self._LIVE_PIPE.isVisible():
                    self._cursor_text.setPos(self.mapToScene(event.pos()))

        if self.LMB_state and self._rubber_band.isActive:
            rect = QtCore.QRect(self._origin_pos, event.pos()).normalized()
            # if the rubber band is too small, do not show it.
            if max(rect.width(), rect.height()) > 5:
                if not self._rubber_band.isVisible():
                    self._rubber_band.show()
                map_rect = self.mapToScene(rect).boundingRect()
                path = QtGui.QPainterPath()
                path.addRect(map_rect)
                self._rubber_band.setGeometry(rect)
                self.scene().setSelectionArea(
                    path
                )
                self.scene().update(map_rect)

                if self.SHIFT_state or self.CTRL_state:
                    nodes, pipes = self.selected_items()

                    for node in self._prev_selection_nodes:
                        node.selected = True

                    if self.CTRL_state:
                        for pipe in pipes:
                            pipe.setSelected(False)
                        for node in nodes:
                            node.selected = False

        elif self.LMB_state:
            self.COLLIDING_state = False
            nodes, pipes = self.selected_items()
            if len(nodes) == 1:
                node = nodes[0]
                [p.setSelected(False) for p in pipes]

                if self.pipe_collision:
                    colliding_pipes = [
                        i for i in node.collidingItems()
                        if isinstance(i, PipeItem) and i.isVisible()
                    ]
                    for pipe in colliding_pipes:
                        if not pipe.input_port:
                            continue
                        port_node_check = all([
                            not pipe.input_port.node is node,
                            not pipe.output_port.node is node
                        ])
                        if port_node_check:
                            pipe.setSelected(True)
                            self.COLLIDING_state = True
                            break

        self._previous_pos = event.pos()
        super(NodeViewer, self).mouseMoveEvent(event)
