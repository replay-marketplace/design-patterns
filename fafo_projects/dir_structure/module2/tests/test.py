from module2 import calculate


def test_calculate_add():
    assert calculate(2, 3, "add") == 5
    assert calculate(0, 0, "add") == 0
    assert calculate(-1, 1, "add") == 0


def test_calculate_sub():
    assert calculate(5, 3, "sub") == 2
    assert calculate(0, 0, "sub") == 0
    assert calculate(1, 1, "sub") == 0


if __name__ == "__main__":
    test_calculate_add()
    test_calculate_sub()
    print("All tests passed!")
