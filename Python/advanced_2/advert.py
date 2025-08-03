"""
Модуль для рабты с динамическими атрибутами объекта (объявления).
"""

import json
import keyword
from typing import Dict, Any


class ColorizeMixin:
    """
    Миксин для добавления возможности цветовой окраски строки.
    """

    def colorize_str(self, text: str) -> str:
        """
        Окрашивает строку в цвет, определяемый атрибутом repr_color_code.

        Args:
            text (str): Текст, который нужно окрасить.

        Returns:
            str: Окрашенный текст.
        """
        color_code = getattr(self, "repr_color_code", 37)
        return f"\033[{color_code}m{text}\033[0m"


class PreAdvert:
    """
    Класс для преобразования данных из словаря в атрибуты объекта.
    """

    def __init__(self, dictionary: Dict[str, Any]) -> None:
        """
        Инициализирует объект, присваивая атрибуты из словаря.

        Args:
            dictionary (Dict[str, Any]): Словарь с данными для инициализации объекта.
        """
        for key, value in dictionary.items():
            if isinstance(value, dict):
                value = PreAdvert(value)
            if keyword.iskeyword(key):
                key += "_"
            setattr(self, key, value)

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта, представляя все атрибуты.
        Атрибут price обрабатывается отдельно (для добалвения ₽)

        Returns:
            str: Строковое представление объекта.
        """
        text = "|"
        for key, value in self.__dict__.items():
            if isinstance(value, PreAdvert):
                value = value.__str__()
                text += value
            elif key == "_price":
                text += str(value) + " ₽ | "
            else:
                text += str(value) + " | "
        return text


class Advert(ColorizeMixin, PreAdvert):
    """
    Класс для обработки объявления с заголовком, ценой и другими данными.
    Наследует функциональность от ColorizeMixin и Pre_Advert.
    """

    repr_color_code = 33

    def __init__(self, dictionary: Dict[str, Any]) -> None:
        """
        Инициализирует объект. Проверяет цену и наличие заголовка.

        Args:
            dictionary (Dict[str, Any]): Словарь с данными для инициализации объекта.

        Raises:
            ValueError: Если цена меньше 0 или отсутствует обязательный атрибут "title".
        """
        super().__init__(dictionary)
        self._price = self.__dict__.get("_price", 0)
        if self._price < 0:
            raise ValueError("must be >= 0")

        if "title" not in self.__dict__:
            raise ValueError("title - required attribute")

    @property
    def price(self) -> int:
        """
        Возвращает цену в объявлении.

        Returns:
            int: Цена.
        """
        return self._price

    @price.setter
    def price(self, new_value: int) -> None:
        """
        Устанавливает цену объявления. Проверяет, что она не меньше 0.

        Args:
            new_value (int): Новая цена объявления.

        Raises:
            ValueError: Если цена меньше 0.
        """
        if new_value < 0:
            raise ValueError("must be >= 0")
        self._price = new_value

    def __str__(self) -> str:
        """
        Возвращает строковое представление с окрашенным текстом.

        Returns:
            str: Строковое представление с применением цветового оформления.
        """
        text = super().__str__()
        return self.colorize_str(text)


if __name__ == "__main__":
    LESSON_STR = """{
        "title": "python",
        "price": 3,
        "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"],
        "class": 123
        }
    }"""

    DOG_STR = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""

    lesson = json.loads(LESSON_STR)
    dg = json.loads(DOG_STR)

    a = Advert(lesson)
    print(a.price)
    a.price = 100
    print(a.price)
    print(a)

    b = Advert(dg)
    print(b.price)
    print(b)
