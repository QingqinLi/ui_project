# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from util.opera_excel import OperaExcel


class GetData:
    def __init__(self):
        self.opera_excel = OperaExcel()

    def get_case_lines(self):
        lines = self.opera_excel.get_lines()
        return lines

    def get_handle_step(self, row):
        handle_step = self.opera_excel.get_cell(row, 3)
        return handle_step

    def get_element_key(self, row):
        element_key = self.opera_excel.get_cell(row, 4)
        return element_key

    def get_handle_element(self, row):
        handle_element = self.opera_excel.get_cell(row, 5)
        return handle_element

    def get_except_element(self, row):
        print("hello")
        except_element = self.opera_excel.get_cell(row, 6)
        return except_element

    def write_value(self, row, value):
        self.opera_excel.write_value(row, value)


if __name__ == '__main__':
    d = GetData()


