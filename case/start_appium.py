# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import sys
sys.path.append("../../")

from appium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from util.get_by_local import GetByLocal
from util.read_ini import ReadIni


def get_driver():
    capbilities = {
        "platformName": "Android",
        "deviceName": "e636c401",
        # pc端app的路径
        "app": "Users/qing.li/Downloads/MJWeatherBox-prod-release.apk",
        # 启动的activity
        "appActivity": "com.moji.mjweather.MainActivity",
        # 使用的底层测试平台
        "automationName": "UiAutomator2",
        # appAcitivity改成appWaitActivity,真机防止报错
        # "appWaitActivity": "com.imooc.component.imoocmain.index.MCMainActivity",
        # 是否重新安装app
        "noReset": True,
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capbilities)
    return driver


def get_size(driver):
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


def swipe_up(driver):
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    driver.swipe(width / 2, height - 50, width / 2, 50, 1000)


def direction(direct, driver):
    if direct == 'up':
        swipe_up(driver)


def go_login(driver):
    driver.find_element_by_xpath("//*[@text='账号']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='点击登录']").click()


def login(driver):
    driver.find_element_by_id("cn.com.open.mooc:id/tvPassLogin").click()
    sleep(3)
    driver.find_element_by_id("cn.com.open.mooc:id/accountEditChannel2").send_keys("13263106808")
    driver.find_element_by_id("cn.com.open.mooc:id/passwordEditChannel2").send_keys("291518lq")
    driver.find_element_by_id("cn.com.open.mooc:id/login").click()
    sleep(4)


def into_main(driver):
    get_element = GetByLocal(driver)
    get_element.get_element("agree").click()
    sleep(1)
    get_element.get_element("allow").click()
    sleep(2)
    get_element.get_element("allow").click()
    sleep(2)
    get_element.get_element("allow").click()
    sleep(5)


def into_main_by_uiautomator(driver):
    driver.find_element_by_android_uiautomator('new UiSelector().text("同意并进入")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("允许")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("允许")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("允许")').click()


def get_web_view(driver):
    sleep(20)
    webview = driver.contexts
    print("webview", webview)
    for view in webview:
        if '///' in view:
            # 切换之后driver也切换
            driver.switch_to_default_content(view)
            break
    # 切换到h5之后，使用selenium的定位方式
    driver.find_element_by_link_text("C").click()
    driver.switch_to.context(webview[0])
    driver.find_element_by_id("").click()


# 处理页面的toast
def get_toast(driver):
    toast_element = ("xpath", "//*[contains(@text, 'xxx')]")
    WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(toast_element))


def login_page(driver):
    driver.find_elements_by_id("com.moji.mjweather:id/tab_container")[3].click()
    driver.find_element_by_id("com.moji.mjweather:id/mNickView").click()
    sleep(2)
    driver.find_element_by_id("com.moji.mjweather:id/tv_switch_login").click()
    driver.find_element_by_id("com.moji.mjweather:id/cb_treaty").click()
    sleep(2)
    driver.find_element_by_id("com.moji.mjweather:id/et_login_input_account").send_keys("13263106808")
    driver.find_element_by_id("com.moji.mjweather:id/et_login_input_password").send_keys("123456")
    driver.find_element_by_id("com.moji.mjweather:id/tv_action_login").click()


def logout_page(driver):
    driver.find_elements_by_id("com.moji.mjweather:id/tab_container")[3].click()
    driver.find_element_by_id("com.moji.mjweather:id/mSettingsView").click()
    sleep(2)


driver = get_driver()
login_page(driver)
# get_web_view(driver)
# go_login(driver)
# sleep(3)
# login(driver)
# driver.quit()
#
# size = driver.get_window_size()
# width = size['width']
# height = size['height']
# driver.swipe(width/2, height-50, width/2, 50, 1000)