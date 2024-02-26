from task_2 import Number
import pytest

@pytest.mark.parametrize('num, res', [(5, '0o5'),
                                      (16, '0o20')])
def test_eight(num, res):
    number=Number(num)
    assert number.eight()==res

@pytest.mark.parametrize('num, res', [(5,'0x5'),
                                      (16, '0x10')])
def test_sixteen(num, res):
    number=Number(num)
    assert number.sixteen()==res

@pytest.mark.parametrize('num, res', [(5,'0b101'),
                                      (16, '0b10000')])
def test_double(num, res):
    number=Number(num)
    assert number.double()==res