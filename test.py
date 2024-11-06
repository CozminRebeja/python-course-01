def isPalindrome(input):
    input_str = str(input)
    return input_str == input_str[::-1]

def canBeWrittenAsSumOfSquares(num):
    for start in range(1, int(num**0.5) + 1):
        sum_squares = 0
        for i in range(start, int(num**0.5) + 1):
            sum_squares += i * i
            if sum_squares == num:
                return True
            if sum_squares > num:
                break
    return False

def check(input):
    amount = 0
    for num in range(1, input):
        if isPalindrome(num) and canBeWrittenAsSumOfSquares(num):
            amount += 1
    return amount

# Test the function
result = check(1000)
print(result) 
