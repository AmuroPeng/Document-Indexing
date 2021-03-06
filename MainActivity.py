# -*- coding:utf-8 -*-

import Function
import os
import GUI_Main, GUI_EditFile, GUI_NewFile, GUI_Search_Substitute, \
    GUI_Encoding, GUI_Top20
import sys
from PyQt5.QtWidgets import QTableWidgetItem
import time
import re
import manifest
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class MainForm(QtWidgets.QMainWindow, GUI_Main.Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init()

    def init(self):
        self.checkBox_selcetAll.hide()
        self.Open.triggered.connect(self.open_file)
        self.New.triggered.connect(self.create_file)
        self.SearchButton.clicked.connect(self.adv_search)
        self.importItems.triggered.connect(self.import_Items)
        self.loadIndex.triggered.connect(self.load_index)
        self.saveIndex.triggered.connect(self.save_index)
        menu = QtWidgets.QMenu()
        menu.addAction('编码&译码   ', self.advsearch_encode)  # 不知道怎么左对齐,暂时先加空格来手动居中了_(:з」∠)_
        menu.addAction('Top 20   ', self.advsearch_Top20)
        self.AdvancedSearchButton.setMenu(menu)

    def open_file(self):
        func = Function.Edit()
        filepath = func.open_file()
        if filepath:
            # 显示
            edit = EditForm(filepath)
            edit.show()
            edit.exec_()

    def create_file(self):
        create = NewFileForm()
        create.show()
        create.exec_()
        fname = create.textNewFile.toPlainText()
        print(fname)
        if fname:
            func = Function.Edit()
            func.new_file(fname + ".txt")
            # 显示编辑窗口
            filepath = manifest.SaveTempPos + '' + fname + ".txt"
            print(filepath)
            edit = EditForm(filepath)
            edit.show()
            edit.exec_()

    def adv_search(self):
        def key(temp):
            return len(temp[1])

        print('MainForm ---> adv_search')
        keyword = self.SearchText.text()
        if self.tabWidget_result.count():  # 每次点搜索需要先清空之前的tab在添加
            for i in range(self.tabWidget_result.count()):
                # print('第'+str(i)+'次,移除前是'+str(self.tabWidget_result.count()))
                self.tabWidget_result.removeTab(0)
                # print('第'+str(i)+'次,移除后是'+str(self.tabWidget_result.count()))
        if keyword in self.word_dic.keys():
            word_dic_list = [(file, pos) for file, pos in self.word_dic[keyword].items()]
            word_dic_list.sort(key=key, reverse=True)  # 做这个list为了使addTab时可以按照词频进行展示,左边tab显示频率高的
            for path, _ in word_dic_list:
                # for path in self.word_dic[keyword].keys():
                self.tab_1 = QtWidgets.QWidget()
                self.tab_1.setObjectName(str(os.path.split(path)[1]))
                text = open(path, 'r').read()
                self.textBrowser = QtWidgets.QTextBrowser(self.tab_1)
                self.textBrowser.setGeometry(QtCore.QRect(20, 20, 331, 211))
                self.textBrowser.setObjectName(str(os.path.split(path)[1]))
                self.textBrowser.setText(text)
                # highlight
                if keyword:
                    cursor = self.textBrowser.textCursor()  # 光标
                    format = QtGui.QTextCharFormat()
                    format.setBackground(QtGui.QBrush(QtGui.QColor("orange")))
                    for pos in self.word_dic[keyword][path]:
                        cursor.setPosition(pos)  # 这里不需要减一,在索引环节因为前后空格判断时需要加一所以抵消了
                        for i in range(len(keyword)):
                            cursor.movePosition(QtGui.QTextCursor.Right, 1)
                        cursor.mergeCharFormat(format)
                # highlight
                self.tabWidget_result.addTab(self.tab_1, '')
                _translate = QtCore.QCoreApplication.translate
                self.tabWidget_result.setTabText(self.tabWidget_result.indexOf(self.tab_1),
                                                 _translate("MainWindow", str(os.path.split(path)[1])))
        print('MainForm <--- adv_search')

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

    def import_Items(self):
        print('MainForm --> importItems')
        _func_edit = Function.Edit()
        filepaths = _func_edit.open_files()
        if filepaths:
            file_dic = {filepaths[i]: open(filepaths[i], 'r').read() for i in range(len(filepaths))}
            print('开始加载时间:', time.strftime("%H%M%S"))
            self.word_dic = {}
            self.word_dict_sorted = {}
            word_dic_ = dict()
            for k, v in file_dic.items():
                v = v.replace('<br />', '\n')  # 199_1的txt里居然有br!我都傻了,之后全是错位的!还好发现的及时
                v = re.sub(r'[.?!,""><)(/]', ' ', v)
                for word in v.split(' '):  # 省的实例化split之后的list了,这个好厉害_(:з」∠)_
                    if word == '':
                        continue
                    else:
                        if word not in self.word_dic.keys():
                            self.word_dic[word] = {}
                            self.word_dict_sorted[word] = {}
                        temp_word = ' ' + word + ' '  # 保证是按词搜索而不是按字符串搜索
                        temp_v = v + ' '  # 保证最后一个词如果是keyword可以正常高亮
                        kmp_list = Function.Calculate.kmp(temp_word, temp_v)
                        self.word_dic[word][k] = kmp_list  # 这样可以让dict的value是list么?答:应该是可以_(:з」∠)_
                        self.word_dict_sorted[word][k] = kmp_list

            print('word_dic', str(self.word_dic))
            print('结束加载时间:', time.strftime("%H%M%S"))
            # self.checkBox_selcetAll.setGeometry(QtCore.QRect(70, 120, 301, 21))
            positions = [(i, j) for i in range(5) for j in range(4)]
            for position, path in zip(positions, filepaths):
                checkBox = QtWidgets.QCheckBox(os.path.split(path)[1], self)
                checkBox.filepath = path
                checkBox.setCheckState(True)
                self.Layout_Items.addWidget(checkBox, *position)
            self.checkBox_selcetAll.show()
            print('MainForm <-- importItems')

    def save_index(self):
        print('MainForm --> save_index')
        Function.save_struct(manifest.SaveStructPos, self.word_dic)
        print('MainForm <-- save_index')

    def load_index(self):
        print('MainForm --> load_index')
        self.word_dic = Function.load_struct(manifest.SaveStructPos)
        print('MainForm <-- load_index')


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

    def save_text(self, filepath):
        print("save")
        content = self.textEdit.toPlainText()
        # location = manifest.SaveTempPos  # 需要修改的以后
        # fname = self.MainForm.create_file()
        print("进入Function函数")
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
        print("Search_SubstituteForm-->search")
        key = self.lineEdit_searchContent.text()
        self.lineEdit_searchContent_2.setText(self.lineEdit_searchContent.text())  # 将替换栏的搜索内容和查找栏一致,便于对同一个词进行多个操作
        text = editform.textEdit.toPlainText()  # 得调用主函数建的实例,在用里面的参数
        result = Function.Calculate.kmp(key, text)
        print('搜索内容:' + key + '  结果:' + str(result))
        editform.textEdit.setText(text)  # 用于刷新高亮
        # Function.Display.highlight(key, result, editform)
        if key:
            cursor = editform.textEdit.textCursor()  # 光标
            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(QtGui.QColor("orange")))
            for pos in result:
                cursor.setPosition(pos - 1)  # 不懂为什么得减1,不减就错位了
                for i in range(len(key)):
                    cursor.movePosition(QtGui.QTextCursor.Right, 1)
                cursor.mergeCharFormat(format)
        print("Search_SubstituteForm-->search")

    def allSubstitute(self, editform):
        print("Search_SubstituteForm-->allSubstitute")
        old = self.lineEdit_searchContent_2.text()
        self.lineEdit_searchContent.setText(self.lineEdit_searchContent_2.text())  # 同上面方法中的查找,便于多部操作搜索值
        new = self.lineEdit_substituteContent_2.text()
        text = editform.textEdit.toPlainText()
        editform.textEdit.setText('')  # 加这么一句可以间接消除之前显示的高光
        editform.textEdit.setText(text.replace(old, new))  # text做replace之后,本身是不变的,只是传一个改变后的值而已
        text = editform.textEdit.toPlainText()
        result = Function.Calculate.kmp(new, text)
        print('搜索内容:' + new + '  结果:' + str(result))
        # Function.Display.highlight(key, result, editform)
        if new:
            cursor = editform.textEdit.textCursor()  # 光标
            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(QtGui.QColor("orange")))
            for pos in result:
                cursor.setPosition(pos - 1)  # 不懂为什么得减1,不减就错位了
                for i in range(len(new)):
                    cursor.movePosition(QtGui.QTextCursor.Right, 1)
                cursor.mergeCharFormat(format)
        print("Search_SubstituteForm-->allSubstitute")


class EncodingForm(QtWidgets.QDialog, GUI_Encoding.Ui_Dialog):
    def __init__(self):
        super(EncodingForm, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init()

    def init(self):
        func = Function.Edit()
        filepaths = func.open_file()
        if filepaths:
            text = open(filepaths, 'r').read()
            self.textEdit.setText(text)
            self.pushButtonEncode.clicked.connect(lambda: self.encoding(text))
            self.pushButtonDecode.clicked.connect(self.decoding)


    def encoding(self, text):
        print('EncodingForm >>>>> encoding')
        _func_cal = Function.Calculate()
        list_sorted = _func_cal.frequency_to_char(text)
        nodes = Function.createNodes([item[1] for item in list_sorted])
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
        if filepaths:
            file_dic = {filepaths[i]: open(filepaths[i], 'r').read() for i in range(len(filepaths))}
            print(time.strftime("%M%S"))
            text = ''
            # 把选的文章放在一个text里
            for i in file_dic:
                text += file_dic[i]
            _func_cal = Function.Calculate()
            text = Function.strip_html(text)
            list_sorted = _func_cal.frequency_to_str(text, ' ')  # 没有用kmp是因为不需要得到每个值的具体位置,只需要加1即可,所以kmp更麻烦
            _translate = QtCore.QCoreApplication.translate
            for i in range(0, 19):
                item = self.tableWidget_Freq.item(i, 0)  # 需要在设计ui时初始化每个item的值,要不然就报错不知道为啥_(:з」∠)_
                item.setText(_translate("Dialog", str(list_sorted[i][0])))
                item = self.tableWidget_Freq.item(i, 1)
                item.setText(_translate("Dialog", str(list_sorted[i][1])))
            self.textBrowser.setText(str(list_sorted))
            print(time.strftime("%M%S"))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec_())
