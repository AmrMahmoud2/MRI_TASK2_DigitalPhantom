# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MRI-Phantom22.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1071, 621))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 0, 591, 587))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cb = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cb.setObjectName("cb")
        self.cb.addItem("")
        self.cb.addItem("")
        self.gridLayout_2.addWidget(self.cb, 0, 0, 1, 1)
        self.cb2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cb2.setObjectName("cb2")
        self.cb2.addItem("")
        self.gridLayout_2.addWidget(self.cb2, 1, 0, 1, 1)
        self.edit1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit1.sizePolicy().hasHeightForWidth())
        self.edit1.setSizePolicy(sizePolicy)
        self.edit1.setObjectName("edit1")
        self.gridLayout_2.addWidget(self.edit1, 2, 0, 1, 1)
        self.edit2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit2.sizePolicy().hasHeightForWidth())
        self.edit2.setSizePolicy(sizePolicy)
        self.edit2.setObjectName("edit2")
        self.gridLayout_2.addWidget(self.edit2, 3, 0, 1, 1)
        self.edit3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit3.sizePolicy().hasHeightForWidth())
        self.edit3.setSizePolicy(sizePolicy)
        self.edit3.setObjectName("edit3")
        self.gridLayout_2.addWidget(self.edit3, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 500, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 500, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 500, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(20, 500, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.l1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l1.setMouseTracking(True)
        self.l1.setTabletTracking(True)
        self.l1.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.l1.setAcceptDrops(True)
        self.l1.setFrameShape(QtWidgets.QFrame.Box)
        self.l1.setObjectName("l1")
        self.gridLayout_8.addWidget(self.l1, 0, 0, 1, 1)
        self.l3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l3.setFrameShape(QtWidgets.QFrame.Box)
        self.l3.setObjectName("l3")
        self.gridLayout_8.addWidget(self.l3, 2, 0, 1, 1)
        self.l2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l2.setFrameShape(QtWidgets.QFrame.Box)
        self.l2.setObjectName("l2")
        self.gridLayout_8.addWidget(self.l2, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 611, 551))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphicsView_4 = PlotWidget(self.gridLayoutWidget_2)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout_3.addWidget(self.graphicsView_4, 2, 2, 1, 1)
        self.graphicsView_3 = PlotWidget(self.gridLayoutWidget_2)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout_3.addWidget(self.graphicsView_3, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 1, 1, 1)
        self.graphicsView = PlotWidget(self.gridLayoutWidget_2)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.graphicsView_2 = PlotWidget(self.gridLayoutWidget_2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout_3.addWidget(self.graphicsView_2, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem6, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cb.setItemText(0, _translate("MainWindow", "Select Phantom"))
        self.cb.setItemText(1, _translate("MainWindow", "Shepp-Logan phantom"))
        self.cb2.setItemText(0, _translate("MainWindow", "Select Time"))
        self.edit1.setText(_translate("MainWindow", "Theta"))
        self.edit2.setText(_translate("MainWindow", "TR"))
        self.edit3.setText(_translate("MainWindow", "TE"))
        self.lineEdit_2.setText(_translate("MainWindow", "Phantom"))
        self.lineEdit_3.setText(_translate("MainWindow", "T1 IMAGE"))
        self.lineEdit.setText(_translate("MainWindow", "T2 IMAGE"))
        self.l1.setText(_translate("MainWindow", "TextLabel"))
        self.l3.setText(_translate("MainWindow", "TextLabel"))
        self.l2.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Tab1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


from pyqtgraph import PlotWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# class Label(QtWidgets.QLabel):
#     def __init__(self, parent):
#         super(Label, self).__init__(parent=parent)
#
#     def paintEvent(self, event):
#         super().paintEvent(event)
#         qp = QtGui.QPainter(self)
#         print("hello")
#         col = QColor(0, 0, 0)
#         col.setNamedColor('#d4d4d4')
#         qp.setPen(col)
#
#         qp.setBrush(QColor(255, 0, 0))
#         qp.drawRect(450,50,90,60)



    # def drawRectangles(self, qp):
    #     col = QColor(0, 0, 0)
    #     col.setNamedColor('#d4d4d4')
    #     qp.setPen(col)
    #
    #     qp.setBrush(QColor(255, 0, 0))
    #     qp.drawRect(150, 50, 90, 60)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
