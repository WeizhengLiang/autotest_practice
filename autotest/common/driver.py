# coding=utf-8

"""
------------------------------------
@Time : 2022/05/01
@Auth : Weizheng Liang
@File : driver.py
@purpose：浏览器设置，默认chrome
@IDE  : PyCharm
------------------------------------
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# 默认chrome
browser_type = "Chrome"


def open_browser():

    global driver
    if browser_type == 'Firefox':
        driver = webdriver.Firefox()
    elif browser_type == 'Chrome':
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        # driver = webdriver.Chrome()
    elif browser_type == 'IE':
        driver = webdriver.Ie()
    elif browser_type == '':
        driver = webdriver.Chrome()
    return driver


if __name__ == '__main__':
    driver = open_browser()
