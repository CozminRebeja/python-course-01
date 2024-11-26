"""
Write a Python program which accepts the radius of a circle from the
user and computes the area.
"""

user_input = int(input("radius: "))
pi = 3.14

area = (user_input ** 2) * pi

print(f"area: {area}")