import pytest
import sys

print(sys.path)


# @pytest.mark.run(order=1)  # 自己改写顺序，需要去装饰器，conftest中pytest_collection_modifyitems改写。
def test_yang():
    assert True


class TestAdd:

    # 测试修改pytest_collection_modifyitems钩子函数后，编码格式有没有效果！
    @pytest.mark.parametrize('a,b,c', [[1, 2, 3]], ids=['小数字'])
    def test_add_1(self, a, b, c, initcalc_class):
        assert c == initcalc_class.add(a, b)
