"""
Модуль для создания и работы с покемонами.
Включает функциональность для увеличения опыта и представления покемонов через эмодзи.
"""

from abc import ABC, abstractmethod


class EmojiMixin:
    """
    Миксин для представления типа покемона с использованием эмодзи.
    """

    poketype: str

    def __str__(self) -> str:
        """
        Возвращает эмодзи, соответствующее типу покемона.

        Returns:
            str: Эмодзи типа покемона, если тип известен, иначе текстовое представление типа.
        """
        if self.poketype == "grass":
            return "🌿"
        if self.poketype == "fire":
            return "🔥"
        if self.poketype == "water":
            return "🌊"
        if self.poketype == "electric":
            return "⚡"
        return self.poketype


class PokemonTrainInterface(ABC):
    """
    Абстрактный интерфейс для тренировки покемонов.
    """

    @abstractmethod
    def increase_experience(self, value: int) -> None:
        """
        Увеличивает количество опыта покемона.

        Args:
            value (int): Количество опыта для добавления.

        Returns:
            None
        """

    @property
    @abstractmethod
    def experience(self) -> int:
        """
        Возвращает текущий опыт покемона.

        Returns:
            int: Текущее значение опыта.
        """


class BasePokemon(PokemonTrainInterface):
    """
    Базовый класс для покемонов.
    """

    def __init__(self) -> None:
        """
        Инициализация базового покемона с начальным количеством опыта.
        """
        self._experience = 100

    def increase_experience(self, value: int) -> None:
        """
        Увеличивает опыт покемона.

        Args:
            value (int): Количество опыта для добавления.

        Returns:
            None
        """
        self._experience += value

    @property
    def experience(self) -> int:
        """
        Возвращает текущий опыт покемона.

        Returns:
            int: Текущее значение опыта.
        """
        return self._experience


class Pokemon(BasePokemon, EmojiMixin):
    """
    Класс для покемона, включающий тип покемона, имя и базовые функции.
    """

    def __init__(self, name: str, poketype: str) -> None:
        """
        Инициализация покемона с заданными именем и типом.

        Args:
            name (str): Имя покемона.
            poketype (str): Тип покемона.
        """
        self.name = name
        self.poketype = poketype
        super().__init__()

    def __str__(self) -> str:
        """
        Возвращает строковое представление покемона.

        Returns:
            str: Эмодзи, соответствующее типу покемона.
        """
        return EmojiMixin.__str__(self)


if __name__ == "__main__":
    bulbasaur = Pokemon(name="Bulbasaur", poketype="grass")
    print(bulbasaur)
    bulbasaur.increase_experience(100)
    assert bulbasaur.experience == 200
    print(bulbasaur.experience)
