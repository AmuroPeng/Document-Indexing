# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_EditFile.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(60, 50, 271, 131))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 220, 271, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonClear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout.addWidget(self.pushButtonClear)
        self.pushButtonSave = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.pushButtonSearch = QtWidgets.QPushButton(Dialog)
        self.pushButtonSearch.setGeometry(QtCore.QRect(340, 10, 41, 31))
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.pushButtonSubstitute = QtWidgets.QPushButton(Dialog)
        self.pushButtonSubstitute.setGeometry(QtCore.QRect(340, 60, 41, 31))
        self.pushButtonSubstitute.setObjectName("pushButtonSubstitute")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonClear.setText(_translate("Dialog", "清空"))
        self.pushButtonSave.setText(_translate("Dialog", "保存"))
        self.pushButtonSearch.setText(_translate("Dialog", "🔍"))
        self.pushButtonSubstitute.setText(_translate("Dialog", "替换"))

