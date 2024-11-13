def count_digits(n):
    """
    This function returns a list that contains the count of each digit (0-9) in the given number.
    """
    count = [0] * 10  # Create a list with 10 zeros for digits 0-9
    
    while n > 0:
        count[n % 10] += 1  # Increment the count of the current last digit
        n //= 10  # Remove the last digit from n by integer division
    
    return count

def check_same(x, y):
    """
    This function checks if two numbers x and y have the same digits by comparing their digit frequency lists.
    """
    return count_digits(x) == count_digits(y)

def permutedX(p, q):
    """
    This function finds the smallest integer x between p and q such that 2x, 3x, 4x, and 5x all contain the same digits as x.
    """
    for x in range(p, q + 1):
        if (check_same(x, 2 * x) and
            check_same(x, 3 * x) and
            check_same(x, 4 * x) and
            check_same(x, 5 * x)):
            return x  # Return the smallest x that meets the condition
    
    return -1  # Return -1 if no such number exists

# Example usage
result = permutedX(1, 150000)
if result != -1:
    print(f"The smallest x between 1 and 150000 such that 2x, 3x, 4x, 5x contain the same digits is: {result}")
else:
    print(f"No such number exists between 1 and 150000.")

print("gicu suge")
print("gicu linge")
# testing updates