# """
# Write a Python program to convert a Fahrenheit temperature to Centigrade.
# The formula is C = (F -32) x 5/9
# We use type float for the temperatures.
# """


def convert(x):
    return (x - 32.0) * (5.0/9.0)

print(round(convert(15), 2))

