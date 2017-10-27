# -*- coding:utf-8 -*-

import Function, Huffman
import os
import time
import GUI_Main, GUI_EditFile, GUI_NewFile, GUI_SaveConfirm, GUI_Search_Substitute, GUI_AdvancedSearchOption, \
    GUI_Encoding, GUI_Top20
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QColor, QKeySequence, QSyntaxHighlighter, QTextCharFormat, QTextCursor
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QTableWidget, QHBoxLayout, QTableWidgetItem, QComboBox, \
    QFrame
from PyQt5.QtGui import QFont, QColor, QBrush, QPixmap
import time
import re
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
    QApplication, QMainWindow, QTableWidget


class MainForm(QtWidgets.QMainWindow, GUI_Main.Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init()

    def init(self):
        self.Open.triggered.connect(self.open_file)
        self.New.triggered.connect(self.create_file)
        self.SearchButton.clicked.connect(self.adv_search)
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
        # pass
        _func_edit = Function.Edit()
        filepaths = _func_edit.open_files()
        file_dic = {filepaths[i]: open(filepaths[i], 'r').read() for i in range(len(filepaths))}
        print('时间:', time.strftime("%H%M%S"))
        word_dic = {}
        for k, v in file_dic.items():
            v = re.sub(r'[.?!,""></]', ' ', v)
            for word in v.split(' '):  # 省的实例化split之后的list了,这个好厉害_(:з」∠)_
                if word == '':
                    continue
                else:
                    if word not in word_dic.keys():
                        word_dic[word] = {}
                    kmp_list = Function.Calculate.kmp(word, v)
                    word_dic[word][k] = kmp_list  # 这样可以让dict的value是list么?答:应该是可以_(:з」∠)_
        print('word_dic', str(word_dic))
        print('时间:', time.strftime("%H%M%S"))

    def advsearch_encode(self):
        print('MainForm >>>>> advsearch_encode')
        encode = EncodingForm()
        encode.show()
        encode.exec_()
        print('MainForm <<<<< advsearch_encode')

    def advsearch_Top20(self):
        print('MainForm >>>>> Top20Form')
        top = Top20Form()
        top.show()
        top.exec_()
        print('MainForm <<<<< Top20Form')

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
        result = Function.Calculate.kmp(key, text)
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


# class AdvSearchOptForm(QtWidgets.QDialog, GUI_AdvancedSearchOption.Ui_Dialog):
#     def __init__(self):
#         super(AdvSearchOptForm, self).__init__()
#         self.setupUi(self)
#         self.retranslateUi(self)
#         self.init()
#
#     def init(self):
#         self.pushButtonEncoding.clicked.connect(self.encode)
#         self.pushButtonTOP20.clicked.connect(self.Top20)
#
#     def encode(self):
#         encode = EncodingForm()
#         encode.show()
#         encode.exec_()
#         print('encode exit')
#
#     def Top20(self):
#         print('MainForm >>>>> Top20Form')
#         top = Top20Form()
#         top.show()
#         top.exec_()
#         print('MainForm <<<<< Top20Form')


class EncodingForm(QtWidgets.QDialog, GUI_Encoding.Ui_Dialog):
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
        self.pushButtonEncode.clicked.connect(lambda: self.encoding(text))
        self.pushButtonDecode.clicked.connect(self.decoding)
        # self.pushButtonEncode.clicked.connect()
        # self.pushButtonDecode.clicked.connect()

    def encoding(self, text):
        print('EncodingForm >>>>> encoding')
        print(text)
        _func_cal = Function.Calculate()
        list_sorted = _func_cal.frequency_to_char(text)
        nodes = Function.createNodes([item[1] for item in list_sorted])
        print([item[1] for item in list_sorted])
        root = Function.createHuffmanTree(nodes)
        huff_code = Function.huffmanEncoding(nodes, root)
        self.tableWidget.setRowCount(len(list_sorted))
        for i in range(len(list_sorted)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(list_sorted[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(list_sorted[i][1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(huff_code[i])))
        textcode = ''
        for word in text:
            for i in range(len(list_sorted)):
                if word == list_sorted[i][0]:
                    textcode += str(huff_code[i])
        self.textEdit.setText(textcode)
        print('EncodingForm <<<<< encoding')
        print(str(self.tableWidget.item(1, 2).text()))

    def decoding(self):
        print('EncodingForm >>> decoding')
        codetext = self.textEdit.toPlainText()
        print('codetext=', codetext)
        result = ''
        while codetext != '':
            for i in range(0, self.tableWidget.rowCount()):
                huffcode = self.tableWidget.item(i, 2).text()
                if huffcode == codetext[0:len(huffcode)]:
                    print('i', i, '     codetext', codetext[0:len(huffcode)], '     huffcode', huffcode, '    ',
                          huffcode == codetext[0:len(huffcode)])
                    result += self.tableWidget.item(i, 0).text()
                    codetext = codetext[len(huffcode):]
                    break
        self.textEdit.setText(result)
        print('EncodingForm <<< decoding')


class Top20Form(QtWidgets.QDialog, GUI_Top20.Ui_Dialog):
    def __init__(self):
        super(Top20Form, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init()

    def init(self):
        _func_edit = Function.Edit()
        filepaths = _func_edit.open_files()
        file_dic = {filepaths[i]: open(filepaths[i], 'r').read() for i in range(len(filepaths))}
        print(time.strftime("%M%S"))
        text = ''
        # 把选的文章放在一个text里
        for i in file_dic:
            text += file_dic[i]
        _func_cal = Function.Calculate()
        list_sorted = _func_cal.frequency_to_str(text, ' ')  # 没有用kmp是因为不需要得到每个值的具体位置,只需要加1即可,所以kmp更麻烦
        _translate = QtCore.QCoreApplication.translate
        for i in range(0, 19):
            item = self.tableWidget_Freq.item(i, 0)  # 需要在设计ui时初始化每个item的值,要不然就报错不知道为啥_(:з」∠)_
            item.setText(_translate("Dialog", str(list_sorted[i][0])))
            item = self.tableWidget_Freq.item(i, 1)
            item.setText(_translate("Dialog", str(list_sorted[i][1])))
            # self.tableWidget_Freq.setItem(i, 0, QTableWidgetItem=list_sorted[i][0])
            # self.tableWidget_Freq.setItem(i, 1, QTableWidgetItem=list_sorted[i][1])
        self.textBrowser.setText(str(list_sorted))
        print(time.strftime("%M%S"))
        # self.textEdit.setText(filename);
        # self.pushButtonEncode.clicked.connect()
        # self.pushButtonDecode.clicked.connect()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec_())
