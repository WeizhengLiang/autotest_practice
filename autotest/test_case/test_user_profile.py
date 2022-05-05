# coding=utf-8

"""
------------------------------------
@Time : 2022/05/01
@Auth : Weizheng Liang
@File : test_user_profile.py
@purpose：测试用例
@IDE  : PyCharm
------------------------------------
"""
import time
import unittest
from common import unit
from config import variable
from common.login import LoginPage


class TestCase(unit.Unit):

    def catchAssertionError(self, exp, act):
        expected = exp

        time.sleep(2)

        actual = act
        try:
            self.assertEqual(expected, actual)
        except AssertionError as e:
            print("该用例未通过")
            result = '不通过'
            raise e
        else:
            print("该用例通过")
            result = '通过'

    def test_case101_menu_corner_username(self):
        """
        测试用户主页面右上角的username
        """
        LoginPage(self.driver).login()
        time.sleep(2)

        self.catchAssertionError(f"{variable.user_firstName} {variable.user_lastName}",
                                 LoginPage(self.driver).find_element(*self.account_profile_dropdown_text).text)

    def test_case201_username(self):
        """
        测试用户profile username
        """
        LoginPage(self.driver).find_element(*self.account_profile_dropdown).click()
        time.sleep(1)
        LoginPage(self.driver).find_element(*self.my_account_btn_hidden).click()
        time.sleep(1)
        self.catchAssertionError(f"{variable.user_firstName} {variable.user_lastName}",
                                          LoginPage(self.driver).find_element(*self.actual_username).text)

    def test_case202_jobtitle(self):
        """
        测试用户profile jobtitle
        """
        self.catchAssertionError(variable.user_job_title,
                                          LoginPage(self.driver).find_element(*self.actual_jobtitle).text)

    def test_case203_location(self):
        """
        测试用户profile location
        """
        self.catchAssertionError(variable.user_location,
                                          LoginPage(self.driver).find_element(*self.actual_location).text)

    def test_case204_ownerlabel(self):
        """
        测试用户profile owner label
        """
        self.catchAssertionError(variable.account_owner_label,
                                          LoginPage(self.driver).find_element(*self.actual_account_owner_label).text)

    def test_case205_role(self):
        """
        测试用户 profile role
        """
        self.catchAssertionError("Account Specific Role: " + variable.user_role,
                                 LoginPage(self.driver).find_element(*self.actual_role).text)

    def test_case206_email(self):
        """
        测试用户profile email
        """
        self.catchAssertionError(variable.user_email_address,
                                          LoginPage(self.driver).find_element(*self.actual_email).text)

    def test_case207_phoneNum(self):
        """
        测试用户 profile phone number
        """
        self.catchAssertionError(variable.user_phone_numder,
                                          LoginPage(self.driver).find_element(*self.actual_phone).text)


    def test_case208_user_status(self):
        """
        测试用户 profile user status
        """
        self.catchAssertionError(variable.user_status,
                                          LoginPage(self.driver).find_element(*self.actual_user_status).text)


    def test_case301_username(self):
        """
        测试用户 settings page user status
        """

        LoginPage(self.driver).find_element(*self.account_profile_dropdown).click()
        time.sleep(1)
        LoginPage(self.driver).find_element(*self.my_setting_btn_hidden).click()
        time.sleep(1)

        if LoginPage(self.driver).find_element(*self.setting_name_order_btn_text).get_attribute('class') == 'user-sort-descent':
            pass
        else:
            LoginPage(self.driver).find_element(*self.setting_name_order_btn).click()

        self.catchAssertionError(f"{variable.user_firstName} {variable.user_lastName}",
                                 LoginPage(self.driver).find_element(*self.actual_setting_username).text)

    def test_case302_ownerlabel(self):
        """
        测试用户 settings page user onwner label
        """
        self.catchAssertionError(variable.account_owner_label,
                                 LoginPage(self.driver).find_element(*self.actual_setting_ownerlabel).text)

    def test_case303_jobtitle(self):
        """
        测试用户 settings page user job title
        """
        self.catchAssertionError(variable.user_job_title,
                                 LoginPage(self.driver).find_element(*self.actual_setting_jobtitle).text)

    def test_case304_role(self):
        """
        测试用户 settings page user role
        """
        self.catchAssertionError(variable.user_role,
                                 LoginPage(self.driver).find_element(*self.actual_setting_role).text)

    def test_case305_status(self):
        """
        测试用户 settings page user account status
        """
        self.catchAssertionError(variable.user_status,
                                 LoginPage(self.driver).find_element(*self.actual_setting_status).text)


if __name__ == '__main__':
    unittest.main()
