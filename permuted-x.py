def convert_SortedList(x):
    numList = [x for x in str(x)]
    numList.sort()

    return numList

def sameDigit(x, y):
    x_list = convert_SortedList(x) 
    y_list = convert_SortedList(y)

    if x_list == y_list:
        return True
    return False
    

def permutedX (p, q): 
    i = p + 1
    while i <= q:
        if (sameDigit(i, i * 2) and 
            sameDigit(i, i * 3) and
            sameDigit(i, i * 4) and
            sameDigit(i, i * 5)):
                return i
        i += 1

result = permutedX (1, 1000000)
print(result)
