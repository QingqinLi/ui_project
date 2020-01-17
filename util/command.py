# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
# 执行系统命令
import os
import subprocess

# print(os.system("adb devices"))
#
# # 收集结果
# print(os.popen("adb devices").readlines())


class Command:
    def excute_command_result(self, cmd):
        result_list = []
        result = os.popen(cmd).readlines()
        for i in result:
            if i == '\n': continue
            result_list.append(i.strip('\n'))
        return result_list

    def excute_command(self, cmd):
        # os.system(cmd)
        subprocess.Popen(cmd, shell=True, stdout=open('appium.log', 'a'), stderr=subprocess.STDOUT)


if __name__ == '__main__':
    c = Command()
    print(c.excute_command_result("adb devices"))