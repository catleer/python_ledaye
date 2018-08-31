"""
Created by catleer on 2018-05-22.
"""

__author__ = 'catleer'

import os, codecs

import xlrd

# 获取文件位置
def get_file():

    if __name__ == '__main__':
        parent_path = os.path.abspath('..')
    else:
        parent_path = os.path.abspath('.')
    file_dir = os.path.join(parent_path, 'casedatas')
    type = ".xls"

    case_files = os.listdir(file_dir)
    for file in case_files:
        if type in file:
            return os.path.join(file_dir, file)

    return "没有excel条件的用例"


# 获取每条用例数据
def get_case():
    data = xlrd.open_workbook(get_file())
    sheet_cases = data.nsheets
    if sheet_cases:
        for i in sheet_cases:
            table = data.sheet_by_index(i+1)
        print(table.row_values(1))

        print(table.nrows)