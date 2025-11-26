"""list method"""

list = [10, 20, 30, 40, 50, "apple"]

print("\nA → append %s" % (lambda list: [list.append("banana"), list])(list)[1])

print(
    "\nB → extend %s" % (lambda list: [list.extend(["cherry", [1, 2]]), list])(list)[1]
)

print("\nC → insert %s" % (lambda list: [list.insert(3, 35), list])(list)[1])

print("\nD → count %s" % (lambda list: list.count("apple"))(list))

print("\nE → clear %s" % (lambda list: [new := list.copy(), new.clear(), new])(list)[2])

print("\nF → index %s" % (lambda list: list.index(20))(list))

print("\nG → remove %s" % (lambda list: [list.remove(35), list])(list)[1])

print("\nH → reverse %s" % (lambda list: [list.reverse(), list])(list)[1])

print("\nI → pop %s" % (lambda list: [list.pop(4), list])(list)[1])

print(
    "\nI → sort %s"
    % (
        lambda list: [
            sorted := [str(item) for item in list],
            sorted.sort(),
            sorted,
        ]
    )(
        list
    )[2]
)


ttt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(ttt[:3])
print(ttt[2:])

# round(3 / 2)
# lam = lambda ttt: [cnt := round(len(ttt) / 2), ttt[cnt::]]
# print(111, lam(ttt))
