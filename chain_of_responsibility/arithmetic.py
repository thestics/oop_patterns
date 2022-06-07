#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko
import abc
import dataclasses
from typing import Union

from file_opener import BaseHandler, HandlingError


@dataclasses.dataclass
class UnaryOp:
    op: str
    operand: str
    op_type = 'unary'


@dataclasses.dataclass
class BinaryOp:
    op: str
    left: str
    right: str
    op_type = 'binary'


Op = Union[UnaryOp, BinaryOp]


class ArithmeticHandler(BaseHandler):
    target_op = '__DEFAULT'
    target_op_type = '__DEFAULT'
    
    @abc.abstractmethod
    def handle_concrete(self, obj: Op):
        pass
    
    def handle(self, obj: Op):
        if obj.op == self.target_op and obj.op_type == self.target_op_type:
            return self.handle_concrete(obj)
        if self.next is not None:
            return self.next.handle(obj)
        else:
            raise HandlingError(f"Unable to handle op: {obj}")


class PlusBinHandler(ArithmeticHandler):
    target_op = "+"
    target_op_type = "binary"

    def handle_concrete(self, obj: Op):
        assert isinstance(obj, BinaryOp)
        return int(obj.left) + int(obj.right)


class MulBinHandler(ArithmeticHandler):
    target_op = "*"
    target_op_type = "binary"
    
    def handle_concrete(self, obj: Op):
        assert isinstance(obj, BinaryOp)
        return int(obj.left) * int(obj.right)


class MinusBinHandler(ArithmeticHandler):
    target_op = "-"
    target_op_type = "binary"

    def handle_concrete(self, obj: Op):
        assert isinstance(obj, BinaryOp)
        return int(obj.left) - int(obj.right)


class MinusUnHandler(ArithmeticHandler):
    target_op = "-"
    target_op_type = "unary"

    def handle_concrete(self, obj: Op):
        assert isinstance(obj, UnaryOp)
        return -int(obj.operand)


if __name__ == '__main__':
    ops = [
        BinaryOp('+', '1', '2'),
        BinaryOp('-', '3', '4'),
        UnaryOp('-', '7'),
        BinaryOp('&', '1', '1')
    ]
    
    h = PlusBinHandler()
    h = MinusBinHandler(next_=h)
    h = MulBinHandler(next_=h)
    h = MinusUnHandler(next_=h)
    
    for op in ops:
        try:
            print(f"{op=} {h.handle(op)=}")
        except HandlingError:
            print(f"Unable to handle {op}")
