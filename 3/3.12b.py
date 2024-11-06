# Explain how this line cleverly deletes all the multiple occurrences of characters:

print("".join(set("interesting-exercise-and-quite-useful")))

"""
it deletes all multiple occurences of characters by converting the string into a set of characters
* a set will always delete multiple occurences of the same item *
"""

listTest = {22, 44, 55, 66, 66, 55}

list2 = set(listTest)
print(list2)