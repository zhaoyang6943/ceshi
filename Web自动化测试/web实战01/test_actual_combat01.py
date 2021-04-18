"""
__author__ == 'zhaoyang'
__time__ = '2021-04-18 21:42'
"""
# 复用浏览器：chrome --remote-debugging-port=9222
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAcactualCombat:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").click()
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, "su").click()
        sleep(30)
        ele = self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院 – 软件自动化测试开发培训_接口性能测试")
        assert ele


# 以上代码有什么问题？
# 回答：


# 复用浏览器;(ps:只支持chrome浏览器！！！)
class TestWework:

    # 测试复用浏览器是否成功调用起来，并保存cookies信息，放入datas文件夹中
    def test_wework(self):
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

    # 将上面的获取的cookies手动复制下，放入下面的cookies下
    def test_cookie(self):
        driver = webdriver.Chrome()
        # selenium是有默认的域名的，所以在添加cookies时，需要先打开需要打开的页面，在传入cookies
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        cookies = [
            {'domain': '.qq.com', 'expiry': 1618750337, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851250135332'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'cnqguHCplKqroZ8ND_nawXqXT4qAoNfzQ0JwRJTjNsaaz9L9ygVFexwW0afaec_ROEgzboG5s8Tn34XpiYffHnzuIsu1wevm6XofrkKMK-djpjjUaQwPzwGfEIasjtpvpjJxoy7NBXMCDkbwr3lu4kcmVsqCrITaPLb1-yFnqpfoNAg9bgHl50ADfmv6CAKwFVI9VyJzeF1yNzm4ovzfSf3SaO8S5M_aS4EkGbOw-E3q_SNK4emcQUJW4beJIYjVty-A1yntnbsUeQ1CTXXsMg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851250135332'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324975447575'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'i0taducRALQYz292y83iG2u71oFZflh6ScAogtbTXCWr-P7Na8fyzARKgAGnlP7y'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a5505597'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '18615683572723591'},
            {'domain': '.qq.com', 'expiry': 1618836337, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.862345709.1618748558'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1618780093, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '5ins011'},
            {'domain': '.qq.com', 'expiry': 1620544865, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '2467346003@qq.com'},
            {'domain': '.qq.com', 'expiry': 1650088188, 'httpOnly': True, 'name': 'ied_qq', 'path': '/',
             'secure': False, 'value': 'o1013925784'},
            {'domain': '.qq.com', 'expiry': 1650088188, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': False, 'value': 'c1B6A1m8I5H5L2L1Z8y8f7U2f4'},
            {'domain': '.qq.com', 'expiry': 1681821937, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1070295580.1618390957'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1649926861, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1649926956, 'httpOnly': False,
                                  'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                  'value': '1618390956'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '1361662620'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1621342283, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '051078c62e64faacc6245f5489aa052b8a7a0eb5571029c3918a41954f41e7bc'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'DeYpOjtqWO'}]
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(5)


# 以上代码有问题吗？
# 回答：1. cookies太长；不能跨脚本调用！！！



def test_cookies_V2():
    # 实例化 driver
    driver = webdriver.Chrome()
    # 访问 扫码登录页面
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open("../datas/data.yaml",encoding="UTF-8") as f:
        yaml_data =  yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)

    # 访问通讯录页面
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

# 扩展：
# 1. 当从chrome浏览器获取到cookies后，firefox是否可以用这个cookies呢？
# 2. 如果多个账号登录，保存多个账号的cookies，如果某个cookies过期，自动调用其他cookies
# 3.

