# Write a Python program to convert a Miles to Kilometers.
# The formula is 1M = 1.6Km.

def miles_km(x):
    return float(x * 1.61)

print(round(miles_km(30), 1))