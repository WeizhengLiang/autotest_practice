# coding=utf-8

"""
------------------------------------
@Time : 2022/05/01
@Auth : Weizheng Liang
@File : base.py
@purpose：页面操作封装
@IDE  : PyCharm
------------------------------------
"""


from selenium.webdriver.support.wait import WebDriverWait
from config.read_config import ReadConf


class BasePage(object):
    # 读取config.ini配置文件,传入test config值
    url = ReadConf()
    # 传入test config模块
    test_url = url.readConf("test config")
    # 这里传入test config模块中的url
    base_url = test_url['login_url']
    print()

    def __init__(self, driver, test_config=base_url):

        self.driver = driver
        self.url = test_config
        self.driver.implicitly_wait(5)

    def open_url(self):
        url = self.url
        print(url)
        self.driver.get(url)
        title = self.driver.title
        print("项目名称：", title)
        print("项目地址：", self.driver.current_url)

    def close(self):
        self.driver.quit()

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print("元素在页面中未找到！", *loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            # getattr相当于self.loc
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.mouse_click(loc)  # 调用鼠标点击事件方法
            if clear_first:
                self.mouse_clear(loc)  # 调用鼠标清理事件方法
                self.find_element(*loc).send_keys(value)
        except ArithmeticError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def mouse_click(self, loc):
        return self.find_element(*loc).click()









