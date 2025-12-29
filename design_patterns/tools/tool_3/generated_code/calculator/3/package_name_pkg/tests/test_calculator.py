import pytest
from package_name.calculator import calculator

def test_add():
    assert calculator(5, 3, 'add') == 8
    assert calculator(-1, 1, 'add') == 0
    assert calculator(2.5, 3.5, 'add') == 6.0

def test_sub():
    assert calculator(5, 3, 'sub') == 2
    assert calculator(1, 5, 'sub') == -4
    assert calculator(5.5, 2.5, 'sub') == 3.0

def test_mult():
    assert calculator(5, 3, 'mult') == 15
    assert calculator(-2, 3, 'mult') == -6
    assert calculator(2.5, 4, 'mult') == 10.0

def test_div():
    assert calculator(6, 3, 'div') == 2
    assert calculator(5, 2, 'div') == 2.5
    assert calculator(-10, 2, 'div') == -5

def test_div_by_zero():
    with pytest.raises(ValueError, match='Division by zero'):
        calculator(5, 0, 'div')

def test_invalid_operation():
    with pytest.raises(ValueError, match='Invalid operation'):
        calculator(5, 3, 'invalid')
