#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko
import abc
import uuid
from typing import Type


class PaymentSystem:

    @staticmethod
    @abc.abstractmethod
    def pay(from_, to):
        pass


class PayPal(PaymentSystem):
    
    @staticmethod
    def pay(from_, to):
        print(f'Paying from {from_} to {to} using PayPal')


class GooglePay(PaymentSystem):
    
    @staticmethod
    def pay(from_, to):
        print(f'Paying from {from_} to {to} using Google Pay')


class Customer:
    
    def __init__(self, ps: Type[PaymentSystem]):
        self.payment_system = ps
        # we would have different source address depending on payment system
        # NOTE: In production world this would've been stored in a config
        #       file or fetched from a secrets manager
        self.account_nums = {
            PayPal:     uuid.uuid4(),
            GooglePay:  uuid.uuid4()
        }
        
    def pay(self, to):
        self.payment_system.pay(self.account_nums.get(self.payment_system), to)


if __name__ == '__main__':
    c = Customer(GooglePay)
    c.pay("First address")
    c.payment_system = PayPal
    c.pay("Second address")
