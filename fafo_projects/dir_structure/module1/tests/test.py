from module1 import add, sub


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 0) == 0
    assert sub(1, 1) == 0


if __name__ == "__main__":
    test_add()
    test_sub()
    print("All tests passed!")

