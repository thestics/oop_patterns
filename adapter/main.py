from customs import CustomsVehicle, Customs
from calc_adapter import VehicleCalcAdapter


class AdaptedCustoms(Customs, VehicleCalcAdapter):
    def vehicle_price(self, v: CustomsVehicle) -> float:
        self.vehicle = v
        return super().price()

    def tax(self, v: Customs) -> float:
        self.vehicle = v
        price = self.price()
        return 0.2 * price


if __name__ == "__main__":
    v = CustomsVehicle(1, "truck", 0, 10_000)
    print(AdaptedCustoms().vehicle_price(v))
