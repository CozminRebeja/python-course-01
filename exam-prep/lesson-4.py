# modularization_and_functions.py
"""
Summary of Modularization and Functions in Python
"""

# Section 1: Functions
"""
1. Functions are reusable blocks of code that perform specific tasks.
2. Benefits: Simpler code, reusability, easier debugging, faster development.
"""

# Example: Basic Function
def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

print(greet("Alice"))

# Section 2: Function Arguments and Return Values
"""
1. Functions can accept arguments and return values.
2. Default arguments allow specifying default values for parameters.
3. Keyword arguments allow flexibility in specifying arguments by name.
"""

# Example: Default and Keyword Arguments
def calculate(a, b=10):
    """Calculates the sum and difference of two numbers."""
    return a + b, a - b

result = calculate(20)
print(f"Sum and Difference: {result}")

# Section 3: Variable Scope
"""
1. Local variables are accessible only within their function.
2. Global variables are accessible across the program, but modifying them requires the `global` keyword.
"""

# Example: Variable Scope
x = 5  # Global variable

def modify_global():
    global x
    x += 10
    return x

print(f"Modified Global x: {modify_global()}")

# Section 4: Lambda Functions
"""
1. Anonymous, one-line functions defined with `lambda`.
2. Useful for short, throwaway functions.
"""

# Example: Lambda Function
square = lambda x: x**2
print(f"Square of 4: {square(4)}")

# Section 5: Higher-Order Functions
"""
1. Functions can take other functions as arguments.
2. Examples: map, filter, reduce.
"""

# Example: Higher-Order Function with Lambda
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared Numbers: {squared_numbers}")

# Section 6: Modularization
"""
1. Group related functions in modules to improve organization and reuse.
2. Modules are `.py` files that can be imported into other scripts.
"""

# Example: Creating and Importing a Module
# Save the following code as mymodule.py
"""
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
"""

# Import and Use the Module
import mymodule

print(f"Addition: {mymodule.add(3, 4)}")
print(f"Multiplication: {mymodule.multiply(3, 4)}")

# Section 7: Packages
"""
1. Packages are directories containing multiple modules.
2. Use `__init__.py` for package initialization.
"""

# Example: Package Usage
# Directory structure:
# mypackage/
#     __init__.py
#     module1.py
#     module2.py
"""
from mypackage import module1, module2
print(module1.function1())
print(module2.function2())
"""

# Section 8: DocStrings
"""
1. Docstrings provide documentation for functions, modules, and classes.
2. Accessed via the `__doc__` attribute.
"""

# Example: DocStrings
def example_function():
    """This is an example function."""
    pass

print(example_function.__doc__)

# Section 9: Task Examples
"""
Task 1: Convert Seconds to Hours, Minutes, and Seconds.
"""

# Example: Convert Seconds
def convert_time(seconds):
    """Converts seconds into hours, minutes, and seconds."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours}h:{minutes}m:{seconds}s"

print(convert_time(4567))

"""
Task 2: Word Censorship
"""

# Example: Censor Words
def censor(text):
    """Replaces words longer than four characters with asterisks."""
    words = text.split()
    censored_words = [w if len(w) <= 4 else '*' * len(w) for w in words]
    return ' '.join(censored_words)

print(censor("The code is fourty amazing"))

"""
Task 3: Calculate Total Price in Supermarket
"""

# Example: Calculate Bill
def print_bill(cart, price_list):
    """Calculates the total price for a cart of items."""
    total = 0
    for item in cart:
        if 'x' in item:
            name, qty = item.split('x')
            total += int(qty) * price_list.get(name.strip(), 0)
        else:
            total += price_list.get(item, 0)
    return total

cart = ["milk", "sugar", "milk x3", "sugar", "beer x12"]
price_list = {"milk": 1.3, "sugar": 1.6, "beer": 1.25}
print(f"Total Bill: €{print_bill(cart, price_list):.2f}")