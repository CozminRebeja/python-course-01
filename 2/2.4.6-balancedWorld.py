"""
We can assign a value to each character in a word, based on their position in the alphabet (a = 1,
b = 2, ... , z = 26). A balanced word is one where the sum of values on the left-hand side of the
word equals the sum of values on the right-hand side. For odd length words, the middle character
(balance point) is ignored. Write a program that prints whether any given word is balanced or not.
"""

input = input("Insert a word:")

length = len(input)
i = 0
sumLeft = 0
sumRight = 0

while i < (length // 2):
    sumLeft += (ord(input[i])-96)
    i += 1

while i != length:
    sumRight += (ord(input[i])-96)
    i += 1

if sumLeft == sumRight:
    print(f'{input} is balanced')
else:
    print(f'{input} is not balanced')



