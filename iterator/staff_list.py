import dataclasses


@dataclasses.dataclass
class Employee:
    name: str


class EmployeeStorage:
    
    def __init__(self):
        # some kind of storage, structure of which is unknown outside this
        # class
        self.storage = []
    
    def add_employee(self, e):
        self.storage.append(e)
        return self
    
    def get(self, idx):
        return self.storage[idx]
    
    def __len__(self):
        return len(self.storage)
    
    def __iter__(self):
        return EmployeeStorageIterator(self)


# NOTE: It's common for python classes for one class to serve
#       both as a container and iterator. In that case `__iter__` would
#       simply return `self` and `__next__` can be implemented in the same
#       class
class EmployeeStorageIterator:
    
    def __init__(self, employee_storage):
        self.employee_storage = employee_storage
        self.cur_idx = -1
        
    def __next__(self):
        self.cur_idx += 1
        if self.cur_idx > len(self.employee_storage) - 1:
            raise StopIteration()
        return self.employee_storage.get(self.cur_idx)


if __name__ == '__main__':
    storage = EmployeeStorage()
    storage\
        .add_employee(Employee(name='Suzan')) \
        .add_employee(Employee(name='Louise'))

    for employee in storage:
        print(employee)