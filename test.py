#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/12/10 18:30
# @Author  : lxx
# @File    : test.py
# @Software: PyCharm
from TextProcessor import TextProcessor

text_path="data/text.txt"

text_processor = TextProcessor(text_path)
text_processor.generator_report()