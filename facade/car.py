class Accelerator:
    def press(self):
        print("Pressing accelerator down")

    def lift(self):
        print("Lifting accelerator up")


class Clutch:
    def press(self):
        print("Clutch pressed")

    def lift(self):
        print("Clutch lifted")


class Gear:
    def change_gear(self, gear):
        print(f"Changing gear to {gear}")


class HandBrake:
    def push_down(self):
        print("Handbrake pressed")

    def lift_up(self):
        print("Handbrake released")


class Ignition:
    def turn_on(self):
        print("Ignition on")

    def turn_off(self):
        print("Turn off")


class CarFacade:
    def drive(self):
        ignition = Ignition()
        clutch = Clutch()
        accelerator = Accelerator()
        gear_stick = Gear()
        hand_brake = HandBrake()

        ignition.turn_on()
        clutch.press()
        gear_stick.change_gear(1)
        accelerator.press()
        clutch.lift()
        hand_brake.push_down()
        accelerator.press()
        clutch.press()


class Car:
    def drive(self):
        CarFacade().drive()
