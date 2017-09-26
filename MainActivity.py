# coding=utf-8

import Function
import os
import GUI_Main, GUI_EditFile, GUI_NewFile, GUI_SaveConfirm, GUI_SearchInput
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
import manifest
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


class MainForm(QtWidgets.QMainWindow, GUI_Main.Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init()

    def init(self):
        pass
        # self.Open.clicked.connect(self.openfile)
        # self.Save.clicked.connect(self.btn_open)
        # self.SaveAs.clicked.connect(self.btn_save)

    def openfile(self):
        pass
        filename = QFileDialog.getOpenFileName(self, "打开文件", manifest.DocLocation, "Txt files(*.txt)")
        # "open file Dialog "为文件对话框的标题，第三个是打开的默认路径，第四个是文件类型过滤器
        text = open(filename, 'r').read()
        GUI_EditFile.textEdit.setText(text)#可能有错!


        # #保存时调出来保存成功,别用新的form,用消息窗口
        # def msg(self):
        #     reply = QMessageBox.information(self,  # 使用infomation信息框
        #                                     "标题",
        #                                     "消息",
        #                                     QMessageBox.Yes | QMessageBox.No)
        #     http: // blog.csdn.net / zd0303 / article / details / 50261481


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec_())
