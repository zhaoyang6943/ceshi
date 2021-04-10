from Calculator import Calculator
import pytest
import yaml


class TestAdd:

    def setup_class(self):
        print("我只执行一次开始！----------------------》")
        self.calc = Calculator()

    def teardown_class(self):
        print("我只执行一次结束！----------------------》")

    def setup(self):
        print("开始计算加法！")

    def teardown(self):
        print("加法计算结束！")

    @pytest.mark.parametrize('a,b,c',[
        [1,1,2],
        [10,10,20],
        [999999,999999,1999998]
    ],ids=['small','medium','large'])
    def test_add_int(self,a,b,c):
        '''这个是参数化，没有使用yaml'''
        assert c == self.calc.add(a,b)

    @pytest.mark.parametrize('a,b,c',yaml.safe_load(open("./data_add.yaml")))
    def test_add_yaml(self,a,b,c):
        '''这个是使用yaml的加法用例'''
        # print(a,b,type(a),type(b))
        assert c == self.calc.add(a,b)

    @pytest.mark.parametrize('b', [5, -5, 0.5, -0.5,0])
    @pytest.mark.parametrize('a', [5, -5, 0.5, -0.5,0])
    def test_add_cartesian_product (self,a,b):
        '''笛卡尔积进行加法中，正负数，小数类型的计算，数据很少！'''
        c = a+b  # 原谅我偷懒....
        print(c)
        assert c == self.calc.add(a,b)

"""
    # 笛卡尔积：经常用于接口
    @pytest.mark.parametrize('a',[1,2,3,4])
    @pytest.mark.parametrize('b',[10,20,30,40])
    def test_interface(self,a,b):
        '''这个是练习，不是作业！'''
        c=str(a*b)
        print('a*b='+c)
"""

