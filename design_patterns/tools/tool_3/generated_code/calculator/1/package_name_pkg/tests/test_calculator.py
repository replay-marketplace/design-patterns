import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'package_name')))

from calculator import calculator

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
    try:
        calculator(5, 0, 'div')
        assert False, "Expected ValueError for division by zero"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"

def test_invalid_operation():
    try:
        calculator(5, 3, 'invalid')
        assert False, "Expected ValueError for invalid operation"
    except ValueError as e:
        assert str(e) == "Invalid operation. Use 'add', 'sub', 'mult', or 'div'."
