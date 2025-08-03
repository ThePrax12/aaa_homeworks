import pytest
from one_hot_encoder import fit_transform


def test_multiple_categories():
    """Проверка кодировки нескольких категорий"""
    result = fit_transform("apple", "banana", "cherry")
    expected = [
        ("apple", [0, 0, 1]),
        ("banana", [0, 1, 0]),
        ("cherry", [1, 0, 0]),
    ]
    assert result == expected


def test_multiple_categories_2():
    """Проверка кодировки нескольких категорий с дублями"""
    result = fit_transform("apple", "banana", "cherry", "cherry")
    expected = [
        ("apple", [0, 0, 1]),
        ("banana", [0, 1, 0]),
        ("cherry", [1, 0, 0]),
        ("cherry", [1, 0, 0]),
    ]
    assert result == expected


def test_duplicate_categories():
    """Проверка кодировки с повторяющимися элементами"""
    result = fit_transform("apple", "banana", "apple")
    expected = [
        ("apple", [0, 1]),
        ("banana", [1, 0]),
        ("apple", [0, 1]),
    ]
    assert result == expected


def test_no_arguments():
    """Проверка на вызов функции без аргументов"""
    with pytest.raises(TypeError):
        fit_transform()


def test_single_category():
    """Проверка кодировки одной категории"""
    categories = ["apple"]
    result = fit_transform(*categories)
    expected = [("apple", [1])]
    assert result == expected
