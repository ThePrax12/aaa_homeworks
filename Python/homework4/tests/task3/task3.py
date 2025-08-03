from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoder(unittest.TestCase):

    def test_single_category(self):
        """Проверка кодировки одной категории"""
        result = fit_transform("apple")
        expected = [("apple", [1])]
        self.assertEqual(result, expected)

    def test_multiple_categories(self):
        """Проверка кодировки нескольких категорий"""
        result = fit_transform("apple", "banana", "cherry")
        expected = [
            ("apple", [0, 0, 1]),
            ("banana", [0, 1, 0]),
            ("cherry", [1, 0, 0]),
        ]
        self.assertEqual(result, expected)

    def test_duplicate_categories(self):
        """Проверка кодировки с повторяющимися элементами"""
        result = fit_transform("apple", "banana", "apple")
        expected = [
            ("apple", [0, 1]),
            ("banana", [1, 0]),
            ("apple", [0, 1]),
        ]
        self.assertEqual(result, expected)

    def test_no_arguments(self):
        """Проверка на вызов функции без аргументов"""
        with self.assertRaises(TypeError):
            fit_transform()

    def test_category_not_in_result(self):
        """Проверка, что категория, не переданная в функцию, отсутствует в результате"""
        result = fit_transform("apple", "banana")
        categories = [item[0] for item in result]
        self.assertNotIn("cherry", categories)


if __name__ == "__main__":
    unittest.main()
