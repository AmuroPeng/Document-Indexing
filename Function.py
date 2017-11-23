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
import re


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
        print('Function >>> save_file')
        f = open(filepath, 'w')
        f.write(text)
        f.close()
        print('Function <<< save_file')


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

    def highlight(self, key, result, editform):
        print("function111")
        if key:
            cursor = editform.textEdit.textCursor()  # 光标
            # Setup the desired format for matches
            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(QtGui.QColor("red")))
            # Setup the regex engine
            # regex = QtCore.QRegExp(pattern)
            # Process the displayed document
            pos = 0
            # index = regex.indexIn(text, pos)
            while pos != len(result) - 1:  # 不清楚为啥错着一位,
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


class Calculate(QWidget):
    def frequency_to_str(self, text, split_key):
        print('调用Function.Calculate >>>>> frequency')
        text = text.replace('<br />', '\n')  # 199_1的txt里居然有br!我都傻了,之后全是错位的!还好发现的及时
        text = re.sub(r'[.?!,""></]', ' ', text)  # 去除逗号句号
        dic = {}
        for word in text.split(split_key):  # 省的实例化split之后的list了,这个好厉害_(:з」∠)_
            dic.setdefault(word.lower(), 0)  # lower 不区分大小写  setdefault 如果该key没有value则设为默认值0
            dic[word.lower()] += 1
        list_sorted = list(sorted(dic.items(), key=lambda d: d[1], reverse=True))  # dict没法选择第几项,所以转成list再操作好了
        del list_sorted[0]  # 第一项是''空的,不知道为啥
        print('Function.Calculate <<<<< frequency')
        return list_sorted

    def frequency_to_char(self, text):
        print('调用Function.Calculate >>>>> frequency')
        dic = {}
        for word in list(text):
            dic.setdefault(word, 0)  # setdefault 如果该key没有value则设为默认值0
            dic[word] += 1
        list_sorted = list(sorted(dic.items(), key=lambda d: d[1], reverse=True))  # dict没法选择第几项,所以转成list再操作好了
        # del list_sorted[0]  # 在译码环节就要留着空格了
        print('Function.Calculate <<<<< frequency')
        return list_sorted

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
        # print('部分比配值:' + str(K))

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
        # print('搜索结果:' + str(result))
        # pprint.pprint(result)
        return result


# Tree-Node Type
class Node:
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq

    def isLeft(self):
        return self.father.left == self


# create nodes创建叶子节点
def createNodes(freqs):
    return [Node(freq) for freq in freqs]


# create Huffman-Tree创建Huffman树
def createHuffmanTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]


# Huffman编码
def huffmanEncoding(nodes, root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes


def strip_html(text):  # Delete html tags in text.
    new_text = " "
    is_html = False
    for character in text:
        if character == "<":
            is_html = True
        elif character == ">":
            is_html = False
            new_text += " "
        elif is_html is False:
            new_text += character
    return new_text


if __name__ == '__main__':
    # chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
    # freqs = [10,4,2,5,3,4,2,6,4,4,3,7,9,6]
    chars_freqs = [('C', 2), ('G', 2), ('E', 3), ('K', 3), ('B', 4),
                   ('F', 4), ('I', 4), ('J', 4), ('D', 5), ('H', 6),
                   ('N', 6), ('L', 7), ('M', 9), ('A', 10)]
    nodes = createNodes([item[1] for item in chars_freqs])
    print([item[1] for item in chars_freqs])
    print('nodes', nodes)
    root = createHuffmanTree(nodes)
    codes = huffmanEncoding(nodes, root)
    print(codes)
    for item in zip(chars_freqs, codes):
        print('Character:%s freq:%-2d   encoding: %s' % (item[0][0], item[0][1], item[1]))
