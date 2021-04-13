from pytest学习过程与作业.pytest01.Calculator import Calculator
import pytest
import yaml



def get_add_datas():
    try:
        with open("./datas/data_add.yaml", encoding='utf-8')as f:
            datas = yaml.safe_load(f)
            return datas
            # safe_load(stram),传入的是文件流，所以将打开的yam文件流传入；
            # 目的就是将yam对象，转化为python对象
    except FileNotFoundError:
        with open("../datas/data_add.yaml", encoding='utf-8')as f:
            datas = yaml.safe_load(f)
            return datas


def test_getdatas():
    try:
        with open("./datas/data_add.yaml", encoding='utf-8')as f:
            datas = yaml.safe_load(f)
            return datas
            # safe_load(stram),传入的是文件流，所以将打开的yam文件流传入；
            # 目的就是将yam对象，转化为python对象
    except FileNotFoundError:
        with open("../datas/data_add.yaml", encoding='utf-8')as f:
            datas = yaml.safe_load(f)
            return datas

    print(datas)


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

    @pytest.mark.parametrize('a,b,c', [
        [1, 1, 2],
        [10, 10, 20],
        [999999, 999999, 1999998]
    ], ids=['small', 'medium', 'large'])
    def test_add_int01(self, a, b, c):
        '''这个是参数化，没有使用yaml'''
        assert c == self.calc.add(a, b)

    @pytest.mark.parametrize('a,b,c', get_add_datas()['int_datas'], ids=get_add_datas()['int_ids'])
    def test_add_int02(self, a, b, c):
        '''这个是使用yaml的加法用例'''

        assert c == self.calc.add(a, b)

    @pytest.mark.parametrize('a,b,c', get_add_datas()['float_datas'], ids=get_add_datas()['float_ids'])
    def test_add_float(self, a, b, c):
        assert c == self.calc.add(a, b)

    @pytest.mark.parametrize('a,b,c', get_add_datas()['negative_datas'], ids=get_add_datas()['negative_ids'])
    def test_add_negative(self, a, b, c):
        assert c == self.calc.add(a, b)

    @pytest.mark.parametrize('b', [5, -5, 0.5, -0.5, 0])
    @pytest.mark.parametrize('a', [5, -5, 0.5, -0.5, 0])
    def test_add_cartesian_product(self, a, b):
        '''笛卡尔积进行加法中，正负数，小数类型的计算，数据很少！'''
        c = a + b  # 原谅我偷懒...  真实的实战中，需要对应的数据还是要写的！
        print(c)
        assert c == self.calc.add(a, b)


"""
    # 笛卡尔积：经常用于接口
    @pytest02.mark.parametrize('a',[1,2,3,4])
    @pytest02.mark.parametrize('b',[10,20,30,40])
    def test_interface(self,a,b):
        '''这个是练习，不是作业！'''
        c=str(a*b)
        print('a*b='+c)
"""
