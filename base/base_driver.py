# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import time
from appium import webdriver
from util.write_user_command import WriteUserCommand


class BaseDriver:
    def __init__(self):
        self.write_user_command = WriteUserCommand()

    def android_driver(self, i):
        # 可以直接读配置文件
        # devicename, port
        device = self.write_user_command.get_value("user_info_"+str(i), "deviceName")
        port = self.write_user_command.get_value("user_info_"+str(i), "port")
        print("device, port", device, port)
        capbilities = {
            "platformName": "Android",
            "app": "/Users/qing.li/Downloads/moji.apk",
            "noReset": True,
            "deviceName": device,
            "appActivity": "com.moji.mjweather.MainActivity",
            "resetKeyboard": True,
        }
        print(capbilities)
        # 配置设备，端口为随机对应， 每台设备对应, p , bp, 生成一个session
        driver = webdriver.Remote("http://127.0.0.1:%s/wd/hub"%(str(port)), capbilities)
        return driver

    def ios_driver(self):
        pass

    def get_driver(self):
        pass