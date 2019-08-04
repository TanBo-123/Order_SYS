#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import openpyxl
import matplotlib.pyplot as plt
import numpy as np


#用于matplotlib显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']

fpath =  './menu.xlsx'
wb = openpyxl.load_workbook(fpath)
sheets = wb.sheetnames
ws = wb[wb.sheetnames[0]]
print(len(ws["A"]))



def Export_menu():


    pass