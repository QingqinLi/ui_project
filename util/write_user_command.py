# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import yaml


class WriteUserCommand:
    def __init__(self):
        self.path = "/Users/qing.li/PycharmProjects/AppiumPython/config/userconfig.yaml"

    def get_data(self):
        # 加载文件
        with open(self.path) as f:
            data = yaml.full_load(f)
        return data

    def get_value(self, key, port):
        data = self.get_data()
        return data[key][port]

    def write_data(self, i, device_name, bp, port):

        data = self.join_data(i, device_name, bp, port)
        with open(self.path, "a") as f:
            yaml.dump(data, f)

    def join_data(self, i, device_name, bp, port):
        data = {'user_info_' + str(i): {'bp': str(bp), 'deviceName': device_name, 'port': str(port)}}
        return data

    def clear_data(self):
        with open(self.path, 'w') as f:
            f.truncate()
        f.close()

    def get_file_lines(self):
        data = self.get_data()
        return len(data)


if __name__ == '__main__':
    w = WriteUserCommand()
    print(w.get_value("user_info_1", "port"))