# Write a Python program that prompts the user for his/her amount of
# money, then reports how many Apples the person can afford, and how
# much more money he/she will need to afford an additional Apple.
# Cost of an Apple = 3 Euros

userInput = input("How much money do you have: ")
userMoney = int(userInput)

appleCost = 3

appleAmmount = userMoney // appleCost

print("You can buy ", int(appleAmmount), " apples.")