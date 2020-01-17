# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from util.command import Command


# 用来生成port信息，（不能在被使用，需要是有效的端口）
class Port:
    def port_is_used(self, port):
        self.cmd = Command()
        result = self.cmd.excute_command_result("netstat -nat | grep "+str(port))
        if len(result) > 0:
            # 被占用
            return True
        else:
            return False

    def create_port_list(self, start_port, device_list):
        '''
        生成可用端口
        :return:
        '''
        port_list = []
        if device_list:
            while not len(port_list) == len(device_list):
                if not self.port_is_used(start_port):
                    port_list.append(start_port)
                start_port += 1
            return port_list
        else:
            print("生成可用端口失败")
            return None


if __name__ == '__main__':
    p = Port()
    print(p.port_is_used(4700))
    print(p.create_port_list(4699, [1, 2, 3,]))
