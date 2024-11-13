def roads_to(num):
    ways = [0] * (num + 1)
    ways[0] = 1  # There is one way to make the number 0, which is by using no numbers at all

    # Loop over each integer from 1 to num-1
    for i in range(1, num):
        print(i)
        for j in range(i, num + 1):
            print(j)
            ways[j] += ways[j - i]
            print("---")

    return ways[num]

# Example usage
print(roads_to(5))    # Output: 6