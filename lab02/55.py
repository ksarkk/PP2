set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set4 = {"a", "b" , "c"}
set5 = {1, 2, 3}
set4.update(set5)
print(set4)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

z = x.intersection(y)
print(z)
