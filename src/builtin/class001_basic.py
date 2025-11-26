"""class001.py"""


class Smartphone:
    """Smartphone Class"""

    # 클래스 변수
    class_smartphone_count = 0
    price_per_raise = 0.5

    def __init__(self, brand: str, information: dict[str, str|int]) -> None:
        self._brand = brand
        self.information = information

        Smartphone.class_smartphone_count += 1

    def __str__(self) -> str:
        return f"str : {self._brand} - {self.information}"

    def __repr__(self) -> str:
        return f"repr : {self._brand} - {self.information}"

    def __del__(self) -> None:
        pass
        # Smartphone.smartphone_count -= 1

    def get_information(self) -> None:
        """_summary_"""
        print(f"Current Id : {id(self)}")
        price = self.information.get("price")
        print(f"Smartphone Detail Info : {self._brand} {price}")

    def get_price(self) -> str:
        """_summary_"""
        price = self.information.get("price")
        return f"Before Smartphone Price -> brand : {self._brand}, price : {price}"

    def get_price_calc(self) -> str:
        """_summary_"""
        price = self.information.get("price") or 0

        return f"After Smartphone Price -> brand : {self._brand}, price: {price * Smartphone.price_per_raise}"

    def detail_info(self) -> None:
        """_summary_"""
        print(f"Current Id : {id(self)}")
        price = self.information.get("price")
        print(f"Smartphone Detail Info : {self._brand} {price}")

    @classmethod
    def raise_price(cls, per:float):
        """_summary_"""
        if per <= 1:
            print("Please Enter 1 or More")
            return
        cls.price_per_raise = per
        return "Succeed! price increased."

    def instance_raise_price(self, per:float) -> "Smartphone":
        """_summary_"""
        if per <= 1:
            print("Please Enter 1 or More")
            return self
        Smartphone.price_per_raise = per
        return self

    @staticmethod
    def is_iphone(inst: "Smartphone"):
        """_summary_"""
        if inst._brand == "Iphone":
            return f"OK! This Smartphone is {inst._brand}."
        return "Sorry. This Smartphone is not Iphone."


Smartphone1 = Smartphone("Iphone", {"color": "White", "price": 10000})
Smartphone2 = Smartphone("Galaxy", {"color": "Black", "price": 5000})

# __dict__
print(f"orig__dict__→{Smartphone.__dict__}")
print(f"ins1__dict__→{Smartphone1.__dict__}")
print(f"ins2__dict__→{Smartphone2.__dict__}")
print("")

# __dir__
print(f"ins1__dir__→{dir(Smartphone1)}")
print("")

# __doc__
print(f"orig__doc__→{Smartphone.__doc__}")
print("")

# __str__
print(f"ins1.print→{Smartphone1}")
print(f"ins2.print→{Smartphone2}")
print("")

# __class__
print(f"orig.__class__→{Smartphone1.__class__}", Smartphone2.__class__)
print(f"instance id→{id(Smartphone1.__class__) == id(Smartphone2.__class__)}")
print("")

# smartphone_count
print(f"orig.class_smartphone_count→{Smartphone.class_smartphone_count}")
print(f"ins1.class_smartphone_count→{Smartphone1.class_smartphone_count}")
print(f"ins2.class_smartphone_count→{Smartphone2.class_smartphone_count}")
print("")

# price_calc
print(f"ins1.基本割引→{Smartphone1.get_price_calc()}")
print(f"ins2.基本割引→{Smartphone2.get_price_calc()}")
print("")

# 値上げ
print("値上げ2倍")
Smartphone.raise_price(2)
print("")

print(f"ins1.値上げ2倍→{Smartphone1.get_price_calc()}")
print(f"ins2.値上げ2倍→{Smartphone2.get_price_calc()}")
print("")

# price_calc
print(f"ins1.値上げ3倍→{Smartphone1.instance_raise_price(3).get_price_calc()}")
print(f"ins2.値上げ3倍→{Smartphone2.instance_raise_price(3).get_price_calc()}")
print("")

# static
print("ins1_static →", Smartphone.is_iphone(Smartphone1))
print("ins2_static →", Smartphone.is_iphone(Smartphone2))
