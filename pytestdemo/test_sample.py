import pytest
# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

@pytest.mark.login
def test_answer1():
    assert inc(3) == 4