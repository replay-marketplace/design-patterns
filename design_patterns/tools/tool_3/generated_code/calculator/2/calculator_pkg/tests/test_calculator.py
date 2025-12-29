import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import calculate

def test_add():
    assert calculate(5, 3, 'add') == 8
    assert calculate(-5, 3, 'add') == -2
    assert calculate(0, 0, 'add') == 0
    assert calculate(2.5, 1.5, 'add') == 4.0

def test_sub():
    assert calculate(5, 3, 'sub') == 2
    assert calculate(3, 5, 'sub') == -2
    assert calculate(0, 0, 'sub') == 0
    assert calculate(2.5, 1.5, 'sub') == 1.0

def test_mult():
    assert calculate(5, 3, 'mult') == 15
    assert calculate(-5, 3, 'mult') == -15
    assert calculate(0, 5, 'mult') == 0
    assert calculate(2.5, 2, 'mult') == 5.0

def test_div():
    assert calculate(6, 3, 'div') == 2
    assert calculate(5, 2, 'div') == 2.5
    assert calculate(-6, 3, 'div') == -2
    assert calculate(0, 5, 'div') == 0

def test_div_by_zero():
    try:
        calculate(5, 0, 'div')
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"

def test_invalid_operation():
    try:
        calculate(5, 3, 'invalid')
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Invalid operation. Supported operations: 'add', 'sub', 'mult', 'div'"

