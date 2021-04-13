import pytest


# pip install pytest-ordering
# 控制用例的执行顺序
# 也有映射first，second

# @pytest.mark.run(order=3)  # 自己改写顺序，需要去装饰器，conftest中pytest_collection_modifyitems改写。
def test_foo():
    assert True


# @pytest.mark.run(order=2)  # 自己改写顺序，需要去装饰器，conftest中pytest_collection_modifyitems改写。
def test_bar():
    assert True
