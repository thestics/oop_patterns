import abc
from typing import List


class Payable(abc.ABC):
    def __init__(self, name=None) -> None:
        self.name = name

    @abc.abstractmethod
    def pay_expences(self, amt):
        pass


class Worker(Payable):
    def pay_expences(self, amt):
        print(f"{self.name} was paid ${amt}")


class Manager(Worker):
    pass


class Employee(Worker):
    def __init__(self, name, manager: Manager) -> None:
        super().__init__(name)
        self.manager = manager


class SalesTeam(Payable):
    def __init__(
        self,
        name=None,
        managers: List[Manager] = (),
        workers: List[Employee] = (),
    ) -> None:
        super().__init__(name)
        self.managers = managers
        self.workers = workers

    def pay_expences(self, amt):
        [m.pay_expences(amt) for m in self.managers]
        [m.pay_expences(amt) for m in self.workers]

    def add_manager(self, m: Manager):
        self.managers.append(m)

    def remove_manager(self, m: Manager):
        self.managers.remove(m)

    def add_woker(self, m: Employee):
        self.workers.append(m)

    def remove_worker(self, m: Employee):
        self.workers.remove(m)


if __name__ == "__main__":
    jane = Manager(name="jane")
    bob = Employee(name="bob", manager=jane)
    sue = Employee(name="sue", manager=jane)

    team = SalesTeam(name="team A", managers=[jane], workers=[bob, sue])

    jane.pay_expences(100)
    bob.pay_expences(300)
    team.pay_expences(200)
