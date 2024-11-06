# Given two Python sets, write a Python program to update the first set with items that exist only in the
# first set and not in the second set.

set1 = {1, 2, 3, 5, 6, 9}
set2 = {2, 4, 5, 6, 1, 0}

dif = set1 - set2
print(dif)

x = set1 - dif

for i in x:
    set1.remove(i)

print(set1)