import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src import calculate

def test_calculate():
    assert calculate(2, 3, 'add') == 5
    assert calculate(2, 3, 'mult') == 6
    assert calculate(0, 5, 'add') == 5
    assert calculate(0, 5, 'mult') == 0
    assert calculate(-1, 4, 'add') == 3
    assert calculate(-1, 4, 'mult') == -4
    print("All tests passed for calculate.")

if __name__ == "__main__":
    test_calculate()