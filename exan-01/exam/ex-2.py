def solve(input):
    num_list = input.split()

    total = int(num_list[-1])
    left_number = 0

    for item in num_list[:-1]:
        if item != "+" and item != "=" and item != "x":
            left_number += int(item)


    print(total - left_number)
    return total - left_number
        

solve ("5 + 8 + x = 30") # should return 17 
solve ("5 + x + 20 = 75") # should return 50 
solve ("x + 7 + 23 = 25") # should return -5 
