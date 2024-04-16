from calculator import addition

def test_addition():
    assert addition(1, 2) == 3

from calculator import substraction

def test_substraction():
    assert substraction(1, 2) == -1

from calculator import division

def test_division():
    assert division(1, 2) == 0.5