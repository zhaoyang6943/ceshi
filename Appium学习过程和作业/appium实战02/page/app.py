"""
__author__ == 'zhaoyang'
__time__ = '2021-05-07 21:29'
"""

# app相关的操作，关闭，启动，重启
from Appium学习过程和作业.appium实战02.page.main_page import MainPage


class App:

    def start(self):
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def goto_main(self):
        # 入口，进去首页
        return MainPage()