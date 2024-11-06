# Write a Python program that can eliminate all the duplicates from a given list.

list = [22, 44, 55, 123343243, 66, 66, 44, 55, 77, 88, 77, 77, 123343243, 88, 123343243]

"""
my solution:
list.sort()

i = 0
while (i != len(list)-1):
    if list[i] == list[i + 1] :
        list.pop(i)
        i -= 1
    i += 1
    
print(list)
"""
# alternative:

list = set(list)
print(list)