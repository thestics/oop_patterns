class Plane:
    def __init__(self, id_, airport):
        self.in_the_air = False
        self.id = id_
        self.airport = airport

    def take_off(self):
        self.airport.depart(self)

    def land(self):
        self.airport.land(self)


class Runway:
    def __init__(self):
        self.available = True

    def set_available(self, status: bool):
        self.available = status

    def is_available(self):
        return self.available


class PlanesOnTheGround:
    def __init__(self):
        self.planes = []

    def add_plane(self, plane):
        self.planes.append(plane)

    def remove_plane(self, plane):
        self.planes.remove(plane)


class PlanesInTheAir:
    def __init__(self):
        self.planes = []

    def add_plane(self, plane):
        self.planes.append(plane)

    def remove_plane(self, plane):
        self.planes.remove(plane)


class Mediator:
    def land(self, plane):
        ...

    def depart(self, plane):
        ...


class Airport(Mediator):
    def __init__(
        self,
        runway: Runway,
        grounded: PlanesOnTheGround,
        airborne: PlanesInTheAir,
    ):
        self.runway = runway
        self.grounded = grounded
        self.airborne = airborne
    
    def add_grounded_plane(self, plane):
        self.grounded.add_plane(plane)
    
    def land(self, plane):
        if plane.in_the_air and self.runway.is_available():
            print(f"Plane {plane.id} is landing...")
            self.grounded.add_plane(plane)
            self.airborne.remove_plane(plane)
            plane.in_the_air = False
            self.runway.set_available(False)

    def depart(self, plane: Plane):
        if not plane.in_the_air and self.runway.is_available():
            print(f"Plane {plane.id} is departing...")
            self.grounded.remove_plane(plane)
            self.airborne.add_plane(plane)
            plane.in_the_air = True
            self.runway.set_available(False)


if __name__ == '__main__':
    airport = Airport(
        Runway(), PlanesOnTheGround(), PlanesInTheAir()
    )
    plane = Plane(id_=1, airport=airport)
    airport.add_grounded_plane(plane)
    plane.take_off()

    