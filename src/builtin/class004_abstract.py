"""class002_inheritance with clarification"""

import abc
from typing import Any, Self


class Smartphone(metaclass=abc.ABCMeta):
    """Smartphone Class"""

    __tel: str
    __address: str = "vv"

    @classmethod
    def set_tel(cls, tel: str) -> type[Self]:
        """set_tel"""
        cls.__tel = tel

        return cls

    @classmethod
    def set_address(cls, address: str) -> type[Self]:
        """set_address"""
        cls.__address = address

        return cls

    @classmethod
    def hello(cls, name):
        """_summary_"""
        print(f"hello001:{Smartphone.__address}")
        print(f"hello002:{name} tel:{cls.__tel} address:{cls.__address}")


class Galaxy(Smartphone):
    """_summary_"""

    @classmethod
    def setting(cls, tel: str, address: str) -> type[Self]:
        """Setting"""
        cls.set_tel(tel)
        cls.set_address(address)

        return cls


# Galaxy.setting("080-1234-5678", "japan")
Galaxy.setting("111-1111-11111", "usa").set_tel("080-1234-5678").set_address("japan")
Galaxy.hello("test")  # Output: before, hello:test, after
