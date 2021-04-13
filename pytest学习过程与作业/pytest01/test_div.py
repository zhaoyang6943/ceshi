from pytest学习过程与作业.pytest01.Calculator import Calculator
import pytest
import yaml


def get_div_datas():
    try:
        with open("./datas/data_div.yaml", encoding='utf-8')as f:
            datas = yaml.safe_load(f)
            return datas
            # safe_load(stram),传入的是文件流，所以将打开的yam文件流传入；
            # 目的就是将yam对象，转化为python对象
    except FileNotFoundError:
        with open("../datas/data_div.yaml", encoding='utf-8')as f:
            datas = yaml.safe_load(f)
            return datas

class TestDiv:

    def setup_class(self):
        print("我只执行一次开始！----------------------》")
        self.calc = Calculator()

    def teardown_class(self):
        print("我只执行一次结束！----------------------》")

    def setup(self):
        print("开始计算除法！")

    def teardown(self):
        print("除法计算结束！")

    @pytest.mark.parametrize('a,b,c', [
        [9, 1, 9.0],
        [99, 33, 3.0],
        [99999999, 9, 11111111]
    ], ids=['small', 'medium', 'large'])
    def test_div_int(self, a, b, c):
        '''这个是参数化，没有使用yaml'''
        assert c == self.calc.div(a, b)

    @pytest.mark.parametrize('a,b,c', get_div_datas())
    def test_div_yaml(self, a, b, c):
        '''这个是使用yaml的除法法用例'''
        assert c == self.calc.div(a, b)

    @pytest.mark.parametrize('b', [5, -5, 0.5, -0.5, 0])
    @pytest.mark.parametrize('a', [5, -5, 0.5, -0.5, 0])
    def test_div_cartesian_product(self, a, b):
        '''笛卡尔积进行除法中，正负数，小数类型的计算，数据很少！'''
        try:
            c = a / b  # 原谅我偷懒....
            print(c)
            assert c == self.calc.div(a, b)
        except ZeroDivisionError:
            print("0 cannot be divided")


"""
    # 笛卡尔积：经常用于接口
    @pytest02.mark.parametrize('a',[1,2,3,4])
    @pytest02.mark.parametrize('b',[10,20,30,40])
    def test_interface(self,a,b):
        '''这个是练习，不是作业！'''
        c=str(a*b)
        print('a*b='+c)
"""
