from calculator import Calculator 

tests = Calculator()

def test_addition():
    assert tests.addition(0, 5) == 5
    assert tests.addition(5, 10) == 15
    assert tests.addition(10, 20) == 30

def test_subtraction():
    assert tests.addition(0, 5) == -5
    assert tests.addition(10, 20) == -10
    assert tests.addition(10, 5) == 5

def test_multiplication():
    assert tests.addition(0, 5) == 0
    assert tests.addition(5, 5) == 25
    assert tests.addition(7, 2) == 14

def test_division():
    assert tests.addition(0, 5) == 0
    assert tests.addition(4, 2) == 2
    assert tests.addition(12, 4) == 3

def test_root():
    assert tests.addition(4, 2) == 2
    assert tests.addition(125, 3) == 5
    assert tests.addition(81, 4) == 3
