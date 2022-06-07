import abc


class CustomsVehicle:
    def __init__(self, age: int, model: str, dmg: float, milage: int):
        self.model = model
        self.age = age
        self.damage = dmg
        self.milage = milage


class Customs(abc.ABC):
    @abc.abstractmethod
    def vehicle_price(self, v: CustomsVehicle) -> float:
        pass

    @abc.abstractclassmethod
    def tax(self, v: CustomsVehicle) -> float:
        pass
