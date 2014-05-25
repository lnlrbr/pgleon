#-*- coding:utf-8 -*-

__author__ = 'lionel'

from PyQt4 import QtGui, QtCore

from ui.widgets.qscint import QScint


class QueryPageUI(QtGui.QWidget):
    """Represent a page in the central tabwidget widget. Each page is a particular query"""
    def __init__(self, *args, **kwargs):
        super(QueryPageUI, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.uiQueryEditor = QScint(self)
        self.uiQueryResult = QtGui.QTableView(self)
        self.uiQueryMsg = QtGui.QTextEdit(self)
        self.uiStatusLabel = QtGui.QLabel(self)

        self.uiTab = QtGui.QTabWidget(self)
        self.uiTab.addTab(self.uiQueryResult, "Results")
        self.uiTab.addTab(self.uiQueryMsg, "Messages")

        uiVSplitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        uiVSplitter.addWidget(self.uiQueryEditor)
        uiVSplitter.addWidget(self.uiTab)
        uiVBox = QtGui.QVBoxLayout(self)
        uiVBox.addWidget(uiVSplitter)
        uiVBox.addWidget(self.uiStatusLabel)

        self.setLayout(uiVBox)

    def setStatus(self, status):
        self.uiStatusLabel.setText(status)


# class MainUI(QtGui.QWidget):
class MainUI(QtGui.QMainWindow):

    def __init__(self):
        super(MainUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.uiMenuBar = self.menuBar()
        # self.initMenu()

        self.uiToolBar = self.addToolBar('Execute')

        self.uiQueryBook = QtGui.QTabWidget()
        self.setCentralWidget(self.uiQueryBook)

        self.setGeometry(300, 300, 600, 400)

        self.uiStatusBar = self.statusBar()

        self.show()

    # def initMenu(self):
    #     uiExitAction = QtGui.QAction(QtGui.QIcon('icons/exit.png'), '&Exit', self)
    #     uiExitAction.setShortcut('Ctrl+Q')
    #     uiExitAction.setStatusTip('Exit application')
    #     uiExitAction.triggered.connect(QtGui.qApp.quit)
    #
    #     uiFileMenu = self.uiMenuBar.addMenu('&File')
    #     uiFileMenu.addAction(uiExitAction)

    def uiSetTitle(self, title):
        self.setWindowTitle(title)

    # def closeEvent(self, event):
    #     pass
        # settings = QtCore.QSettings("MyCompany", "MyApp")
        # settings.setValue("geometry", self.saveGeometry())
        # settings.setValue("windowState", self.saveState())
        # self.closeEvent(event)


