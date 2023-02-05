import pytest


def getNumber(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "fizz"
    return number


class SimpleData:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b


def classNum(number):
    return number


class TestSample:
    @pytest.mark.parametrize(
        "inputNum,expected", [(1, 1), (3, "fizz"), (5, "buzz"), (15, "FizzBuzz")]
    )
    def test_equal_num(self, inputNum, expected):
        number = getNumber(inputNum)
        assert number == expected

    def test_simple_data(self):
        data = SimpleData(1, 2)
        aaa = data.sum()
        assert aaa == 3
