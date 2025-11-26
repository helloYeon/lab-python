"""set method"""

set = {"A", "B", "C", "D"}


print("A add → %s" % (lambda set: [set.add("E"), set])(set)[1])

print("B pop → %s" % (lambda set: [set.pop(), set])(set)[1])

print("C copy → %s" % (lambda set: [n := set.copy(), n])(set)[1])

print("D clear → %s" % (lambda set: [n := set.copy(), n.clear(), n])(set)[2])

# 集合データ
set1 = {"A", "B", "C"}
set2 = {"C", "D", "E"}

# 集合.|
print("E set → %s" % (lambda set1, set2: [set1.union(set2)])(set1, set2)[0])

# 集合.|update
print(
    "F update → %s"
    % (lambda set1, set2: [n := set1.copy(), n.update(set2), n])(set1, set2)[2]
)

# 積集合.&
print(
    "G intersection → %s" % ((lambda set1, set2: set1.intersection(set2))(set1, set2))
)

# 積集合.&=
print(
    "H intersection_update → %s"
    % (lambda set1, set2: [n := set1.copy(), n.intersection_update(set2), n])(
        set1, set2
    )[2]
)

# 差集合.-
print(
    "I difference → %s"
    % (lambda set1, set2: [n := set1.difference(set2), n])(set1, set2)[1]
)

# 差集合.-=
print(
    "J difference_update → %s"
    % (lambda set1, set2: [n := set1.copy(), n.difference_update(set2), n])(set1, set2)[
        2
    ]
)

# 対称差集合.^
print(
    "K symmetric_difference → %s"
    % ((lambda set1, set2: set1.symmetric_difference(set2))(set1, set2))
)

# 差集合.^=
print(
    "L symmetric_difference_update → %s"
    % (lambda set1, set2: [n := set1.copy(), n.symmetric_difference_update(set2), n])(
        set1, set2
    )[2]
)

# 集合データ
set1 = {"A", "B", "C"}
set2 = {"C", "D", "E", "A", "B"}

# 超集合
print("M issuperset1 → %s" % set2.issuperset(set1))
print("M issuperset2 → %s" % set1.issuperset(set2))

# 部分集合
print("M issubset → %s" % set1.issubset(set2))

# 互いに素
print("M isdisjoint → %s" % set1.isdisjoint(set2))

# 削除
print("M discard → %s" % (lambda set1: [set1.discard("A"), set1])(set1)[1])
