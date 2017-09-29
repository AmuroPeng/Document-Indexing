# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_AdvancedSearchOption.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 100, 160, 83))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutOption = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutOption.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutOption.setObjectName("verticalLayoutOption")
        self.pushButtonEncoding = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonEncoding.setObjectName("pushButtonEncoding")
        self.verticalLayoutOption.addWidget(self.pushButtonEncoding)
        self.pushButtonTOP20 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonTOP20.setObjectName("pushButtonTOP20")
        self.verticalLayoutOption.addWidget(self.pushButtonTOP20)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonEncoding.setText(_translate("Dialog", "字符编码"))
        self.pushButtonTOP20.setText(_translate("Dialog", "TOP20"))

