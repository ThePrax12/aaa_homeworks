from pizza import MargheritaPizza, PepperoniPizza, HawaiianPizza, ShrimpPizza, log
import click


@log("🚚Доставили за {} c!")
def delivery_func(ordered_pizza: "Pizza") -> None:
    """
    Функция для доставки пиццы.

    Args:
        ordered_pizza (Pizza): Пицца, которая доставляется.

    Returns:
        None
    """
    print(f"Доставляем пиццу {ordered_pizza._name} размера {ordered_pizza._size}")


@log("🏃‍️Забрали за {} c!")
def pickup(ordered_pizza: "Pizza") -> None:
    """
    Функция для самовывоза пиццы.

    Args:
        ordered_pizza (Pizza): Пицца, которая забирается.

    Returns:
        None
    """
    print(f"Ждём самовывоз пиццы {ordered_pizza._name} размера {ordered_pizza._size}")


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option(
    "--delivery", default=False, is_flag=True, help="Флаг для доставки пиццы."
)
@click.argument("pizza", nargs=1)
@click.argument("size", nargs=1)
def order(pizza: str, size: str, delivery: bool) -> None:
    """
    Оформление заказа пиццы с возможностью выбрать способ доставки или самовывоза.

    Args:
        pizza (str): Название пиццы для заказа.
        size (str): Размер пиццы (L или XL).
        delivery (bool): Флаг, если доставка, иначе самовывоз.

    Returns:
        None
    """
    if pizza == "Маргарита":
        ordered_pizza = MargheritaPizza()
        ordered_pizza.cook(size)
    elif pizza == "Пеперони":
        ordered_pizza = PepperoniPizza()
        ordered_pizza.cook(size)
    elif pizza == "Гавайская":
        ordered_pizza = HawaiianPizza()
        ordered_pizza.cook(size)
    elif pizza == "Креветочная":
        ordered_pizza = ShrimpPizza()
        ordered_pizza.cook(size)
    else:
        print("Такой пиццы нет!")
        return

    if delivery:
        delivery_func(ordered_pizza)
    else:
        pickup(ordered_pizza)


@cli.command()
def menu() -> None:
    """
    Выводит меню доступных пицц с ингредиентами.

    Returns:
        None
    """
    print(MargheritaPizza()._name, " : ", ", ".join(MargheritaPizza().dict()))
    print(PepperoniPizza()._name, " : ", ", ".join(PepperoniPizza().dict()))
    print(HawaiianPizza()._name, " : ", ", ".join(HawaiianPizza().dict()))
    print(ShrimpPizza()._name, " : ", ", ".join(ShrimpPizza().dict()))


if __name__ == "__main__":
    cli()
