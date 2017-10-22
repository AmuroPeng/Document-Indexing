# coding=utf-8

import os
import logging
import logging.config
import pprint
import GUI_Main, GUI_EditFile, GUI_NewFile, GUI_SaveConfirm, GUI_SearchInput
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtGui, QtCore
import manifest
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


# logging.config.fileConfig("logging.conf")  # 采用配置文件
# logger = logging.getLogger("simpleExample")  # create logger

class Edit(QWidget):
    def open_file(self):
        # f = open(location, 'r')
        # lines = f.readlines()
        # f.close()
        # print('已打开项目:' + location)  # testing
        # return (lines)
        filename = QFileDialog.getOpenFileName(self, "打开文件", manifest.DocLocation, "Txt files(*.txt)")
        # "open file Dialog "为文件对话框的标题，第三个是打开的默认路径，第四个是文件类型过滤器

        print(filename)
        return filename[0]

    def open_files(self):
        filename = QFileDialog.getOpenFileNames(self, "打开文件", manifest.DocLocation, "Txt files(*.txt)")
        print(filename)
        return filename[0]

    def new_file(self, fname):
        fcontent = open(fname, 'w')
        # fcontent.write(a)
        fcontent.close()
        print('已新建项目:' + fname)  # testing
        return fname

    def save_file(self, filepath, text):
        print(2)
        f = open(filepath, 'w')
        print(f)
        f.write(text)
        print(4)
        f.close()
        print('已保存项目:' + filepath)  # testing

    # def search_file(self,key, text):
    #     print('进入搜索Function>搜索函数')
    #     result=self.kmp(key,text)

    def kmp(P, T):
        # 制作部分匹配值表格K[]
        K = []
        t = -1
        K.append(t)  # K[0]=-1
        for k in range(1, len(P) + 1):
            while t >= 0 and P[t] != P[k - 1]:
                t = K[t]
            t = t + 1
            K.append(t)
        print('部分比配值:' + str(K))

        # 进行KMP搜索
        m = 0  # 在P中的指针
        result = []
        for i in range(0, len(T)):
            while m >= 0 and P[m] != T[i]:
                m = K[m]
            m = m + 1
            if m == len(P):  # 输出
                # logger.debug('找到第' + i + '个元素比配')
                m = K[m]
                result.append(i - len(P) + 2)  # 这个+2是自己试出来的..
                # print(i)
        print('搜索结果:' + str(result))
        # pprint.pprint(result)
        return result


class Display(QWidget):
    def highlight_re(self, pattern, text, color="red"):
        if pattern:
            cursor = self.textEdit.textCursor()  # 光标
            # Setup the desired format for matches
            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(QtGui.QColor(color)))
            # Setup the regex engine
            regex = QtCore.QRegExp(pattern)
            # Process the displayed document
            pos = 0
            index = regex.indexIn(text, pos)
            while index != -1:
                # Select the matched text and apply the desired format
                cursor.setPosition(index)
                for i in range(len(pattern)):
                    cursor.movePosition(QtGui.QTextCursor.Right, 1)
                cursor.mergeCharFormat(format)
                # Move to the next match
                pos = index + regex.matchedLength()
                index = regex.indexIn(text, pos)

    def highlight(self, key, result,editform):
        print("function111")
        if key:
            cursor =editform.textEdit.textCursor()  # 光标
            # Setup the desired format for matches
            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(QtGui.QColor("red")))
            # Setup the regex engine
            # regex = QtCore.QRegExp(pattern)
            # Process the displayed document
            pos = 0
            # index = regex.indexIn(text, pos)
            while pos != len(result) - 1:
                # Select the matched text and apply the desired format
                cursor.setPosition(pos)
                for i in range(len(key)):
                    cursor.movePosition(QtGui.QTextCursor.Right, 1)
                    i = i + 1
                cursor.mergeCharFormat(format)
                pos = pos + 1
                # Move to the next match
                # pos = index + regex.matchedLength()
                # index = regex.indexIn(text, pos)


class HuffNode(object):
    def get_wieght(self):
        raise NotImplementedError(
            "The Abstract Node Class doesn't define 'get_wieght'")

    def isleaf(self):
        raise NotImplementedError(
            "The Abstract Node Class doesn't define 'isleaf'")


class LeafNode(HuffNode):
    def __init__(self, value=0, freq=0, ):
        super(LeafNode, self).__init__()
        # 节点的值
        self.value = value
        self.wieght = freq

    def isleaf(self):
        return True

    def get_wieght(self):
        return self.wieght

    def get_value(self):
        return self.value


class IntlNode(HuffNode):
    def __init__(self, left_child=None, right_child=None):
        super(IntlNode, self).__init__()

        # 节点的值
        self.wieght = left_child.get_wieght() + right_child.get_wieght()
        # 节点的左右子节点
        self.left_child = left_child
        self.right_child = right_child

    def isleaf(self):
        return False

    def get_wieght(self):
        return self.wieght

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child


class HuffTree(object):
    def __init__(self, flag, value=0, freq=0, left_tree=None, right_tree=None):

        super(HuffTree, self).__init__()

        if flag == 0:
            self.root = LeafNode(value, freq)
        else:
            self.root = IntlNode(left_tree.get_root(), right_tree.get_root())

    def get_root(self):

        return self.root

    def get_wieght(self):

        return self.root.get_wieght()

    def traverse_huffman_tree(self, root, code, char_freq):

        if root.isleaf():
            char_freq[root.get_value()] = code
            print("it = %c  and  freq = %d  code = %s") % (chr(root.get_value()), root.get_wieght(), code)
            return None
        else:
            self.traverse_huffman_tree(root.get_left(), code + '0', char_freq)
            self.traverse_huffman_tree(root.get_right(), code + '1', char_freq)


def buildHuffmanTree(list_hufftrees):
    while len(list_hufftrees) > 1:
        # 1. 按照weight 对huffman树进行从小到大的排序
        list_hufftrees.sort(key=lambda x: x.get_wieght())

        # 2. 跳出weight 最小的两个huffman编码树
        temp1 = list_hufftrees[0]
        temp2 = list_hufftrees[1]
        list_hufftrees = list_hufftrees[2:]

        # 3. 构造一个新的huffman树
        newed_hufftree = HuffTree(1, 0, 0, temp1, temp2)

        # 4. 放入到数组当中
        list_hufftrees.append(newed_hufftree)

    # last.  数组中最后剩下来的那棵树，就是构造的Huffman编码树
    return list_hufftrees[0]


if __name__ == "__main__":
    name = Edit.new_file()
    cotent = Edit.kmp('abcd', 'abcdabcddabcdabcd')
