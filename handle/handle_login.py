# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from page.page_login import LoginPage


class HandleLogin:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def send_username(self, username):
        self.login_page.get_username().send_keys(username)

    def send_password(self, password):
        self.login_page.get_password().send_keys(password)

    def click_agree(self):
        self.login_page.get_agree().click()

    def click_login_button(self):
        self.login_page.get_login_button().click()

    def get_error_info(self, msg):
        message = self.login_page.get_error_info().text
        if msg == message:
            return True
        else:
            return False

