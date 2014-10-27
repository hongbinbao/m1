#!/usr/bin/python
# -*- coding:utf-8 -*- 

from uiautomatorplug.android import device as d
'''
make call
'''
d.server.adb.cmd('shell service call phone 2 s16 "10086"')
