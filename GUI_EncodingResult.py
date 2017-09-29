# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_EncodingResult.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 20, 291, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonEncode = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonEncode.setObjectName("pushButtonEncode")
        self.horizontalLayout.addWidget(self.pushButtonEncode)
        self.pushButtonDecode = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonDecode.setObjectName("pushButtonDecode")
        self.horizontalLayout.addWidget(self.pushButtonDecode)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(50, 80, 291, 191))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonEncode.setText(_translate("Dialog", "编码"))
        self.pushButtonDecode.setText(_translate("Dialog", "译码"))

