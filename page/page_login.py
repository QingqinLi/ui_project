# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver


class LoginPage:
    def __init__(self, i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)

    def get_username(self):
        """
        获取用户名元素
        :return:
        """
        return self.get_by_local.get_element("username", "login_element")

    def get_password(self):
        """
        获取密码元素
        :return:
        """
        return self.get_by_local.get_element("password", "login_element")

    def get_agree(self):
        """
        获取用户名元素
        :return:
        """
        return self.get_by_local.get_element("agree", "login_element")

    def get_login_button(self):
        """
        获取用户名元素
        :return:
        """
        return self.get_by_local.get_element("login_button", "login_element")

    def get_error_info(self):
        """
        获取错误提示信息
        :return:
        """
        return self.get_by_local.get_element("error_info", "login_element")

