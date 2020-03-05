# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import xlrd
from xlutils.copy import copy


# 单元格需要设置为文本类型
class OperaExcel:
    def __init__(self, file_path=None, i=None):
        if not file_path:
            self.file_path = "../excel/key_word.xlsx"
        else:
            self.file_path = file_path
        if not i:
            self.i = 0
        else:
            self.i = i
        self.excel = self.get_excel()
        self.table = self.get_tables(self.i)

    def get_excel(self):
        data = xlrd.open_workbook(self.file_path)
        return data

    def get_tables(self, i):
        table = self.excel.sheets()[i]
        return table

    def get_cell(self, row, col):
        return self.table.cell(row, col).value

    def get_lines(self):
        line = self.table.nrows
        return line

    def write_value(self, row, value):
        read_value = self.excel
        write_data = copy(read_value)
        print(write_data)
        write_save = write_data.get_sheet(0)
        print(write_save)
        write_save.write(row, 7, value)
        write_data.save(self.file_path)


if __name__ == '__main__':
    oe = OperaExcel()
    print(oe.write_value(1, "tests"))
    print(oe.get_cell(1, 8))