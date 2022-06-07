
from typing import Tuple
from customs import CustomsVehicle

from vehicle_calc import Car, CarCalc, Truck, TruckCalc, Vehicle, VehicleCalc


class VehicleCalcAdapter:

    def __init__(self, v: CustomsVehicle = None) -> None:
        self.vehicle = v
    
    def dispatch(self) -> Tuple[Vehicle, VehicleCalc]:
        """Based on provided customs vehicle, dispatch to the
        corresponding proprietary vehicle type and vehicle calc"""
        if self.vehicle.model == "truck":
            return Truck(self.vehicle.age, self.vehicle.milage), TruckCalc
        return Car(self.vehicle.age, self.vehicle.model, self.vehicle.dmg), CarCalc

    def price(self):
        assert self.vehicle is not None
        vehicle: Vehicle
        calc: VehicleCalc
        vehicle, calc = self.dispatch()

        # returned in form of string "N USD"
        p = calc(vehicle).calculate_price()
        return p.split()[0] + " ГРН"
