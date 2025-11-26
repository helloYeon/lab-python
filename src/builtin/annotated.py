"""lambda.py"""

from typing import Annotated, Any


class Hoge:
    def __init__(self) -> None:
        self.aa = 11
        self.bb = 22


aa = Annotated[str, Hoge()]

print(f"{aa=} ")


# print("\nA → lambda1 %s" % (lambda x: x**2)(5))

# print("\nB → lambda2 %s" % (lambda x, y: x + y)(3, 4))

# print("\nC → map  %s" % (list(map(lambda x: x**2, [1, 2, 3, 4, 5]))))

# print(
#     "\nD → filter  %s"
#     % (list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
# )

# print("\nE → reduce  %s" % (reduce(lambda carry, item: carry * item, [1, 2, 3, 4])))
