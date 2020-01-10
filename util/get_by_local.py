# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from util.read_ini import ReadIni


class GetByLocal:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key, section=None):
        read_ini = ReadIni()
        try:
            value = read_ini.get_value(key, section)
        except:
            return None
        value = value.split(">")
        by = value[0]
        option = value[1]
        if by == "class":
            return self.driver.find_element_by_class_name(option)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(option)
        else:
            return self.driver.find_element_by_id(option)



