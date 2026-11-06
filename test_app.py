
from app import add, subtract

def test_addition():
    assert add(5, 3) == 8

def test_subtraction():
    assert subtract(10, 4) == 6

def test_addition_with_zero():
    assert add(5, 0) == 5
