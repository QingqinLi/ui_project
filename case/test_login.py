# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import threading
import unittest
from appium import webdriver
from business.business_login import BusinessLogin
import time
import HTMLTestRunner


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # capbilities = {
        #     "platformName": "Android",
        #     "app": "Users/qing.li/Downloads/MJWeatherBox-prod-release.apk",
        #     "noReset": True,
        #     "deviceName": "e636c401",
        #     "appActivity": "com.moji.mjweather.MainActivity",
        #     "resetKeyboard": True,
        # }
        # cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capbilities)
        # cls.business_login = BusinessLogin(cls.driver)
        print("this is setupClass")

    def setUp(self):
        print("this is setup")

    # @unittest.skip("TestLogin")
    def test_login_pass(self):
        self.driver.find_elements_by_id("com.moji.mjweather:id/tab_container")[3].click()
        self.driver.find_element_by_id("com.moji.mjweather:id/mNickView").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.moji.mjweather:id/tv_switch_login").click()
        self.business_login.login_pass("13263106808", "123456")

    def test_username_error(self):
        self.driver.find_elements_by_id("com.moji.mjweather:id/tab_container")[3].click()
        self.driver.find_element_by_id("com.moji.mjweather:id/mNickView").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.moji.mjweather:id/tv_switch_login").click()
        self.assertFalse(self.business_login.login_username_error("1326310680", "123456", "用户名输入不正确，请重新输入"))

    def test_demo(self):
        print("this is test demo")

    def test_demo2(self):
        print("this is test demo2")

    def tearDown(self):
        print("this is teardown")

    @classmethod
    def tearDownClass(cls):
        print("this is teardownClass")


def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(TestLogin("test_demo2"))
    suite.addTest(TestLogin("test_demo"))
    report_file = "/Users/qing.li/PycharmProjects/AppiumPython/report/login"+str(i)+".html"
    fp = open(report_file, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(fp)
    runner.run(suite)


if __name__ == "__main__":
    # unittest.main()
    # 选择case在suite中执行
    # suite = unittest.TestSuite()
    # suite.addTest(TestLogin("test_username_error"))
    # suite.addTest(TestLogin("test_login_pass"))
    # report_file = "/Users/qing.li/PycharmProjects/AppiumPython/report/login0.html"
    # fp = open(report_file, 'wb+')
    # runner = HTMLTestRunner.HTMLTestRunner(fp)
    # runner.run(suite)
    threads = []
    for i in range(3):
        t = threading.Thread(target=get_suite, args=(i,))
        threads.append(t)
    [t.start() for t in threads]
