"""string method"""

print("A → %s", "HEllo".lower())
print("B → %s", "hello words".capitalize())
print("C → %s", " hello　\t".strip())
print("D → %s", "hello".endswith("lo"))
print("E → %s", "one,three".split(","))
print("F → %s", "hello".find("e"))
print("G → %s", "hello words".count("o"))
print("H → %s", "hello".upper())
print("I → %s", "hello words".title())
print("J → %s", "hello words".istitle())
print("K → %s", "Hello".startswith("He"))
print("L → %s", "one, three".replace(",", " |"))
print("M → %s", "-".join(["A", "B", "C"]))
print("O → %s", "hello".index("e"))
print("P → %s", "12345".isnumeric())


a_list = []

b_list = ["A", "B", "D"]


print(a_list + b_list)


my_list = ["apple", "banana", "apple", "orange"]
unique = list(dict.fromkeys(my_list))
print(unique)
# a
