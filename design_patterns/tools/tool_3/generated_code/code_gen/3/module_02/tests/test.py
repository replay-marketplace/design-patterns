import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from module_02 import mult

def test_mult():
    assert mult(2, 3) == 6
    assert mult(0, 5) == 0
    assert mult(-1, 4) == -4
    assert mult(-2, -3) == 6
    print("All tests passed for mult.")

if __name__ == "__main__":
    test_mult()