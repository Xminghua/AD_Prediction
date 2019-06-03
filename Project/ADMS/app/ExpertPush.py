#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/3 21:12
# @Author  : HuaCode
# @File    : ExpertPush.py
# @Software: PyCharm

from datetime import datetime
import xlrd
from xlrd import xldate_as_tuple

"""
从excel表格导入专家用户数据
"""
def get_expertexcel(filename):
    rbook = xlrd.open_workbook(filename)
    sheet = rbook.sheet_by_name('Sheet1')
    rows = sheet.nrows
    cols = sheet.ncols

    all_content = []
    row_flag = 0
    for i in range(rows):
        row_content = []
        row_flag += 1
        for j in range(cols):
            ctype = sheet.cell(i, j).ctype#表格数据类型
            cell = sheet.cell_value(i, j)
            if ctype == 2 and cell % 1 == 0:#如果是整型
                cell = int(cell)
            elif ctype == 3:
                #转换成datetime对象
                date = datetime(*xldate_as_tuple(cell, 0))
                cell = date.strftime('%Y/%d/%m %H:%M:%S')
            elif ctype == 4:
                cell = True if cell == 1 else False
            if row_flag != 1:
                row_content.append(cell)
        if row_content:
            all_content.append(row_content)
    print(all_content)
    return all_content



def get_expertdata(filename):
    index = 0
    data = xlrd.open_workbook(filename)
    table = data.sheets()[index]
    rows = table.nrows
    result = []
    row_flag = 0
    for i in range(rows):
        row_flag += 1
        col = table.row_values(i)  ##获取每一列数据
        # print(col)
        # print(row_flag)
        if row_flag != 1:
            print(int(col[5]))
            result.append(col)
    # print(result)
    return result

class excel_read():
    def __init__(self, excel_path=r'Experts.xlsx',encoding='utf-8',index=0):

      self.data=xlrd.open_workbook(excel_path)  ##获取文本对象
      self.table=self.data.sheets()[index]     ###根据index获取某个sheet
      self.rows=self.table.nrows   ##3获取当前sheet页面的总行数,把每一行数据作为list放到 list

    def get_data(self):
        result=[]
        row = 0
        for i in range(self.rows):
            row += 1
            col=self.table.row_values(i)  ##获取每一列数据
            print(col)
            print(row)
            if row != 1:
                print(int(col[5]))
                result.append(col)
        print(result)
        return result

# if __name__ == '__main__':
#    get_expertexcel('Experts.xlsx')



        ##获取的结果样式[[],[],[],[]]
