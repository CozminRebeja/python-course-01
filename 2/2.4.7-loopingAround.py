"""
Write a Python program that prints all integers from 0 to 99 except multiples of 3 and multiples of 7. Use
a loop and a continue statement.
"""

def check_3 (input):
    if input % 3 == 0:
        return True
    else:
        return False
    
def check_7 (input):
    if input % 7 == 0:
        return True
    else:
        return False

for x in range(100):
    if check_3(x) or check_7(x):
         continue
    else:
        print(x)