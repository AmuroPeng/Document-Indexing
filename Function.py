# coding=utf-8

import os
import logging
import logging.config
import pprint
import os
import GUI_Main, GUI_EditFile, GUI_NewFile, GUI_SaveConfirm, GUI_SearchInput
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
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


if __name__ == "__main__":
    name = Edit.new_file()
    cotent = Edit.kmp('abcd', 'abcdabcddabcdabcd')
