"""
Write a function called filestripper(file, word) that deletes 
all the occurences of the given word for that file
"""

file = open("in.txt", "r")


def filestripper(file, word):

    file_out = open("out.txt", "w")
    
    for line in file:
        file_out.write(line.strip("word"))

    file_out.close()
    print("Done")

filestripper(file, "test")