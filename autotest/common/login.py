# coding=utf-8

"""
------------------------------------
@Time : 2022/05/01
@Auth : Weizheng Liang
@File : login.py
@purpose：登陆操作
@IDE  : PyCharm
------------------------------------
"""

from selenium.webdriver.common.by import By
from common.base import BasePage
import time


class LoginPage(BasePage):
    # 定位用户名
    username_loc = (By.XPATH, "//input[@id='input-emailWork']")
    # 用户密码
    password_loc = (By.XPATH, "//input[@id='input-password']")
    # 定位登录按钮
    login_button_loc = (By.XPATH, "//button[@class='commit-button primary-button']")

    def input_username(self, username):  # 输入用户名
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):  # 输入密码
        self.find_element(*self.password_loc).send_keys(password)

    def click_login_button(self):  # 点击登录按钮
        self.find_element(*self.login_button_loc).click()

    def login(self, username='xvchengcheng77+0228@gmail.com', password='EastbayA1914'):
        self.open_url()
        time.sleep(2)
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()
        return self.driver
