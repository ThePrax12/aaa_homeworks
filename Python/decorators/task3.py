"""
   3 задание
"""

import sys
from typing import Callable, Any


def redirect_output(filepath: str) -> Callable:
    """
    Декоратор, перенаправляющий вывод print из декорируемой функции в указанный файл.

    :param filepath: Путь к файлу, куда будет перенаправлен вывод.
    :return: Обёрнутый декоратор, изменяющий стандартный вывод.
    """

    def decorator(function: Callable) -> Callable:
        """
        Декоратор для замены sys.stdout на файл во время выполнения декорируемой функции.

        :param function: Функция, вывод которой нужно перенаправить.
        :return: Обёрнутая функция с перенаправлением вывода.
        """

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обёртка, перенаправляющая вывод из sys.stdout в указанный файл.

            :param args: Позиционные аргументы для декорируемой функции.
            :param kwargs: Именованные аргументы для декорируемой функции.
            :return: Результат выполнения декорируемой функции.
            """
            original_stdout = sys.stdout
            try:
                with open(filepath, "w", encoding="utf-8") as output_file:
                    sys.stdout = output_file
                    return function(*args, **kwargs)
            finally:
                sys.stdout = original_stdout

        return wrapper

    return decorator


@redirect_output("./function_output.txt")
def calculate() -> None:
    """
    Пример функции для демонстрации декоратора.
    Вычисляет степени чисел от 1 до 20 и выводит их в файл.
    """
    for power in range(1, 5):
        for num in range(1, 20):
            print(num**power, end=" ")
        print()


if __name__ == "__main__":
    calculate()
