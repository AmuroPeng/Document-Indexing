# coding=utf-8

import os
import logging
import logging.config
import pprint


# logging.config.fileConfig("logging.conf")  # 采用配置文件
# logger = logging.getLogger("simpleExample")  # create logger


def open_file(location):
    f = open(location, 'r')
    lines = f.readlines()
    f.close()
    print('已打开项目' + location)  # testing
    return (lines)


def new_file():
    # 检查新建文件名是否重复
    while True:
        fname = input('Enter filename:')
        if os.path.exists(fname):
            print("Error:'%s' already exists" % fname)
            # !!!这里加入清空用户填写栏的内容,以及跳转回输入重新输入界面
        else:
            break
    fcontent = open(fname, 'w')
    # fcontent.write(a)
    fcontent.close()
    print('已新建项目:' + fname)  # testing
    return fname


def save_file(content, location):
    f = open(location, 'w')
    f.write(str(content))
    f.close()
    print('已保存项目:' + location)  # testing


def search_file(f, word):
    print()


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
    name = new_file()
    open_file(name)
    cotent = kmp('abcd', 'abcdabcddabcdabcd')
    save_file(cotent, name)
