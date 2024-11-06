"""
Write a Python program that asks the user for a molecular formula and
displays the number of atoms of each element in the given substance. You
may also assume that the given molecular formula is in correct notation,
which means the names of the elements are as in periodic table (the upper
case for the first character in the element name and the lower case for the
second character). For example Co = Cobalt and CO = Carbon monoxide.
Thus, Na3PO4 is correct notation, na3po4 or NA3PO4 are incorrect
notations.
"""
import re

formulaInput = input("insert forumla: ")

pices = re.findall("[A-Z][a-z]?|[0-9]+", formulaInput)
print(pices)
