#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/12/10 18:01
# @Author  : lxx
# @File    : TextProcessor.py
# @Software: PyCharm
import numpy as np
import  matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']

class TextProcessor():
    def __init__(self,text_file_path):
        self.text_file_path = text_file_path

    def readFile(self):
        line_size=[]
        for line in open(self.text_file_path,encoding="utf-8"):
            line = line.strip()
            line_size.append(len(line))
        return line_size

    def generator_report(self):
        line_size=self.readFile()
        max_len=max(line_size)
        min_len =min(line_size)
        mean_len = np.mean(line_size)
        median_len = np.median(line_size)
        plt.figure(figsize=(10, 10), dpi=80)
        plt.subplot(1, 2, 2)
        x=["最短长度","平均长度","中位数","最长长度"]
        y=[min_len,mean_len,median_len,max_len]
        # 柱子的宽度
        width = 0.45
        # 绘制柱状图, 每根柱子的颜色为紫罗兰色
        p2 = plt.bar(x, y, width, label="num", color="#87CEFA")
        # 设置横轴标签
        plt.xlabel('长度类型')
        # 设置纵轴标签
        plt.ylabel('长度')
        # 添加标题
        plt.title('文本长度统计')
        # 添加图例
        plt.legend(loc="upper right")
        plt.show()