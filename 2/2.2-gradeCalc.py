#Grade Calculator

scoreInput = int(input("What is your score: "))

if 0 < scoreInput <= 60:
    print("F")
elif 61 < scoreInput <= 70:
    print("D")    
elif 71 < scoreInput <= 80:
    print("C")
elif 81 < scoreInput <= 90:
    print("B")
elif 91 < scoreInput <= 100:
    print("A") 

