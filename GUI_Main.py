# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMainWindow
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 100, 519, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SearchText = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchText.sizePolicy().hasHeightForWidth())
        self.SearchText.setSizePolicy(sizePolicy)
        self.SearchText.setMinimumSize(QtCore.QSize(347, 0))
        self.SearchText.setObjectName("SearchText")
        self.horizontalLayout.addWidget(self.SearchText)
        self.SearchButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SearchButton.setObjectName("SearchButton")
        self.horizontalLayout.addWidget(self.SearchButton)
        self.AdvancedSearchButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.AdvancedSearchButton.setObjectName("AdvancedSearchButton")
        self.horizontalLayout.addWidget(self.AdvancedSearchButton)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 240, 571, 301))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 23))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_view = QtWidgets.QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        self.menu_settings = QtWidgets.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Open = QtWidgets.QAction(MainWindow)
        self.Open.setObjectName("Open")
        self.Save = QtWidgets.QAction(MainWindow)
        self.Save.setObjectName("Save")
        self.SaveAs = QtWidgets.QAction(MainWindow)
        self.SaveAs.setObjectName("SaveAs")
        self.Close = QtWidgets.QAction(MainWindow)
        self.Close.setObjectName("Close")
        self.Quit = QtWidgets.QAction(MainWindow)
        self.Quit.setObjectName("Quit")
        self.preference = QtWidgets.QAction(MainWindow)
        self.preference.setObjectName("preference")
        self.language = QtWidgets.QAction(MainWindow)
        self.language.setObjectName("language")
        self.instructions = QtWidgets.QAction(MainWindow)
        self.instructions.setObjectName("instructions")
        self.info = QtWidgets.QAction(MainWindow)
        self.info.setObjectName("info")
        self.New = QtWidgets.QAction(MainWindow)
        self.New.setObjectName("New")
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.New)
        self.menu_file.addAction(self.Open)
        self.menu_file.addAction(self.Save)
        self.menu_file.addAction(self.SaveAs)
        self.menu_file.addAction(self.Close)
        self.menu_file.addAction(self.Quit)
        self.menu_settings.addAction(self.preference)
        self.menu_settings.addAction(self.language)
        self.menu_help.addAction(self.instructions)
        self.menu_help.addAction(self.info)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SearchButton.setText(_translate("MainWindow", "搜索"))
        self.AdvancedSearchButton.setText(_translate("MainWindow", "高级搜索"))
        self.menu_file.setTitle(_translate("MainWindow", "文件"))
        self.menu_view.setTitle(_translate("MainWindow", "查看"))
        self.menu_settings.setTitle(_translate("MainWindow", "设置"))
        self.menu_help.setTitle(_translate("MainWindow", "帮助"))
        self.Open.setText(_translate("MainWindow", "打开"))
        self.Save.setText(_translate("MainWindow", "保存"))
        self.SaveAs.setText(_translate("MainWindow", "另存为"))
        self.Close.setText(_translate("MainWindow", "关闭"))
        self.Quit.setText(_translate("MainWindow", "退出"))
        self.preference.setText(_translate("MainWindow", "首选项"))
        self.language.setText(_translate("MainWindow", "语言"))
        self.instructions.setText(_translate("MainWindow", "使用说明"))
        self.info.setText(_translate("MainWindow", "关于"))
        self.New.setText(_translate("MainWindow", "新建"))


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = OpenFile()
#     ex.show()
#     sys.exit(app.exec_())
