# coding=utf-8

"""
------------------------------------
@Time : 2022/05/01
@Auth : Weizheng Liang
@File : read_config.py
@purpose：读取config文件
@IDE  : PyCharm
------------------------------------
"""

import configparser
import os


class ReadConf:

    def __init__(self):
        current_path = os.path.dirname(os.path.relpath(__file__))
        # 获取配置文件路径
        config_path = os.path.join(current_path, "config.ini")
        # 创建管理对象
        self.conf = configparser.ConfigParser()
        # 读ini文件
        self.conf.read(config_path, encoding="utf-8")

    def readConf(self, param):
        # 获取某个section中的所有值,将其转化为字典
        items = dict(self.conf.items(param))
        return items


if __name__ == '__main__':
    test = ReadConf()
    test_elements = test.readConf("test config")  # 传入test config的值
    print('test元素为： ', test_elements)

