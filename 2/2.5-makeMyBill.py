"""
A craftsman has to prepare a bill at the end of each week.
To do this, he tells his company how many meters of
cable he has laid and how many hours it took him.

The company calculates the costs as follows:
• A fully used cable drum with 500 meters of cable costs €1000.
• Any additional cable, from a started drum, cost €3 per meter.
• The craftsman has an hourly rate of €50.
• If he has worked more than 40 hours, he is entitled to double
the hourly rate for each hour of overtime.

Write a Python program that calculates the overall costs.
Read the meters of cable and the hours from the console
and print the costs to the console.
"""

def main():
    meters_input = int(input("meters:"))
    hours_input = int(input("hours: "))

    total = cableCalc(meters_input) + hourCalc(hours_input)
    print("--------------")
    print(f"total: ${total}")

def cableCalc(meters):
    if meters % 500 == 0:
        return (meters / 500) * 1000
    else:
        remainder = (meters % 500) * 3

        return ((meters // 500) * 1000) + remainder

def hourCalc(hours):
    total = 0
    for hour in range(hours):
        if hour < 40:
            total += 50
        else:
            total += 100

    return total


main()
