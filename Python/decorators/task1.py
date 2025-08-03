"""
   1 задание
"""

from datetime import datetime
import sys


def my_write(string_text: str) -> int:
    """
    Переопределённая функция записи в stdout, которая добавляет
    временную метку перед каждой строкой (кроме пустых строк).

    :param string_text: Текст для записи в стандартный вывод.
    :return: Количество символов, записанных в исходный stdout.
    """
    final_text = string_text
    if string_text != "\n":
        final_text = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]: ") + final_text
    original_write(final_text)
    return len(string_text)


if __name__ == "__main__":
    original_write = sys.stdout.write
    sys.stdout.write = my_write
    print("1, 2, 3")
    sys.stdout.write = original_write
