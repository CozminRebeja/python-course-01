#leap year identifier
yearInput = int(input("Insert a year: "))

if (yearInput % 4 == 0) and (yearInput % 100 != 0):
    print(f"Year {yearInput} is a leap year")
else:
    print(f"Year {yearInput} is not a leap year")

