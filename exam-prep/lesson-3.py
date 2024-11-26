# collections_summary.py
"""
Summary of Python Collections: Lists, Dictionaries, Sets, and Tuples
"""

# Section 1: Lists
"""
1. A list is a mutable sequence that can hold elements of different types.
2. Elements can be accessed, modified, added, or removed.
"""

# Example: Basic List Operations
my_list = [1, 2, 3, 4]
my_list.append(5)  # Adds 5 at the end
print(f"List after append: {my_list}")
my_list[1] = 10  # Modifies the second element
print(f"List after modification: {my_list}")
my_list.pop(2)  # Removes the third element
print(f"List after pop: {my_list}")

# Example: Slicing
sliced_list = my_list[1:3]
print(f"Sliced list: {sliced_list}")

# Section 2: Iterating Through Lists
"""
1. Use loops or comprehensions to iterate through lists.
2. Use enumerate() to loop with indices.
"""

# Example: Iteration with enumerate
chars = ['A', 'B', 'C']
for index, value in enumerate(chars):
    print(f"Index: {index}, Value: {value}")

# Section 3: List Comprehensions
"""
1. List comprehensions are a concise way to generate lists.
2. Syntax: [expression for item in collection if condition]
"""

# Example: List Comprehension
squared = [x**2 for x in range(5)]
print(f"Squared numbers: {squared}")

# Section 4: Dictionaries
"""
1. Dictionaries store key-value pairs.
2. Keys must be unique and immutable.
"""

# Example: Dictionary Operations
my_dict = {'name': 'Alice', 'age': 25}
my_dict['city'] = 'Vienna'  # Add new key-value pair
print(f"Dictionary after adding city: {my_dict}")
del my_dict['age']  # Remove a key-value pair
print(f"Dictionary after deleting age: {my_dict}")

# Example: Dictionary Comprehension
squared_dict = {x: x**2 for x in range(5)}
print(f"Squared dictionary: {squared_dict}")

# Section 5: Sets
"""
1. Sets are unordered collections of unique elements.
2. Common operations include union, intersection, and difference.
"""

# Example: Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
intersection_set = set1 & set2
print(f"Union: {union_set}, Intersection: {intersection_set}")

# Section 6: Tuples
"""
1. Tuples are immutable sequences, often used for fixed data structures.
2. Syntax is similar to lists, but tuples are enclosed in parentheses.
"""

# Example: Basic Tuple Usage
my_tuple = (10, 20, 30)
print(f"Tuple: {my_tuple}, First element: {my_tuple[0]}")

# Section 7: Useful Built-in Functions
"""
1. Use `zip` to combine multiple lists into tuples.
2. Use `len`, `min`, and `max` for common operations on collections.
"""

# Example: Using zip to Combine Lists
list1 = ['name', 'age', 'city']
list2 = ['Alice', 25, 'Vienna']
combined = dict(zip(list1, list2))
print(f"Combined dictionary: {combined}")

# Section 8: Try at Home Tasks
"""
Task 1: Remove duplicates from a list using a set.
"""

# Example: Remove Duplicates
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(duplicate_list))
print(f"Unique elements: {unique_list}")

"""
Task 2: Check if a string is a valid Sudoku solution.
"""

# Example: Validate Sudoku Row
def is_valid_sudoku_row(row):
    return len(row) == len(set(row))

sudoku_row = [5, 3, 4, 6, 7, 8, 9, 1, 2]
print(f"Is valid row: {is_valid_sudoku_row(sudoku_row)}")

# Task 3: Decode a Secret Message
"""
Decode a message by reversing steps like word reversal and swapping characters.
"""

# Example: Decode Secret Message
def decode_message(encoded):
    words = encoded.split()
    decoded_words = [word[::-1] for word in words]
    return ' '.join(decoded_words)

secret_message = "siht si a tset"
print(f"Decoded message: {decode_message(secret_message)}")
