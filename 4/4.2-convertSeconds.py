"""
Write a Python function convertTime that takes
the number of seconds as input
and returns a string representing the hours, minutes and seconds.
"""

# 1 min = 60 sec
# 1 h = 60 min

def convertTime(x):
    seconds, minutes, hours = x, 0, 0
    while x > 0:
        x -= 60
        if x > 0 :
            seconds -= 60
            minutes += 1
        if minutes == 60:
            hours += 1
            minutes = 0
        
    return(f"{hours}H:{minutes}M:{seconds}S")

def main():
    print(convertTime(1234))
    print(convertTime(4567))

if __name__ == "__main__":
    main()


#convertTime(1234) should return: 0h:20M:34S