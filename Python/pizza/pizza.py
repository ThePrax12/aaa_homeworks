import random
from typing import List


def log(message: str):
    """
    Декоратор, который выводит время определённого действия

    Args:
        message (str): Шаблон сообщения, кудм будет подставлено время.

    Returns:
        function: Декорированная функция.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            time = str(random.randint(1, 10))
            text = message.format(time)
            print(text)
            return result

        return wrapper

    return decorator


class Pizza:
    """
    Базовый класс для пиццы.

    Атрибуты:
        _name (str): Название пиццы.
        _size (str | None): Размер пиццы ('L' или 'XL').
        _ingredients (dict): Ингредиенты пиццы и их количество.
        _stage (str): Статус приготовления пиццы ('Uncooked' или 'Cooked').
    """

    def __init__(self, name: str, ingredients: List[str]):
        """
        Инициализация пиццы с именем, ингредиентами и начальным состоянием.

        Args:
            name (str): Название пиццы.
            ingredients (List[str]): Список ингредиентов пиццы.
        """
        self._name = name
        self._size = None
        self._ingredients = dict.fromkeys(ingredients, 0)
        self._stage = "Uncooked"

    @log("🍳Приготовили за {} c!")
    def cook(self, size: str) -> None:
        """
        Готовим пиццу, меняем её параметры и определяем размер.

        Args:
            size (str): Размер пиццы ('L' или 'XL').

        Returns:
            None
        """
        if size not in ("L", "XL"):
            print("Неверный размер пиццы")
            return

        if self._stage == "Cooked":
            print("Пицца уже приготовлена")
            return

        self._size = size
        self._stage = "Cooked"

        if size == "L":
            self._ingredients = dict.fromkeys(self._ingredients.keys(), 1)
        else:
            self._ingredients = dict.fromkeys(self._ingredients.keys(), 2)

    def dict(self) -> List[str]:
        """
        Получаем список ингредиентов пиццы.

        Returns:
            List[str]: Список ингредиентов пиццы.
        """
        return list(self._ingredients.keys())

    def __eq__(self, other: object) -> bool:
        """
        Сравниваем две пиццы по имени и размеру.

        Args:
            other (object): Объект, с которым сравниваем текущую пиццу.

        Returns:
            bool: Результат сравнения.
        """
        if not isinstance(other, Pizza):
            return False
        return (
            self._name == other._name
            and self._size is not None
            and other._size is not None
            and self._size == other._size
        )


class MargheritaPizza(Pizza):
    """
    Класс для пиццы 'Маргарита'.
    """

    def __init__(self) -> None:
        """
        Инициализация пиццы 'Маргарита' с ингредиентами.
        """
        super().__init__("Маргарита🧀", ["Томатный соус", "Моцарелла", "Томаты"])


class PepperoniPizza(Pizza):
    """
    Класс для пиццы 'Пеперони'.
    """

    def __init__(self) -> None:
        """
        Инициализация пиццы 'Пеперони' с ингредиентами.
        """
        super().__init__("Пеперони🍕", ["Томатный соус", "Моцарелла", "Пеперони"])


class HawaiianPizza(Pizza):
    """
    Класс для пиццы 'Гавайская'.
    """

    def __init__(self) -> None:
        """
        Инициализация пиццы 'Гавайская' с ингредиентами.
        """
        super().__init__("Гавайская🍍", ["Томатный соус", "Курица", "Ананас"])


class ShrimpPizza(Pizza):
    """
    Класс для пиццы с креветками.
    """

    def __init__(self) -> None:
        """
        Инициализация пиццы 'С креветками' с ингредиентами.
        """
        super().__init__(
            "С креветками🍤", ["Томатный соус", "Моцарелла", "Креветки", "Зелень"]
        )
