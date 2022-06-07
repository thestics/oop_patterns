import abc
from typing import Sequence


class DrinkType(abc.ABC):
    @abc.abstractmethod
    def get_price_delta(self) -> int:
        pass


class DefaultDrink(DrinkType):
    def get_price_delta(self) -> int:
        return 0


class BlackDrink(DrinkType):
    def get_price_delta(self) -> int:
        return 10


class DrinkAddition(abc.ABC):
    @abc.abstractmethod
    def get_price_delta(self) -> int:
        pass


class MilkAddition(DrinkAddition):
    def get_price_delta(self) -> int:
        return 5


class Consumption(abc.ABC):
    @abc.abstractmethod
    def consume(self) -> None:
        pass


class ConsumeInHouse(Consumption):
    def consume(self) -> None:
        print("Drink consumed in house")


class ConsumeOutdoors(Consumption):
    def consume(self) -> None:
        print("Drink consumed outdoors")


class Beverage:
    base_price = 10

    def __init__(
        self,
        sugar,
        drink_type: DrinkType,
        drink_additions: Sequence[DrinkAddition],
        consumption_type: Consumption,
    ):
        self.sugar = sugar
        self.drink_type = drink_type
        self.drink_additions = drink_additions
        self.consumption_type = consumption_type

    def prepare(self):
        type_name = self.drink_type.__class__.__name__
        additions = (
            ", ".join(add.__class__.__name__ for add in self.drink_additions)
            or "none"
        )
        consumption_type = self.consumption_type.__class__.__name__
        print(
            f"Preparing beverage of type {type_name} with additions: {additions} to {consumption_type}"
        )

    def drink(self):
        print("Drinking...")

    def cost(self):
        return (
            self.base_price
            + 0.1 * self.sugar
            + self.drink_type.get_price_delta()
            + sum(add.get_price_delta() for add in self.drink_additions)
        )


class Coffe(Beverage):
    base_price = 15


class Tea(Beverage):
    base_price = 12


black_coffe_with_milk_to_go = Coffe(
    sugar=1,
    drink_type=BlackDrink(),
    drink_additions=[MilkAddition()],
    consumption_type=ConsumeOutdoors(),
)

black_coffe_with_milk_to_go.prepare()
print("Price: ", black_coffe_with_milk_to_go.cost(), " UAH")
