# Write a Python program to convert a Celsius Temperature to Fahrenheit.
# The formula is: F = C (9/5)+32

def celsius_fahrenheit(input):
    return round((input * (9.0 / 5.0) + 32), 2)

print(celsius_fahrenheit(32))

