# Example: Basic Input-Output
user_name = input("Enter your name: ")  # Input
print(f"Hello, {user_name}!")  # Output

# Section 3: Comments
"""
1. Use '#' for single-line comments.
2. Simulate multi-line comments with triple quotes (docstrings).
"""

# Section 4: Variables, Expressions, and Data Types
"""
1. Variables are containers for storing data. E.g., int, float, str.
2. Variables must be initialized before use.
"""

# Example: Variable Initialization and Type Checking
x = 42
y = 3.14
z = "Hello, World!"
print(f"x: {x} (type: {type(x)})")
print(f"y: {y} (type: {type(y)})")
print(f"z: {z} (type: {type(z)})")

# Section 5: Arithmetic and Assignment Operators
"""
Operators: +, -, *, /, %, **, //
Example: x += y is equivalent to x = x + y.
"""

# Example: Arithmetic Operations
a = 10
b = 3
print(f"Addition: {a + b}")
print(f"Exponentiation: {a ** b}")

# Section 6: Naming Conventions
"""
1. Start variable names with a letter or underscore.
2. Use meaningful names; avoid cryptic symbols.
"""

# Section 7: Input and Type Conversion
"""
Use input() to read user input. Convert data types using int(), float(), etc.
"""

# Example: Reading and Converting Input
temperature_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
print(f"Temperature in Celsius: {temperature_celsius:.2f}")

# Section 8: Formatted Strings
"""
1. Use f-strings for dynamic string formatting.
2. Example: f"My age is {age}".
"""

# Example: Using f-Strings
name = "Alice"
age = 25
print(f"Hello, {name}. You are {age} years old.")

# Section 9: Tasks to Try at Home
"""
1. Convert Fahrenheit to Celsius.
2. Calculate the area of a circle.
3. Convert miles to kilometers.
"""

# Example Task: Area of a Circle
radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * radius**2
print(f"Area of the circle: {area:.2f}")

# Example Task: Sum of Two Numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"Sum: {num1 + num2}")

# Example Task: Base and Exponent
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(f"{base} raised to the power of {exponent} is {base ** exponent}")