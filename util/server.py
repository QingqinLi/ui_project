# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from util.command import Command
from util.port import Port
import threading
from util.write_user_command import WriteUserCommand


# 处理设备信息
class Server:
    def __init__(self):
        self.cmd = Command()
        self.port = Port()
        self.write_user_command = WriteUserCommand()
        self.device_list = self.get_devices()

    def get_devices(self):
        """
        获取设备信息
        :return:
        """
        result_list = self.cmd.excute_command_result("adb devices")
        device_list = []
        if len(result_list) > 1:
            for d in result_list:
                if d == 'List of devices attached':
                    continue
                elif '\tdevice' in d:
                    device_list.append(d.replace('\tdevice', ''))
            return device_list
        else:
            return None

    def create_port_list(self, start_port):
        port_list = self.port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self, i):
        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_list = self.create_port_list(4900)
        command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(bootstrap_list[i]) + " -U " + self.device_list[i] + \
                  " --no-reset --session-override --log appium.log"
        command_list.append(command)
        self.write_user_command.write_data(i, self.device_list[i], bootstrap_list[i], appium_port_list[i])
        # port device 配对关系写入配置文件，base文件读取
        return command_list

    def start_server(self, i):
        """
        启动服务
        :return:
        """
        appium_command = self.create_command_list(i)
        self.cmd.excute_command(appium_command)

    def kill_server(self):
        """
        杀掉之前的进程
        :return:
        """
        server_list = self.cmd.excute_command_result("ps -ef | grep node")
        if server_list:
            self.cmd.excute_command("killall node")

    def main(self):
        """
        多线程启动appium
        :return:
        """
        self.kill_server()
        self.write_user_command.clear_data()
        appium_list = []
        for i in range(len(self.device_list)):
            appium_t = threading.Thread(target=self.start_server, args=(i, ))
            print("id: ", i)
            appium_list.append(appium_t)
        [i.start() for i in appium_list]


if __name__ == '__main__':
    s = Server()
    print(s.main())