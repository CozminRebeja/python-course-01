def is_palindromic(x):
    """
    This function checks if a given integer x is a palindrome.
    A number is palindromic if it reads the same forward and backward.
    """
    original = x
    reversed_num = 0
    
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10  # Build the reversed number
        x //= 10  # Remove the last digit from x
    
    return reversed_num == original

def consecutive_squares(x):
    """
    This function checks if the number x can be expressed as the sum of consecutive squares.
    """
    start = 1
    while start * start < x:
        sum_of_squares = 0
        i = start
        
        while sum_of_squares < x:
            sum_of_squares += i * i
            if sum_of_squares == x:
                return True
            i += 1
        
        start += 1
    
    return False

def check(n):
    """
    This function counts how many numbers less than n are both palindromic
    and can be expressed as the sum of consecutive squares.
    """
    count = 0
    
    for num in range(1, n):
        if is_palindromic(num) and consecutive_squares(num):
            count += 1
    
    return count

# Example usage
result = check(1000)
print(f"Result: {result}")
