import abc
from typing import Sequence


class Lamp:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def light_on(self):
        if self.is_on:
            return
        print(f"{self.name} is on")
        self.is_on = True

    def light_off(self):
        if not self.is_on:
            return
        print(f"{self.name} is off")
        self.is_on = False


class Command:
    @abc.abstractmethod
    def execute(self):
        pass


class LightCommandOn(Command):
    def __init__(self, lamp: Lamp):
        self.lamp = lamp
        
    def execute(self):
        self.lamp.light_on()


class LightCommandOff(Command):
    def __init__(self, lamp: Lamp):
        self.lamp = lamp
    
    def execute(self):
        self.lamp.light_off()


class LightCommandOnUniversal(Command):
    def __init__(self, lamps: Sequence[Lamp]):
        self.lamps = lamps
    
    def execute(self):
        for l in self.lamps:
            l.light_on()

class LightCommandOffUniversal(Command):
    def __init__(self, lamps: Sequence[Lamp]):
        self.lamps = lamps
    
    def execute(self):
        for l in self.lamps:
            l.light_off()


class Controller:
    def __init__(
        self,
        command_on: Command,
        command_off: Command,
    ):
        self.command_on = command_on
        self.command_off = command_off

    def on(self):
        return self.command_on.execute()

    def off(self):
        return self.command_off.execute()


if __name__ == '__main__':
    foo_lamp = Lamp(name='foo')
    command_foo_on = LightCommandOn(foo_lamp)
    command_foo_off = LightCommandOff(foo_lamp)
    controller_foo = Controller(command_foo_on, command_foo_off)

    bar_lamp = Lamp(name='bar')
    command_bar_on = LightCommandOn(bar_lamp)
    command_bar_off = LightCommandOff(bar_lamp)
    controller_bar = Controller(command_foo_on, command_foo_off)

    command_universal_on = LightCommandOnUniversal([foo_lamp, bar_lamp])
    command_universal_off = LightCommandOffUniversal([foo_lamp, bar_lamp])
    universal_controller = Controller(command_universal_on, command_universal_off)
    
    controller_foo.on()
    controller_foo.off()
    
    controller_bar.on()
    controller_bar.off()
    
    universal_controller.on()
    universal_controller.off()
