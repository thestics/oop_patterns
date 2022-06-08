#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko

import abc
from typing import Sequence, Union


class Visitor:
    
    @abc.abstractmethod
    def visit_sales(self, p: "SalesPerson"):
        pass
    
    @abc.abstractmethod
    def visit_manager(self, p: "Manager"):
        pass

    @abc.abstractmethod
    def visit_it_support(self, p: "ITSupport"):
        pass


class GiveRaiseVisitor(Visitor):
    
    # in real world arguments should be packed into one object, containing
    # all the data about changes in salaries
    def __init__(self, manager_delta, sales_delta, it_delta):
        self.manager_delta = manager_delta
        self.sales_delta = sales_delta
        self.it_delta = it_delta
    
    def visit_manager(self, p: "Manager"):
        p.salary += self.manager_delta
    
    def visit_sales(self, p: "SalesPerson"):
        p.salary += self.sales_delta

    def visit_it_support(self, p: "ITSupport"):
        p.salary += self.it_delta


class AcceptsVisitors:
    
    @abc.abstractmethod
    def accept(self, v: Visitor): ...


class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @abc.abstractmethod
    def get_salary(self): ...


class SalesPerson(AcceptsVisitors, Employee):

    def get_salary(self):
        return self.salary
    
    def accept(self, v: Visitor):
        v.visit_sales(self)


class Manager(AcceptsVisitors, Employee):
    
    # we'll pretend it's some sort of another implementation
    def get_salary(self):
        return self.salary
    
    def accept(self, v: Visitor):
        v.visit_manager(self)


class ITSupport(AcceptsVisitors, Employee):
    
    # we'll pretend it's some sort of another implementation
    def get_salary(self):
        return self.salary
    
    def accept(self, v: Visitor):
        v.visit_it_support(self)


class StaffList:
    
    def __init__(self, staff: Sequence[Union[AcceptsVisitors, Employee]]):
        self.staff = staff
        
    def give_raise(self, manager_delta, sales_delta, it_delta):
        visitor = GiveRaiseVisitor(manager_delta, sales_delta, it_delta)
        for employee in self.staff:
            employee.accept(visitor)
