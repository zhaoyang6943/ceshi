
from Calculator import Calculator
import pytest


class TestAdd:

    def setup(self):
        self.calc = Calculator()
        print("开始！")

    def teardown(self):
        print("结束！")

    @pytest.mark.parametrize('a,b,c',[
        [1,1,2],
        [10,10,20],
        [999999,999999,1999998]
    ],ids=['small','medium','large'])
    def test_add_int(self,a,b,c):
        assert c == self.calc.add(a,b)

    def test_add_float(self):
        calc = Calculator()
        assert 2.0221 == calc.add(1.01,1.0121)

    def test_add_bignumber(self):
        assert 2 == self.calc.add(1,1)

    # 笛卡尔积：经常用于接口
    @pytest.mark.parametrize('a',[1,2,3,4])
    @pytest.mark.parametrize('b',[10,20,30,40])
    def test_interface(self,a,b):
        c=str(a*b)
        print('a*b='+c)