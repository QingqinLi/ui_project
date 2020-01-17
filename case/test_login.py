# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import threading
import unittest
from business.business_login import BusinessLogin
import time
import HTMLTestRunner
from util.server import Server
import multiprocessing
from threading import Lock
from util.write_user_command import WriteUserCommand


class ParameTestCase(unittest.TestCase):
    """
    继承，可以传递参数
    """
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global param
        param = parame


class TestLogin(ParameTestCase):

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
        print("parame:", param)
        cls.business_login = BusinessLogin(param)
        print("this is setupClass")

    def setUp(self):
        print("this is setup", param)

    # @unittest.skip("TestLogin")
    def test_login_pass(self):
        # self.driver.find_elements_by_id("com.moji.mjweather:id/tab_container")[3].click()
        # self.driver.find_element_by_id("com.moji.mjweather:id/mNickView").click()
        # time.sleep(2)
        # self.driver.find_element_by_id("com.moji.mjweather:id/tv_switch_login").click()
        time.sleep(15)
        self.business_login.login_pass("13263106808", "123456")

    def test_username_error(self):
        self.driver.find_elements_by_id("com.moji.mjweather:id/tab_container")[3].click()
        self.driver.find_element_by_id("com.moji.mjweather:id/mNickView").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.moji.mjweather:id/tv_switch_login").click()
        self.assertFalse(self.business_login.login_username_error("1326310680", "123456", "用户名输入不正确，请重新输入"))

    def test_demo(self):
        print("this is test demo:", param)

    def test_demo2(self):
        print("this is test demo2")

    def tearDown(self):
        print("this is teardown")

    @classmethod
    def tearDownClass(cls):
        print("this is teardownClass")


def get_suite(n, l):
    l.acquire()
    suite = unittest.TestSuite()
    # suite.addTest(TestLogin("test_login_pass", parame=n))
    print("n:", n)
    suite.addTest(TestLogin("test_login_pass", parame=n))
    suite.addTest(TestLogin("test_demo2", parame=n))
    report_file = "/Users/qing.li/PycharmProjects/AppiumPython/report/login"+str(n)+".html"
    fp = open(report_file, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(fp)
    runner.run(suite)
    l.release()


def init_appium():
    server = Server()
    server.main()
    time.sleep(5)


def get_count():
    write_user_command = WriteUserCommand()
    count = write_user_command.get_file_lines()
    return count


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
    # 启动appium服务器
    init_appium()
    threads = []
    l = Lock()
    for i in range(get_count()):
        # 使用多线程需要使用线程锁， 防止线程间数据混乱
        t = threading.Thread(target=get_suite, args=(i, l))
        threads.append(t)
        # t = multiprocessing.Process(target=get_suite, args=(i, ))
        # threads.append(t)
    [t.start() for t in threads]
