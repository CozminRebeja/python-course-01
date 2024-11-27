# basic_programming_constructs.py
"""
Basic Programming Constructs: Summary of Key Concepts and Python Examples
"""

# Section 1: Conditional Execution
"""
1. Use `if`, `else`, and `elif` statements to make decisions in your program.
2. Boolean expressions test conditions and determine the flow of execution.
3. Indentation defines code blocks in Python.
"""

# Example: Discount Calculator
items_bought = int(input("Enter the number of items bought: "))
if items_bought > 20:
    discount = 10
elif 10 < items_bought <= 20:
    discount = 5
elif 5 <= items_bought <= 10:
    discount = 2
else:
    discount = 0
print(f"You get a {discount}% discount!")

# Section 2: Boolean Logic
"""
1. Use `and`, `or`, and `not` to combine or invert conditions.
2. Short-circuit evaluation stops evaluating as soon as the result is determined.
"""

# Example: Short Circuit Evaluation
a, b, c = 1, 2, 3
print(f'a > b or b < c: {a > b or b < c}')
print(f'a == b and c > b: {a == b and c > b}')

# Section 3: Strings
"""
1. Strings are immutable sequences of characters.
2. Use methods like `.upper()`, `.lower()`, `.replace()` for string operations.
3. Use slicing to extract parts of a string: `my_string[start:end:step]`.
"""

# String Methods:
"""
• upper()
• lower()
• capitalize() - Converts the first character of the string to uppercase and the rest to lowercase.
• count(s) - Returns the number of occurrences of a substring s in the string.
• find(s) - Returns the lowest index of the substring s in the string. Returns -1 if not found.
• rfind(s) - Returns the highest index of the substring s in the string. Returns -1 if not found.
• index(s) - Similar to find(), but raises a ValueError if the substring s is not found.
• strip() - Removes leading and trailing whitespace (or specified characters).
• lstrip() - Removes leading whitespace (or specified characters).
• rstrip() - Removes trailing whitespace (or specified characters)
• replace(a, b) - Replaces all occurrences of substring a with substring b.
• expandtabs() - Replaces tabs (\t) with spaces. The number of spaces per tab is configurable (default is 8).
• split() - Splits the string into a list of substrings using whitespace as the delimiter by default.
• join() - Joins a sequence of strings with the string as the delimiter.
• center() - Centers the string in a field of a given width.
• ljust() - Left-justifies the string in a field of a given width.
• rjust() - Right-justifies the string in a field of a given width.
• removeprefix (p) - Removes the specified prefix p from the string if it starts with p.
• removesuffix (s) - Removes the specified suffix s from the string if it ends with s.
"""

# Example: String Manipulation
my_string = "informatics"
print(f"First 2 and last 2 chars: {my_string[:2] + my_string[-2:]}")  # incs

# Section 4: Loops
"""
1. Use `while` loops for indefinite repetition based on a condition.
2. Use `for` loops to iterate over a sequence.
3. `break` exits a loop immediately; `continue` skips the rest of the current iteration.
"""

# Example: Sum of Squares in a Range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
sum_of_squares = sum(i**2 for i in range(start, end + 1))
print(f"Sum of squares: {sum_of_squares}")

# Section 5: Functions for Strings and Numbers
"""
1. Use `ord()` to get ASCII/Unicode value of a character.
2. Use `chr()` to get a character from an ASCII/Unicode value.
"""

# Example: ASCII Manipulation
char = 'a'
print(f"ASCII value of '{char}': {ord(char)}")
num = 99
print(f"Character for ASCII value {num}: {chr(num)}")

# Section 6: Try at Home Tasks
"""
Task 1: Leap Year Identifier
Determine if a year is a leap year.
"""

# Example: Leap Year Checker
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

"""
Task 2: Balanced Word
Check if the left and right halves of a word have the same ASCII sum.
"""

# Example: Balanced Word Checker
word = input("Enter a word: ").lower()
mid = len(word) // 2
left, right = word[:mid], word[mid + 1:] if len(word) % 2 else word[mid:]
is_balanced = sum(ord(c) for c in left) == sum(ord(c) for c in right)
print(f"{word} is {'balanced' if is_balanced else 'not balanced'}.")

"""
Task 3: Kaprekar Number Checker
Check if a number is a Kaprekar number.
"""

# Example: Kaprekar Number Checker
num = int(input("Enter a number: "))
square = str(num**2)
split = len(square) // 2
left, right = square[:split] or "0", square[split:]
if int(left) + int(right) == num:
    print(f"{num} is a Kaprekar number.")
else:
    print(f"{num} is not a Kaprekar number.")