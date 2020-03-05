# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from key_word.action_method import ActionMethod
from key_word.get_data import GetData
from util.server import Server
import time
from multiprocessing import Process
from util.write_user_command import WriteUserCommand


class RunMain:
    def __init__(self, i):
        self.action_method = ActionMethod(i)
        self.get_data = GetData()

    def run_method(self):
        lines = self.action_method.get_excel_lines()
        for i in range(1, lines):
            handle_step = self.get_data.get_handle_step(i)
            element_key = self.get_data.get_element_key(i)
            handle_element = self.get_data.get_handle_element(i)
            except_element = self.get_data.get_except_element(i)
            # print("test", i, handle_step, element_key, handle_element, except_element)
            if not except_element:
                # 反射
                handle_method = getattr(self.action_method, handle_step)
                handle_method(element_key, handle_element)
                time.sleep(2)
            else:
                if handle_step:
                    handle_method = getattr(self.action_method, handle_step)
                    handle_method(element_key, handle_element)
                    time.sleep(2)
                flag = self.action_method.get_element(except_element)
                if flag:
                    self.get_data.write_value(i, 'pass')
                else:
                    self.get_data.write_value(i, 'fail')


def rmain(i):
    rm = RunMain(i)
    rm.run_method()


def get_count():
    write_user_command = WriteUserCommand()
    count = write_user_command.get_file_lines()
    return count


if __name__ == '__main__':
    Server().main()
    time.sleep(5)
    # rm = RunMain()
    # time.sleep(5)
    # rm.run_method()

    process = []
    for i in range(get_count()):
        # 使用多线程需要使用线程锁， 防止线程间数据混乱
        t = Process(target=rmain, args=(i,))
        process.append(t)
        # t = multiprocessing.Process(target=get_suite, args=(i, ))
        # threads.append(t)
    [t.start() for t in process]