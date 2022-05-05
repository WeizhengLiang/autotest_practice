# coding=utf-8

"""
------------------------------------
@Time : 2022/05/01
@Auth : Weizheng Liang
@File : unit.py
@purpose：封装浏览器启动和关闭操作，元素路径等
@IDE  : PyCharm
------------------------------------
"""

import unittest
import warnings
from selenium.webdriver.common.by import By
from common.driver import open_browser


class Unit(unittest.TestCase):

    account_profile_dropdown = (By.XPATH, "//button[@class='dropdown-icon']")
    my_account_btn_hidden = (By.XPATH, "//div[@id='option-0--menu--1']")

    # page1
    account_profile_dropdown_text = (By.XPATH, "//button[@class='dropdown-icon']/span[1]/b")

    # page2
    actual_username = (By.XPATH, "//span[@class='name']")
    actual_jobtitle = (By.XPATH, "//div[@class='job-title']")
    actual_location = (By.XPATH, "//div[@class='job-location']")
    actual_account_owner_label = (By.XPATH, "//span[@class='account-owner-label']")
    actual_role = (By.XPATH, "//div[@class='role']")
    actual_email = (By.XPATH, "//div[@class='contact-information']/div[2]")
    actual_phone = (By.XPATH, "//div[@class='contact-information']/div[3]")
    actual_user_status = (By.XPATH, "//div[@class='user-status-column']/div[2]")

    # page3
    # get the first user info
    my_setting_btn_hidden = (By.XPATH, "//div[@id='option-2--menu--1']")
    setting_name_order_btn = (By.XPATH, "//button[@id='userNameOrderButton']")
    setting_name_order_btn_text = (By.XPATH, "//button[@id='userNameOrderButton']/i")
    actual_setting_username = (By.XPATH, "//span[@class='user-list-avatar'][1]/span[2]")
    actual_setting_ownerlabel = (By.XPATH, "//span[@class='account-owner-label user-name-label'][1]")
    actual_setting_jobtitle = (By.XPATH, "//span[@class='user-title'][1]")
    actual_setting_role = (By.XPATH, "//tr[@class='ant-table-row ant-table-row-level-0 table-user-row'][1]/td[@class='ant-table-cell account-specific-user-role-box']")
    actual_setting_status = (By.XPATH, "//span[@id='statusFilter'][1]")

    driver = None

    @classmethod
    def setUpClass(cls):
        # 忽略告警信息
        warnings.simplefilter('ignore', ResourceWarning)
        cls.driver = open_browser()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()
