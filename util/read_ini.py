# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
# 读取ini文件的工具类
import configparser


class ReadIni:
    def __init__(self, file_path=None):
        if not file_path:
            self.file_path = "/Users/qing.li/PycharmProjects/AppiumPython/config/LocalElemnt.ini"
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    def get_value(self, key, section=None):
        if not section:
            section = 'login_element'
        try:
            return self.data.get(section, key)
        except Exception as e:
            return None


# if __name__ == "__main__":
#     read_ini = ReadIni()
#     print(read_ini.get_value("username"))
