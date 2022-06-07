import abc


class Vehicle:
    def __init__(self, age: int, model: str, dmg: float, milage: int):
        self.model = model
        self.age = age
        self.damage = dmg
        self.milage = milage


class Car(Vehicle):
    def __init__(self, age: int, model: str, dmg: float):
        super().__init__(age, model, dmg, 0)


class Truck(Vehicle):
    def __init__(self, age: int, milage: int):
        super().__init__(age, "truck", 0, milage)


class VehicleCalc(abc.ABC):
    def __init__(self, v: Vehicle = None) -> None:
        self.vehicle = v

    def set_vehicle(self, v: Vehicle):
        self.vehicle = v

    @abc.abstractmethod
    def calculate_price(self) -> str:
        pass


class CarCalc(VehicleCalc):
    avg_car_price = 6_000
    car_price_map = {"ford": 3_000, "audi": 5_000, "bmw": 7_000, "tesla": 10_000}

    def calculate_price(self) -> str:
        retail_price = self.car_price_map.get(self.vehicle.model, self.avg_car_price)
        price = self.vehicle.damage * max(retail_price - 100 * self.vehicle.damage, 0)
        return f"{price} USD"


class TruckCalc(VehicleCalc):
    avg_truck_price = 10_000

    def calculate_price(self) -> str:
        price = max(
            self.avg_truck_price - 100 * self.vehicle.age - 0.01 * self.vehicle.milage,
            0,
        )
        return f"{price} USD"
