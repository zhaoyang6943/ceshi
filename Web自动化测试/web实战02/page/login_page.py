"""
__author__ == 'zhaoyang'
__time__ = '2021-04-21 21:31'
"""
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from Web自动化测试.web实战02.page.register_page import RegisterPage


class TestLoginPage:
    """
    我不需要集成BasePage，我是独立的复用操作，下面的返回注册页面（goto_regsiter），请当做一个笑话
    ps  ：  “暂且当做 TestLoginPage 的PO，当做登录成功的样子”  ！！！
    """
    def test_do_login(self):
        """
        chrome --remote-debugging-port=9222
        手动，开启复用，拿取cookies后，进行执行用例！本身不执行pytest，毕竟不是test_开头的文件！
        进行扫码登录，保存cookies
        ps  ：  “暂且当做do_login的PO，当做登录成功的样子”  ！！！
        :return:
        """
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        # 在当前页面调试
        self.driver.find_element(By.ID, "menu_contacts").click()
        # 1. 手动复制 出，打印获取的cookies，给到  “test_cookie”  方法中使用
        print(self.driver.get_cookies())

        # 2. 存入文本, "w" 是覆盖写入， “test_cookies_V2” 使用的是存入yaml中的cookies，读出来
        cookie = self.driver.get_cookies()
        try:
            with open("../datas/data.yaml", "w", encoding="UTF-8") as f:
                # 导入yaml，将获取的cookie存进去；
                yaml.dump(cookie, f)
        except FileNotFoundError:
            # 从第一级项目调用test用例时，可能会出现~~~~~~~~~~~
            with open("./datas/data.yaml", "w", encoding="UTF-8") as f:
                # 导入yaml，将获取的cookie存进去；
                yaml.dump(cookie, f)

    def goto_regsiter(self):
        """
        返回注册页面
        :return:
        """
        return RegisterPage()
