import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from module_01 import add

def test_add():
    assert add(2, 3) == 5
    assert add(0, 5) == 5
    assert add(-1, 4) == 3
    assert add(-2, -3) == -5
    print("All tests passed for add.")

if __name__ == "__main__":
    test_add()