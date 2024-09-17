import pytest
from src.decorators import log


def test_log():
    @log(filename="../mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open("../mylog.txt", "r") as file:
        for i in file:
            result = i
    assert result == 'my_function ok\n'


def test_log_error():
    @log(filename="../mylog.txt")
    def my_function(x, y):
        raise TypeError
    with pytest.raises(TypeError):
        my_function(1, 2)

    with open("../mylog.txt", "r") as file:
        for i in file:
            result = i
    assert result == 'my_function error: . Inputs: (1, 2), {}\n'


# def test_log_cons(capsys):
#     @log()
#     def my_function(x, y):
#         return x + y
#     with pytest.raises(TypeError):
#         my_function(1, 2)
#
#     assert result == 'my_function error: . Inputs: (1, 2), {}\n'