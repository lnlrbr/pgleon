#-*- coding:utf-8 -*-
from PyQt4 import QtGui, QtCore

__author__ = 'lionel'


class ExplorerUI(QtGui.QDockWidget):
    def __init__(self, *args, **kwargs):
        super(ExplorerUI, self).__init__(*args, **kwargs)
        self.initUI()
        self.setObjectName('Explorer Dock')
        self.setWindowTitle('Explorer Dock')

    def initUI(self):
        #toolbar
        self.uiToolBar = QtGui.QToolBar('Explorer toolbar', parent=self)
        self.uiToolBar.setIconSize(QtCore.QSize(8, 8))
        self.uiToolBar.setMovable(False)

        self.uiRefreshAction = QtGui.QAction(QtGui.QIcon('icons/refresh.png'), 'Refresh', self.uiToolBar)
        self.uiRefreshAction.setStatusTip('Refresh')
        self.uiToolBar.addAction(self.uiRefreshAction)

        self.uiExpandAction = QtGui.QAction(QtGui.QIcon('icons/expand.png'), 'Expand', self.uiToolBar)
        self.uiExpandAction.setStatusTip('Expand')
        self.uiToolBar.addAction(self.uiExpandAction)

        self.uiCollapseAction = QtGui.QAction(QtGui.QIcon('icons/collapse.png'), 'Collapse', self.uiToolBar)
        self.uiCollapseAction.setStatusTip('Collapse')
        self.uiToolBar.addAction(self.uiCollapseAction)

        self.uiExplorerTree = QtGui.QTreeView(self)
        self.setWidget(self.uiExplorerTree)