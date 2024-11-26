"""
Write a Python program which accepts the radius and height of a
cylinder and calculates the volume.
"""

r_input = int(input("radius: "))
h_input = int(input("height: "))
pi = 3.14

volume = pi * (r_input**2) * h_input

print(f"volume: {volume}")


