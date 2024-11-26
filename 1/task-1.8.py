"""
Convert Decimal number to octal using print() output formatting.
For a given num = 8
Expected Output:
The octal number of decimal number 8 is 10
"""

user_input = int(input("octal num: "))

print(oct(user_input)[2:])
