# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import time
from appium import webdriver


class BaseDriver:
    def android_driver(self):
        # 可以直接读配置文件
        # devicename, port
        capbilities = {
            "platformName": "Android",
            "app": "/Users/qing.li/Downloads/MJWeatherBox-prod-release.apk",
            "noReset": True,
            "deviceName": "R58MB0Z4WCX",
            "appActivity": "com.moji.mjweather.MainActivity",
            "resetKeyboard": True,
        }
        driver = webdriver.Remote("http://127.0.0.1:4700/wd/hub", capbilities)
        return driver

    def ios_driver(self):
        pass

    def get_driver(self):
        pass