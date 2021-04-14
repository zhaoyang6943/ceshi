"""
__author__ == 'zhaoyang'
__time__ = '2021-04-14 16:38'
"""


from selenium import webdriver


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
