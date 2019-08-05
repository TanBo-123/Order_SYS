#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import openpyxl
#import matplotlib.pyplot as plt
#import numpy as np


#用于matplotlib显示中文
#plt.rcParams['font.sans-serif'] = ['SimHei']

Contents_line = 1


def Export_menu(menu,score,num):
    menu_len = len(menu)-1
    menu_list = []
    temp = 0
    for menu_cell,score_cell in zip(menu[1:],score[1:]):
        menu_list.append([menu_cell.value,score_cell.value,0])
    for i in range(menu_len):
        menu_list[i] = [menu_list[i][0],temp,temp+menu_list[i][1]]
        temp = menu_list[i][2]
    print(menu_list,temp)
    pass



fpath =  './menu.xlsx'
wb = openpyxl.load_workbook(fpath)
sheets = wb.sheetnames
ws = wb[wb.sheetnames[0]]
print(len(ws["A"]), type(ws["A"]))
#for cell in ws["A"]:
#    print(type(cell),cell.value)

Export_menu(ws["A"],ws["C"],3)

wb.save(fpath)