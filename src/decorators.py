from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """
    Автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    """
    def my_decorator(func: Callable) -> Callable:
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            text = ""
            try:
                result = func(*args, **kwargs)
                text = f"{func.__name__} ok"
                return result
            except Exception as error:
                text = f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}"
                raise error
            finally:
                if filename:
                    with open("../mylog.txt", "a") as file:
                        file.write(text + "\n")
                else:
                    print(text)

        return wrapper

    return my_decorator


@log(filename="../mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)

