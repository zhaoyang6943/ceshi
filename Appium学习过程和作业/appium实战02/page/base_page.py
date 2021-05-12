"""
__author__ == 'zhaoyang'
__time__ = '2021-05-10 21:29'
"""

# 基类，init的一些操作放入里面
# 封装一些最基本的方法，便于后期维护
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

import logging

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("../logs/info.log",encoding='utf-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


logger.addHandler(handler)

# logging.basicConfig(
#             # 日志级别
#             level=logging.INFO,
#             # 日志格式
#             # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
#             format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#             # 打印日志的时间
#             datefmt='%a, %d %b %Y %H:%M:%S',
#             # 日志文件存放的目录（目录必须存在）及日志文件名
#             filename='report.log',
#             # 打开日志文件的方式
#             filemode='w'
#         )


class BasePage:

    def __init__(self, driver: WebDriver=None):
        # 初始化driver
        self.driver = driver

        self.logging = logger

    def find(self, by, value):

        self.logging.info(by)
        self.logging.info(value)

        return self.driver.find_element(by, value)

    def swipe_find(self, text, num=5):
        # num 默认查找次数

        self.driver.implicitly_wait(1)
        for i in range(0, num):
            if i == num - 1:
                self.logging.info(f"找了{i}次，未找到")
                raise NoSuchElementException(f"找了{i}次，未找到")

            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[contains(@text,'{text}')]")
                self.driver.implicitly_wait(5)
                # 如果找到了这个元素，则返回
                return element
            except NoSuchElementException:
                self.logging.info("未找到，滑动")
                print("未找到，滑动")
                # "滑动一页，继续查找

                # 屏幕尺寸会返回一个宽和高
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']
                # 'width' , 'height'
                start_x = width / 2
                start_y = height * 0.8

                # 从下往上滑动，x轴是没有变化的
                end_x = start_x
                end_y = height * 0.3

                duration = 2000  # ms
                # 最终完成滑动的操作
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
