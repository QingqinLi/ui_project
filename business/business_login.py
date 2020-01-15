# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from handle.handle_login import HandleLogin


class BusinessLogin:
    def __init__(self):
        self.handle_login = HandleLogin()

    def login_pass(self, username, password):
        self.handle_login.click_agree()
        self.handle_login.send_username(username)
        self.handle_login.send_password(password)
        self.handle_login.click_login_button()

    def login_username_error(self, username, password, error_info):
        self.handle_login.click_agree()
        self.handle_login.send_username(username)
        self.handle_login.send_password(password)
        self.handle_login.click_login_button()
        return self.handle_login.get_error_info(error_info)



