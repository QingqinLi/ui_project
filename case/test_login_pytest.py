# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import unittest
from appium import webdriver
from business.business_login import BusinessLogin
import time
import pytest


class TestLogin:

    @classmethod
    def setup_class(cls):
        capbilities = {
            "platformName": "Android",
            "app": "Users/qing.li/Downloads/MJWeatherBox-prod-release.apk",
            "noReset": True,
            "deviceName": "e636c401",
            "appActivity": "com.moji.mjweather.MainActivity",
            "resetKeyboard": True,
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capbilities)
        cls.business_login = BusinessLogin(cls.driver)
        print("this is setupClass")

    def setup(self):
        print("this is setup")

    @pytest.mark.fail
    @pytest.mark.parametrize("username, password, message", [
        ("1326808", "123456", "用户名输入不正确，请重新输入"),
        ("1233444", "123456", "用户名输入不正确，请重新输入"),
    ])
    def test_username_error(self, username, password, message):
        TestLogin.driver.find_elements_by_id("com.moji.mjweather:id/tab_container")[3].click()
        TestLogin.driver.find_element_by_id("com.moji.mjweather:id/mNickView").click()
        time.sleep(2)
        TestLogin.driver.find_element_by_id("com.moji.mjweather:id/tv_switch_login").click()
        assert TestLogin.business_login.login_username_error(username, password, message)

    # @unittest.skip("TestLogin")
    # @pytest.mark.success
    # def test_login_pass(self):
    #     TestLogin.driver.find_elements_by_id("com.moji.mjweather:id/tab_container")[3].click()
    #     TestLogin.driver.find_element_by_id("com.moji.mjweather:id/mNickView").click()
    #     time.sleep(2)
    #     TestLogin.driver.find_element_by_id("com.moji.mjweather:id/tv_switch_login").click()
    #     TestLogin.business_login.login_pass("13263106808", "123456")
    def test_demo(self):
        print("this is test demo")

    def test_demo2(self):
        print("this is test demo2")

    def teardown(self):
        print("this is teardown")

    @classmethod
    def teardown_class(cls):
        print("this is teardownClass")


# if __name__ == "__main__":
#     # unittest.main()
#     # 选择case在suite中执行
#     suite = unittest.TestSuite()
#     suite.addTest(TestLogin("test_username_error"))
#     runner = unittest.TextTestRunner()
#     runner.run(suite)

"""
可以使用pytest_order对测试用例进行顺序的编排， 使用pytest.mark对不同的测试用例进行标记，使用and.not来设置
测试用例的执行关系, terminal中使用pytest -m 来指明分组
参数化， pytest.mark.parametrize

报告生成：
    pytest-html
"""