"""
Write a Python program which asks the user for the total number
electricity units to be charged. Calculate total
electricity bill according to the given condition.

• For first 50 units €0.50/unit
• For next 100 units €0.75/unit
• For next 100 units €1.20/unit
• For remaining units above 250 €. 1.50/unit plus an additional surcharge of 20% is added to the bill

Example:
Enter electricity units: 500
Total bill= € 714.0
"""

user_input = int(input("bill units: "))
total = 0.0

for unit in range(user_input):
    if unit < 50:
        total += 0.50
    elif unit < 150:
        total += 0.75
    elif unit < 250:
        total += 1.20
    else:
        total += 1.50
    
if user_input > 250:
    total += (total * 0.2)

print(f"total bill: {total}")