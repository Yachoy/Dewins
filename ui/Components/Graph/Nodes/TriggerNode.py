from typing import *
from math import *

import PySide6.QtGui

from Dewins.ui.Components.Graph.Nodes.Prototypes.CommonNodeProto import PortOut
from Dewins.ui.Components.Graph.Nodes.Prototypes.InputNodeProto import InputNodePrototype
from Dewins.ui.Components.Graph.Nodes.Prototypes.TriggerNodePrototype import TriggerNodePrototype
from Dewins.ui.NodeGraph.base.port import Port
from Qt.QtWidgets import QWidget
from Dewins.ui.Components.Graph.Nodes.widgets.TriggerWidgets import *
from Dewins.ui.Components.Qt.VisualiseWinWidgets import WidgetVisualise


class OnUserClickTrigger(TriggerNodePrototype):

    def set_window_handler(self, win: WidgetVisualise):
        self._vis_wid = win
        win.click_lmb_signal.connect(self.process_LMB_click_event)

    __identifier__ = "Trigger"
    NODE_NAME = "On Click Trigger"

    def __init__(self):
        self._vis_wid: WidgetVisualise = None
        super().__init__()
        self._x, self._y = 0, 0
        self.add_output("X pos")
        self.add_output("Y pos")

    def process_LMB_click_event(self, event: PySide6.QtGui.QMouseEvent):
        x, y = event.pos().x(), event.pos().y()
        width, height = self._vis_wid.get_label().pixmap().width(), self._vis_wid.get_label().pixmap().height()
        orig_width, orig_height = self._vis_wid.get_cached_pixmap().width(), self._vis_wid.get_cached_pixmap().height()
        x, y = int(x/width * orig_width), int(y/height*orig_height)
        self._run_point(x, y)

    def tick(self):
        pass

    def _run_point(self, x: int, y: int):
        self._x, self._y = x, y
        self.run(True)

    def load_data_from_output_port_for_input(self, port: PortOut) -> Optional[Any]:
        if port.name() == "X pos":
            return self._x
        elif port.name() == "Y pos":
            return self._y
