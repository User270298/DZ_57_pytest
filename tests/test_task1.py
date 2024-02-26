from task_1 import Numbers
import pytest


@pytest.mark.parametrize('lst, res', [([3, 3], 6),
                                      ([9, 1], 10)])
def test_summ(lst, res):
    number = Numbers(lst)
    assert number.summ() == res


@pytest.mark.parametrize('lst, res', [([3, 3], 2),
                                      ([9, 1], 2)])
def test_summ(lst, res):
    number = Numbers(lst)
    assert number.middle() == res


@pytest.mark.parametrize('lst, res', [([3, 5], 5),
                                      ([9, 1], 9)])
def test_summ(lst, res):
    number = Numbers(lst)
    assert number.maximum() == res


@pytest.mark.parametrize('lst, res', [([10, 3], 3),
                                      ([9, 1], 1)])
def test_summ(lst, res):
    number = Numbers(lst)
    assert number.minimum() == res
