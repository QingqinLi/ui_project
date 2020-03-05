# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from util.opera_excel import OperaExcel
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ActionMethod:
    def __init__(self, i):
        self.driver = BaseDriver().android_driver(i)
        self.get_by_local = GetByLocal(self.driver)
        self.opera_excel = OperaExcel()
        self.width = self.get_window_size()[0]
        self.height = self.get_window_size()[1]

    def input(self, *args):
        element = self.get_by_local.get_element(args[0])
        if not element:
            return args[0], "element not found"
        element.send_keys(args[1])

    def on_click(self, *args):
        print(args)
        element = self.get_by_local.get_element(args[0])
        if not element:
            return args[0], "element not found"
        element.click()

    def sleep_time(self, *args):
        time.sleep(args[0])

    def get_window_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_up(self, *args):

        start_x, end_x = self.width/2, self.width/2
        start_y, end_y = self.height*9/10, self.height[1]/10
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def swipe_down(self, *args):
        start_x, end_x = self.width/2
        start_y, end_y = self.height/10, self.height*9/10
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def swipe_left(self, *args):
        start_x, end_x = self.width*9/10, self.width/10
        start_y, end_y = self.height/2, self.height/2
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def swipe_right(self, *args):
        start_x, end_x = self.width/10, self.width*9/10
        start_y, end_y = self.height/2, self.height/2
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def get_toast_element(self, *args):
        time.sleep(2)
        toast_element = ("xpath", "//*[contains(@text, "+args[0]+")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_element))

    def get_excel_lines(self, *args):
        lines = self.opera_excel.get_lines()
        return lines

    def get_element(self, *args):
        element = self.get_by_local.get_element(args[0])
        return element