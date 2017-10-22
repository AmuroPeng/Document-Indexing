# coding=utf-8`

import Function
import os
import GUI_Main, GUI_EditFile, GUI_NewFile, GUI_SaveConfirm, GUI_Search_Substitute, GUI_AdvancedSearchOption, \
    GUI_EncodingResult, GUI_Top20
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QColor, QKeySequence, QSyntaxHighlighter, QTextCharFormat, QTextCursor
import sys
import manifest
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize, QMetaObject, QCoreApplication, \
    QPropertyAnimation
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QPushButton, \
    QApplication, QMainWindow


class MainForm(QtWidgets.QMainWindow, GUI_Main.Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init()

    def init(self):
        self.Open.triggered.connect(self.open_file)
        self.New.triggered.connect(self.create_file)
        # self.AdvancedSearchButton.clicked.connect(self.adv_search)
        # self..clicked.connect(self.btn_save)
        # pushbutton = QtGui.QPushButton('Popup Button')
        menu = QtWidgets.QMenu()
        menu.addAction('编码&译码   ', self.advsearch_encode)  # 不知道怎么左对齐,暂时先加空格来手动居中了_(:з」∠)_
        menu.addAction('Top 20   ', self.advsearch_Top20)
        self.AdvancedSearchButton.setMenu(menu)

    def open_file(self):
        func = Function.Edit()
        filepath = func.open_file()
        # 显示
        edit = EditForm(filepath)
        edit.show()
        edit.exec_()

    def create_file(self):
        create = NewFileForm()
        create.show()
        create.exec_()
        fname = create.textNewFile.toPlainText()
        # 检查新建文件名是否重复
        # while True:
        #     if os.path.exists(fname):
        #         print("Error:'%s' already exists" % fname)
        #         QMessageBox.information(self,  # 使用infomation信息框
        #                                 "标题",
        #                                 "消息",
        #                                 QMessageBox.Yes | QMessageBox.No)
        #         # !!!这里加入清空用户填写栏的内容,以及跳转回输入重新输入界面
        #     else:
        #         break
        print(fname)
        func = Function.Edit()
        func.new_file(fname + ".txt")
        # 显示编辑窗口
        filepath = manifest.SaveTempPos + '\\' + fname + ".txt"
        print(filepath)
        edit = EditForm(filepath)
        edit.show()
        edit.exec_()

    def adv_search(self):
        pass
        # self.setCentralWidget(pushbutton)
        # self.resize(200, 30)

    def advsearch_encode(self):
        print('MainForm >>>>> advsearch_encode')
        encode = EncodingForm()
        encode.show()
        encode.exec_()
        print('MainForm <<<<< advsearch_encode')

    def advsearch_Top20(self):
        print('MainForm >>>>> advsearch_Top20')
        top = Top20Form()
        top.show()
        top.exec_()
        print('MainForm <<<<< advsearch_Top20')

        # #保存时调出来保存成功,别用新的form,用消息窗口
        # def msg(self):
        #     reply = QMessageBox.information(self,  # 使用infomation信息框
        #                                     "标题",
        #                                     "消息",
        #                                     QMessageBox.Yes | QMessageBox.No)
        #     http: // blog.csdn.net / zd0303 / article / details / 50261481


class EditForm(QtWidgets.QDialog, GUI_EditFile.Ui_Dialog):
    def __init__(self, filepath):
        super(EditForm, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init(filepath)

    def init(self, filepath):
        print('进入EditForm')
        text = open(filepath, 'r').read()
        self.textEdit.setText(text)
        print('等待点击按钮')
        self.pushButtonClear.clicked.connect(self.clear_text)
        self.pushButtonSave.clicked.connect(lambda: self.save_text(filepath))
        # 这里加lambda是因为,不加的话,save_text后面带括号,就直接执行这个函数了!
        self.pushButtonSearch.clicked.connect(self.search_text)
        # key=self.search_text()
        # !!!!! self.pushButtonSubstitute.clicked.connect(lambda :self.substitute_text(key))
        # self.Save.clicked.connect(self.btn_open)
        # self.SaveAs.Led.connect(self.btn_save)

    def save_text(self, filepath):
        print("save")
        content = self.textEdit.toPlainText()
        # location = manifest.SaveTempPos  # 需要修改的以后
        # fname = self.MainForm.create_file()
        print("进入Fun函数")
        save = Function.Edit()
        print('文本内容为:' + content)
        save.save_file(filepath, content)

    def clear_text(self):
        self.textEdit.setText("")
        print("cleared")

    def search_text(self):
        print("进入search方法")
        search = Search_SubstituteForm(self)
        search.show()
        search.exec_()

    def substitute_text(self, key):
        text = self.textEdit.toPlainText()
        text_new = self.textEdit.toPlainText().replace(key, text)
        print('已替换' + key)


class NewFileForm(QtWidgets.QDialog, GUI_NewFile.Ui_Dialog):
    def __init__(self):
        super(NewFileForm, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init()

    def init(self):
        pass


class Search_SubstituteForm(QtWidgets.QDialog, GUI_Search_Substitute.Ui_Dialog):
    def __init__(self, editForm):
        super(Search_SubstituteForm, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init(editForm)

    def init(self, editForm):
        print("进入搜索替换Form")
        num = 0
        self.pushButton_searchNext.clicked.connect(lambda: self.search(num, editForm))
        self.pushButton_allSubstitute_2.clicked.connect(lambda: self.allSubstitute(editForm))

    def search(self, num, editform):
        print("ENTER Search_SubstituteForm-->search")
        key = self.lineEdit_searchContent.text()
        self.lineEdit_searchContent_2.setText(self.lineEdit_searchContent.text())  # 将替换栏的搜索内容和查找栏一致,便于对同一个词进行多个操作
        text = editform.textEdit.toPlainText()  # 得调用主函数建的实例,在用里面的参数
        print(key + text)
        result = Function.Edit.kmp(key, text)
        print('搜索内容:' + key + '\n结果:' + str(result))
        # Function.Display.highlight(key, result, editform)
        if key:
            cursor = editform.textEdit.textCursor()  # 光标
            # Setup the desired format for matches
            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))
            # Setup the regex engine
            # regex = QtCore.QRegExp(pattern)
            # Process the displayed document
            pos = 0
            # index = regex.indexIn(text, pos)
            while pos != len(result):
                # Select the matched text and apply the desired format
                cursor.setPosition(result[pos] - 1)  # 不懂为什么得减1,不减就错位了
                for i in range(len(key)):
                    cursor.movePosition(QtGui.QTextCursor.Right, 1)
                cursor.mergeCharFormat(format)
                pos = pos + 1
                # Move to the next match
                # pos = index + regex.matchedLength()
                # index = regex.indexIn(text, pos)
        print("CLOSE Search_SubstituteForm-->search")

    def allSubstitute(self, editform):
        print("ENTER Search_SubstituteForm-->allSubstitute")
        old = self.lineEdit_searchContent_2.text()
        self.lineEdit_searchContent.setText(self.lineEdit_searchContent_2.text())  # 同上面方法中的查找,便于多部操作搜索值
        new = self.lineEdit_substituteContent_2.text()
        text = editform.textEdit.toPlainText()
        editform.textEdit.setText(text.replace(old, new))  # text做replace之后,本身是不变的,只是传一个改变后的值而已
        print("CLOSE Search_SubstituteForm-->allSubstitute")


class AdvSearchOptForm(QtWidgets.QDialog, GUI_AdvancedSearchOption.Ui_Dialog):
    def __init__(self):
        super(AdvSearchOptForm, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init()

    def init(self):
        self.pushButtonEncoding.clicked.connect(self.encode)
        self.pushButtonTOP20.clicked.connect(self.Top20)

    def encode(self):
        encode = EncodingForm()
        encode.show()
        encode.exec_()
        print('encode exit')

    def Top20(self):
        top = Top20Form()
        top.show()
        top.exec_()


class EncodingForm(QtWidgets.QDialog, GUI_EncodingResult.Ui_Dialog):
    def __init__(self):
        super(EncodingForm, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init()

    def init(self):
        func = Function.Edit()
        filepaths = func.open_file()
        text = open(filepaths, 'r').read()
        # for k in range(0, len(filepaths[0])):
        #     # print('length=' + len(filepaths[0]))  # !!!!!!!有问题
        #     print("进入循环取text")
        #     text_temp = open(filepaths[0][k], 'r').read()
        #     text_temp += '\n\n'
        #     text += text_temp
        # print("退出循环取text")
        self.textEdit.setText(text)
        print(1)
        self.pushButtonEncode.clicked.connect(self.encoding)
        self.pushButtonDecode.clicked.connect(lambda: self.decoding(text))
        print(11)
        # self.pushButtonEncode.clicked.connect()
        # self.pushButtonDecode.clicked.connect()

    def encoding(self):
        # print(self.textEdit.toPlainText())
        self.textEdit.setText(manifest.TemtEncoding)
        # print(self.textEdit.toPlainText())
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def decoding(self, text):
        self.textEdit.setText(text)


class Top20Form(QtWidgets.QDialog, GUI_Top20.Ui_Dialog):
    def __init__(self):
        super(Top20Form, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init()

    def init(self):
        func = Function.Edit()
        filepaths = func.open_files()
        print(287)
        file_dic = {filepaths[i]: open(filepaths[i], 'r').read() for i in range(len(filepaths))}
        print(289)
        self.textBrowser.setText(str(file_dic))
        # self.textEdit.setText(filename);
        # self.pushButtonEncode.clicked.connect()
        # self.pushButtonDecode.clicked.connect()

    def count(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec_())
