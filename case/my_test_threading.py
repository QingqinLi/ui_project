# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import threading


def sum(a):
    print(a+1)


threads = []
for i in range(5):
    t = threading.Thread(target=sum, args=(i, ))
    threads.append(t)
    print("test")
[t.start() for t in threads]