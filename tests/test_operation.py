from src.math_operation import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(5,6) == 11

def test_sub():
    assert sub(5,4) == 1
    assert sub(6,4) == 2

