"""
   2 задание
"""

from datetime import datetime
import sys
from typing import Callable, Any


def timed_output(function: Callable) -> Callable:
    """
    Декоратор, добавляющий временные метки к выводу print внутри декорируемой функции.

    :param function: Функция, для которой нужно добавить временные метки к стандартному выводу.
    :return: Обёрнутая функция с модифицированным выводом.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Обёртка, заменяющая sys.stdout.write для добавления временных меток.

        :param args: Позиционные аргументы для декорируемой функции.
        :param kwargs: Именованные аргументы для декорируемой функции.
        :return: Результат выполнения декорируемой функции.
        """

        def my_write(string_text: str) -> int:
            """
            Переопределённая функция записи в stdout, добавляющая временную метку.

            :param string_text: Текст для записи в стандартный вывод.
            :return: Количество символов, записанных в stdout.
            """
            final_text = string_text
            if string_text != "\n":
                final_text = (
                    datetime.now().strftime("[%Y-%m-%d %H:%M:%S]: ") + final_text
                )
            original_write(final_text)
            return len(string_text)

        original_write = sys.stdout.write
        sys.stdout.write = my_write
        try:
            ans = function(*args, **kwargs)
        finally:
            sys.stdout.write = original_write
        return ans

    return wrapper


@timed_output
def print_greeting(name: str) -> None:
    """
    Пример функции для демонстрации декоратора. Выводит приветствие с именем.

    :param name: Имя пользователя для приветствия.
    """
    print(f"Hello, {name}!")


if __name__ == "__main__":
    print_greeting("Nikita")
