"""
Write a Python program which asks the user for 
a base and an exponent number.

Then display the output as follows:
base = 5
exponent = 4
5 raises to the power of 4 is: 625
"""

base_input = int(input("base: "))
exponent_input = int(input("exponent: "))

result = base_input ** exponent_input

print(f"{base_input} raised to the power of {exponent_input} is: {result}")
