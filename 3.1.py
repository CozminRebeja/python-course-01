# Playing with lists

"""
Make a list with [ ] brackets.
Append with the append() function
Create a list with some initial elements
Create a list with N repeated elements
Assign some lists to some variables. a = [1,2,3] b = 3*[‘xyz’]
• Try an empty list, repeated elements, initial set of elements
• Add two lists: a + b What happens?
• Try list indexing, deletion, functions from dir(my_list)
• Try assigning the result of a list slice to a new variable
"""

list = [2, 10, 45, 18, 23, 6, 9]
list.append([5, 22])

list2 = ['carrot', 'a', 25]
n = 10

list3 = [12]*n
print(list3)

a = [1, 2, 3]
b = 3 * ['xyz']
list4 = a + b
print(list4)


dir(a)

result = list3[slice(3, 9, 3)]
print(result)