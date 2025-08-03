import unittest
from pizza import Pizza, MargheritaPizza, PepperoniPizza, ShrimpPizza, HawaiianPizza
from click.testing import CliRunner
from order import cli


class TestPizza(unittest.TestCase):

    def test_pizza_initialization(self):
        """Тестирование инициализации пиццы"""
        pizza = MargheritaPizza()
        self.assertEqual(pizza._name, "Маргарита🧀")
        self.assertEqual(
            pizza._ingredients, {"Томатный соус": 0, "Моцарелла": 0, "Томаты": 0}
        )
        self.assertEqual(pizza._size, None)
        self.assertEqual(pizza._stage, "Uncooked")

    def test_cook(self):
        """Тестирование метода cook"""
        pizza = PepperoniPizza()
        pizza.cook("L")
        self.assertEqual(pizza._size, "L")
        self.assertEqual(pizza._stage, "Cooked")
        self.assertEqual(
            pizza._ingredients, {"Томатный соус": 1, "Моцарелла": 1, "Пеперони": 1}
        )

    def test_invalid_size_in_cook(self):
        """Тестирование некорректного размера пиццы"""
        pizza = HawaiianPizza()
        pizza.cook("M")
        self.assertEqual(pizza._size, None)
        self.assertEqual(pizza._stage, "Uncooked")

    def test_dict(self):
        """Тестирование метода dict"""
        pizza = MargheritaPizza()
        self.assertEqual(pizza.dict(), ["Томатный соус", "Моцарелла", "Томаты"])

    def test_eq(self):
        """Тестирование оператора сравнения __eq__"""
        pizza1 = MargheritaPizza()
        pizza1.cook("XL")
        pizza2 = MargheritaPizza()
        pizza2.cook("XL")
        pizza3 = PepperoniPizza()
        pizza3.cook("L")
        self.assertTrue(pizza1 == pizza2)
        self.assertFalse(pizza1 == pizza3)

    def test_cli_order(self):
        """Тестирование команды CLI 'order'"""
        runner = CliRunner()
        result = runner.invoke(cli, ["order", "Маргарита", "L", "--delivery"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Доставляем пиццу", result.output)

        result = runner.invoke(cli, ["order", "Маргарита", "L"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Ждём самовывоз пиццы", result.output)

    def test_cli_menu(self):
        """Тестирование команды CLI 'menu'"""
        runner = CliRunner()
        result = runner.invoke(cli, ["menu"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Маргарита", result.output)
        self.assertIn("Пеперони", result.output)


if __name__ == "__main__":
    unittest.main()
