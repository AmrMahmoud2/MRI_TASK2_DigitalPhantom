# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MRI-Phantom.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.b1 = QtWidgets.QPushButton(Dialog)
        self.b1.setGeometry(QtCore.QRect(100, 280, 89, 25))
        self.b1.setObjectName("b1")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 30, 241, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.l1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l1.setMinimumSize(QtCore.QSize(128, 128))
        self.l1.setMaximumSize(QtCore.QSize(1080, 1080))
        self.l1.setText("")
        self.l1.setObjectName("l1")
        self.gridLayout.addWidget(self.l1, 0, 0, 1, 1)
        self.cb = QtWidgets.QComboBox(Dialog)
        self.cb.setGeometry(QtCore.QRect(360, 260, 211, 41))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        self.cb.setFont(font)
        self.cb.setEditable(False)
        self.cb.setCurrentText("")
        self.cb.setObjectName("cb")
        self.cb.addItem("")
        self.cb.addItem("")
        self.cb.addItem("")
        self.cb.addItem("")
        self.cb.addItem("")
        self.cb.addItem("")
        self.cb.addItem("")
        self.cb.addItem("")
        self.cb.addItem("")
        self.cb.setItemText(8, "")

        self.retranslateUi(Dialog)
        self.cb.setCurrentIndex(8)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.cb.activated['QString'].connect(self.l1.show)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.b1.setText(_translate("Dialog", "Browse"))
        self.cb.setItemText(0, _translate("Dialog", "Shepp-Logan phantom"))
        self.cb.setItemText(1, _translate("Dialog", "Piecewise-Smooth Shepp-Logan phantom"))
        self.cb.setItemText(2, _translate("Dialog", "Defrise phantom with vertical ellipses"))
        self.cb.setItemText(3, _translate("Dialog", "\'QRM\' phantom (ellipses)"))
        self.cb.setItemText(4, _translate("Dialog", "1 cone"))
        self.cb.setItemText(5, _translate("Dialog", "1 rectangular"))
        self.cb.setItemText(6, _translate("Dialog", "composite"))
        self.cb.setItemText(7, _translate("Dialog", "composite of 6 gaussians + 1 parabola"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
