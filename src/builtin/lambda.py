"""lambda.py"""

from functools import reduce

print("\nA → lambda1 %s" % (lambda x: x**2)(5))

print("\nB → lambda2 %s" % (lambda x, y: x + y)(3, 4))

print("\nC → map  %s" % (list(map(lambda x: x**2, [1, 2, 3, 4, 5]))))

print(
    "\nD → filter  %s"
    % (list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
)

print("\nE → reduce  %s" % (reduce(lambda carry, item: carry * item, [1, 2, 3, 4])))


base = {
    "userId": 2,
    "loginId": "t.test2@example.com",
    "lastName": "アドグローブ",
    "firstName": "1",
    "esCompanyId": 2,
    "createDate": "2024-02-01T18:01:40+09:00",
    "updateDate": "2024-02-01T18:01:51+09:00",
}


# 100個の辞書をリストに追加
dictionaries = []

for i in range(10):
    new_dict = base.copy()
    new_dict["userId"] = i
    new_dict["firstName"] = str(i)
    dictionaries.append(new_dict)

print(dictionaries)
