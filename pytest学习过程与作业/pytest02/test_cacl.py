"""
__author__ == 'zhaoyang'
__time__ = '2021-04-13 21:14'
"""
import allure
import pytest

"""
上节课的作业，使用fixture 实现setup/teardown 功能
使用fixture 实现 参数化的功能
使用插件完成测试用例顺序的控制
改造测试用例的编码，支持中文编码格式（选做）
添加命令行参数，使用hook插件实现（拔高，选做）???
生成测试 报告截图
"""


@allure.feature("计算器")
class TestCacl:

    @pytest.mark.run(order=7)
    @allure.story("相加-整数")
    def test_add_int(self, get_add_datas2, initcalc_class):
        assert get_add_datas2[2] == initcalc_class.add(get_add_datas2[0], get_add_datas2[1])

    @pytest.mark.run(order=6)
    @allure.story("相加-浮点数")
    def test_add_float(self, get_add_datas_float, initcalc_class):
        assert get_add_datas_float[2] == initcalc_class.add(get_add_datas_float[0], get_add_datas_float[1])

    @pytest.mark.run(order=5)
    @allure.story("相加-负数")
    def test_add_negative(self, get_add_datas_negative, initcalc_class):
        assert get_add_datas_negative[2] == initcalc_class.add(get_add_datas_negative[0], get_add_datas_negative[1])

    @pytest.mark.run(order=4)
    @allure.story("相除-整数")
    def test_div_int(self, get_div_datas_int, initcalc_class):
        assert get_div_datas_int[2] == initcalc_class.div(get_div_datas_int[0], get_div_datas_int[1])

    @pytest.mark.run(order=3)
    @allure.story("相除-浮点数")
    def test_div_float(self, get_div_datas_float, initcalc_class):
        assert get_div_datas_float[2] == initcalc_class.div(get_div_datas_float[0], get_div_datas_float[1])

    @pytest.mark.run(order=2)
    @allure.story("相除-负数")
    def test_div_negative(self, get_div_datas_negative, initcalc_class):
        assert get_div_datas_negative[2] == initcalc_class.div(get_div_datas_negative[0], get_div_datas_negative[1])

    @pytest.mark.run(order=1)
    @allure.story("相除-除数为零")
    def test_div_zero(self, get_div_datas_zero, initcalc_class):
        assert get_div_datas_zero[2] == initcalc_class.div(get_div_datas_zero[0], get_div_datas_zero[1])