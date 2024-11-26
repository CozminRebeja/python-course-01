"""
Write a Python program that reads three Integers from the user 
and calculates the maximum of the three numbers.

Print the result to the console.
"""


num_list = [int(input("num1: ")), int(input("num2: ")), int(input("num3: "))]

max = num_list[0]

for num in num_list:
    if num > max:
        max = num

print(max)