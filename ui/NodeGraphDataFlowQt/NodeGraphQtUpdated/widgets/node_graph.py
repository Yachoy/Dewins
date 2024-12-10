from Qt import QtWidgets, QtGui

from NodeGraphQt.constants import (
    NodeEnum, ViewerEnum, ViewerNavEnum
)

from NodeGraphQt.widgets.viewer_nav import NodeNavigationWidget
from NodeGraphQt.widgets.node_graph import SubGraphWidget
from Qt import QtWidgets, QtCore, QtGui

from NodeGraphQt.constants import NodeEnum, ViewerNavEnum

from NodeGraphQt.widgets.viewer_nav import NodeNavigationDelagate


class DUSubGraphWidget(QtWidgets.QWidget):

    def __init__(self, parent=None, graph=None):
        super(DUSubGraphWidget, self).__init__(parent)
        self._graph = graph
        self._navigator = DUNodeNavigationWidget()
        self._layout = QtWidgets.QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(1)
        self._layout.addWidget(self._navigator)

        self._viewer_widgets = {}
        self._viewer_current = None

    @property
    def navigator(self):
        return self._navigator

    def add_viewer(self, viewer, name, node_id):
        if viewer in self._viewer_widgets:
            return

        if self._viewer_current:
            self.hide_viewer(self._viewer_current)

        self._navigator.add_label_item(name, node_id)
        self._layout.addWidget(viewer)
        self._viewer_widgets[viewer] = node_id
        self._viewer_current = viewer
        self._viewer_current.show()

    def remove_viewer(self, viewer=None):
        if viewer is None and self._viewer_current:
            viewer = self._viewer_current
        node_id = self._viewer_widgets.pop(viewer)
        self._navigator.remove_label_item(node_id)
        self._layout.removeWidget(viewer)
        viewer.deleteLater()

    def hide_viewer(self, viewer):
        self._layout.removeWidget(viewer)
        viewer.hide()

    def show_viewer(self, viewer):
        if viewer == self._viewer_current:
            self._viewer_current.show()
            return
        if viewer in self._viewer_widgets:
            if self._viewer_current:
                self.hide_viewer(self._viewer_current)
            self._layout.addWidget(viewer)
            self._viewer_current = viewer
            self._viewer_current.show()


class DUNodeNavigationWidget(QtWidgets.QListView):

    navigation_changed = QtCore.Signal(str, list)

    def __init__(self, parent=None):
        super(DUNodeNavigationWidget, self).__init__(parent)
        self.setSelectionMode(QtWidgets.QListWidget.SingleSelection)
        self.setResizeMode(QtWidgets.QListWidget.Adjust)
        self.setViewMode(QtWidgets.QListWidget.ListMode)
        self.setFlow(QtWidgets.QListWidget.LeftToRight)
        self.setDragEnabled(False)
        self.setMinimumHeight(20)
        self.setMaximumHeight(36)
        self.setSpacing(0)

        # self.viewport().setAutoFillBackground(False)
        self.setStyleSheet(
            'QListView {{border: 0px;background-color: rgb({0},{1},{2});}}'
            .format(*ViewerNavEnum.BACKGROUND_COLOR.value)
        )

        self.setItemDelegate(NodeNavigationDelagate(self))
        self.setModel(QtGui.QStandardItemModel())

    def keyPressEvent(self, event):
        event.ignore()

    def mouseReleaseEvent(self, event):
        super(DUNodeNavigationWidget, self).mouseReleaseEvent(event)
        if not self.selectedIndexes():
            return
        index = self.selectedIndexes()[0]
        rows = reversed(range(1, self.model().rowCount()))
        if index.row() == 0:
            rows = [r for r in rows if r > 0]
        else:
            rows = [r for r in rows if index.row() < r]
        if not rows:
            return
        rm_node_ids = [self.model().item(r, 0).toolTip() for r in rows]
        node_id = self.model().item(index.row(), 0).toolTip()
        [self.model().removeRow(r) for r in rows]
        self.navigation_changed.emit(node_id, rm_node_ids)

    def clear(self):
        self.model().sourceMode().clear()

    def add_label_item(self, label, node_id):
        item = QtGui.QStandardItem(label)
        item.setToolTip(node_id)
        metrics = QtGui.QFontMetrics(item.font())
        if hasattr(metrics, 'horizontalAdvance'):
            width = metrics.horizontalAdvance(item.text())
        else:
            width = metrics.width(item.text())
        width *= 1.5
        item.setSizeHint(QtCore.QSize(width, 20))
        self.model().appendRow(item)
        self.selectionModel().setCurrentIndex(
            self.model().indexFromItem(item),
            QtCore.QItemSelectionModel.ClearAndSelect)

    def update_label_item(self, label, node_id):
        rows = reversed(range(self.model().rowCount()))
        for r in rows:
            item = self.model().item(r, 0)
            if item.toolTip() == node_id:
                item.setText(label)

    def remove_label_item(self, node_id):
        rows = reversed(range(1, self.model().rowCount()))
        node_ids = [self.model().item(r, 0).toolTip() for r in rows]
        if node_id not in node_ids:
            return
        index = node_ids.index(node_id)
        if index == 0:
            rows = [r for r in rows if r > 0]
        else:
            rows = [r for r in rows if index < r]
        [self.model().removeRow(r) for r in rows]
