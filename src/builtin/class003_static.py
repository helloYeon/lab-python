"""class002_inheritance"""

import abc



class Smartphone(metaclass=abc.ABCMeta):
    """Smartphone Class"""

    def __init__(self, brand:str, price:int) -> None:
        self._brand :str = brand
        self._price :int = price

    def __str__(self) -> str:
        return f"str : {self._brand} - {str(self._price)}"

    @abc.abstractmethod
    def func1(self) -> str:
        """_summary_"""
        pass

    @property
    def price(self) -> int:
        """Smartphone Class"""
        return self._price

    @price.setter
    def price(self, price:int) -> None:
        if price < 0:
            raise ValueError("Price below 0 is not possible")
        self._price = price


class Galaxy(Smartphone):
    """_summary_"""

    def __init__(self, price:int, country:str) -> None:
        super().__init__("Galaxy", price)
        self._country = country

    def __str__(self) -> str:
        return (
            f"str : {self._brand} - {self._price} - {self._country} - {self.__class__} "
        )

    def func1(self) -> str:
        """_summary_"""
        print("executed func1")
        return ""


class Iphone(Smartphone):
    """_summary_"""

    def __init__(self, price:int, country:str) -> None:
        super().__init__("IPhone", price)
        self._country = country

    def __str__(self) -> str:
        return (
            f"str : {self._brand} - {self._price} - {self._country} - {self.__class__} "
        )

    def func1(self) -> str:
        """_summary_"""
        print("executed func1")
        return ""

    @staticmethod
    def static1():
        """_summary_"""
        print("executed static1")


# iphone
iphone = Iphone(5000, "america")
print(iphone)

# galaxy
galaxy = Galaxy(7000, "korea")
print(galaxy)

# # static
# Iphone.static1()


# dic = {
#     "request_infos": {
#         "headers": {
#             "body": {
#                 "peppol_format_data_list": ["data1", "data2"],
#                 "other_data": "value"
#             }
#         }
#     }
# }

# # ネストされたキーが存在するか確認して削除
# if (
#     "request_infos" in dic and
#     "headers" in dic["request_infos"] and
#     "body" in dic["request_infos"]["headers"] and
#     "peppol_format_data_list" in dic["request_infos"]["headers"]["body"]
# ):
#     del dic["request_infos"]["headers"]["body"]["peppol_format_data_list"]

# # 結果を表示
# print(dic)
