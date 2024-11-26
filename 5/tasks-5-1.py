"""
Write a function called filemerger(file1, file2) that taskes
two text files as input and creates a third file with contents
of the both input files. The filename of the newly created file
should be returned
"""

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

def filemerger(f1, f2):
    file_out = open("fileOut.txt", "w")
    for line in f1:
        file_out.write(line)
    file_out.write("\n")
    for line in f2:
        file_out.write(line)

    file_out.close()
    print(file_out.name)

filemerger(file1, file2)