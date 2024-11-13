list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

subList = ["h", "i", "j"]
list1.insert(2, subList)

print(list1)