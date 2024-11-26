"""
Write a Python program to change a given string to a new string 
where the first and last chars have been exchanged.
"""

user_input = input("string: ")

first = user_input[0]
last = user_input[-1]

final = list(user_input)
final[0] = user_input[-1]
final[-1] = user_input[0]
show = ""

for i in final:
    show += i

print(show)