import pytest
from src.decorators import log


def test_log(capsys):
    @log(filename="../mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open("../mylog.txt", "r") as file:
        for i in file:
            result = i
    assert result == 'my_function ok\n'


def test_log_error(capsys):
    @log(filename="../mylog.txt")
    def my_function(x, y):
        raise TypeError
    with pytest.raises(TypeError):
        my_function(1, 2)

    with open("../mylog.txt", "r") as file:
        for i in file:
            result = i
    assert result == 'my_function error: . Inputs: (1, 2), {}\n'


def test_log_to_console(capsys):
    @log(filename="../mylog.txt")
    def my_function(x, y):
        captured = capsys.readouterr()
        assert captured.out.strip() == "my_function ok\n"
