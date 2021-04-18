"""
__author__ == 'zhaoyang'
__time__ = '2021-04-18 21:44'
"""
# 作业：使用序列化cookie的方式登录企业微信，完成添加成员操作
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHomework:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_homework(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("../datas/data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)


        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 开始添加成员：
        print("123")

        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@class='ww_operationBar']/a[1]")))
        sleep(3)
        self.driver.find_element(By.XPATH,"//*[@class='ww_operationBar']/a[1]").click()
        print("456")
        self.driver.find_element(By.ID,"username").click()
        self.driver.find_element(By.ID,"username").send_keys("yang")
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("0001")
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys("18217276901")
        self.driver.find_element(By.XPATH,"//*[@class='member_colRight_operationBar ww_operationBar'][2]/a[2]").click()
        sleep(5)
        list = []
        eles = self.driver.find_elements(By.XPATH,"//*[@id='member_list']/tr/td[5]")
        for num in eles:
            list.append(num.text)  # 元素的text才是真正的手机号！
        print(list)
        assert "18217276901" in list


