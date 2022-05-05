# coding=utf-8

"""
------------------------------------
@Time : 2022/05/01
@Auth : Weizheng Liang
@File : run_all_test_case.py
@purpose：执行所有测试用例
@IDE  : PyCharm
------------------------------------
"""

import unittest
from HTMLTestRunner import HTMLTestRunner
import os

current_path = os.getcwd()  # 当前文件路径
case_path = os.path.join(current_path, "test_case")  # 用例路径
# 存放报告路径
report_path = os.path.join(current_path, "report")


# discover找出以test开头的用例
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, "test_user*.py")
    return discover


if __name__ == "__main__":
    # 测试报告为report.html
    result_path = os.path.join(report_path, "report.html")

    # 打开文件，把结果写进文件中，w，有内容的话，清空了再写进去
    fp = open(result_path, "wb")

    runner = HTMLTestRunner(stream=fp,
                            title="UI自动化测试报告",
                            description="用例执行情况")

    # 调用all_case函数返回值
    runner.run(all_case())

    # 关闭刚才打开的文件
    fp.close()



