"""
The palindromic number 434 is interesting because it can be written as the sum of consecutive squares:
112 + 122 + 132 = 121 + 144 + 169 = 434
There are exactly eleven palindromes below one-thousand that can be written as consecutive square
sums, and the sum of these palindromes is 4164. Note that 1 = 0 ** 2 + 1 ** 2 has not been included as this
problem is concerned with the squares of positive integers.
Write a Python function called check which takes an input parameter n and returns the total count of
numbers below n that are both palindromic and can be written as the sum of consecutive squares.
"""
def isPalindrome(input):
    inputList = [input for input in str(input)]
    inputRev = inputList[::-1]

    if inputList == inputRev:
        return True
    
    return False

def sumSqr(num):
    sum = 0
    i = 0
    while i <= int(num**0.5):
        if sum < num:
            sum += (i * i)
        elif sum == num:
            return sum
            break
        elif sum > num:
            sum = 0
            sum += (i * i)
        i += 1
    
    return 0
  

def isSumSqr(input):
    if sumSqr(input) == input:
        return True

    return False

def check(input):
    amount = 0

    for num in range(input):
        if isSumSqr(num) and isPalindrome(num):
            amount += 1

    return amount


print("hi")
print(sumSqr(434))
result = check(1000)
print(result)
# output : 11
