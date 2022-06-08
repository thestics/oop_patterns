#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko

import abc
from typing import Optional, Any


class BaseHandler:
    def __init__(self, next_: Optional["BaseHandler"] = None):
        self.next = next_

    @abc.abstractmethod
    def handle(self, obj: Any):
        pass


class HandlingError(Exception):
    pass


class FileHandler(BaseHandler):
    expected_ext = "__DEFAULT"

    def handle(self, obj: str) -> int:
        split = obj.split(".")
        ext = split[-1] if split else None

        if ext == self.expected_ext:
            print(f"Handled file {obj} by {self.__class__.__name__}")
            return 0
        else:
            if self.next is not None:
                return self.next.handle(obj)
            else:
                raise HandlingError("Unable to find handler")


class ExeFileHandler(FileHandler):
    expected_ext = "exe"


class JpegFileHandler(FileHandler):
    expected_ext = "jpeg"


class BmpFileHandler(FileHandler):
    expected_ext = "bmp"


def build_file_handler_chain() -> FileHandler:
    exe = ExeFileHandler()
    jpeg = JpegFileHandler(next_=exe)
    bmp = BmpFileHandler(next_=jpeg)

    return bmp


if __name__ == "__main__":
    file_names = ["foo.exe", "bar.exe", "foo.bmp", "foo.bar"]

    h = build_file_handler_chain()
    for name in file_names:
        try:
            h.handle(name)
        except HandlingError:
            print(f"Couldn't handle {name}")
