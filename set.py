"""
Set ---> 1) Unordered  2) Mutable
"""
set1 = {12,54,98,16,78,12,65}

print(type(set1))
print(set1)
print(len(set1))
print(max(set1))
print(min(set1))
print(sorted(set1))

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}

print(set1.add(11))
print(set1)

set1.clear()
print(set1)

set3 = set1.copy()
print(set3)

set1.discard(3)
print(set1)

print(set1.difference(set2))
print(set1)

set1.difference_update(set2)
print(set1)

print(set1.symmetric_difference(set2))
set1.symmetric_difference_update(set2)
print(set1)


print(set1.intersection(set2))

# set1.intersection_update(set2)
# print(set1)

print(set1.isdisjoint(set2))

set3 = {1,2,3,4,5}
set4 = {4,5}

print(set3.isdisjoint(set4))
print(set3.issubset(set4))          # Set3 is a superset of set4
print(set3.issuperset(set4)) 
print(set4.issubset(set3))       


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1.pop())
print(set1)

set1.remove(3)
print(set1)

print(set1.symmetric_difference(set2))

set1.symmetric_difference_update(set2)
print(set1)

print(set1.union(set2))

set1.update(set2)
print(set1)
