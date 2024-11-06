#The steinhaus Cyclus
inputNum = int(input("Number: "))

def sqrSum(num) -> int:
    sum = 0
    while num > 0:
        x = num % 10
        sum += (x ** 2)
        num //= 10
    
    return sum


x = sqrSum(inputNum)
active = 0

while active < 2:
    print(x)
    if x == 1 or x == 145:
        active += 1
    
    x = sqrSum(x)

print("Done")