"""
A cashier in a supermarket scans the items as they come on the
conveyer belt. Whenever the customer buys multiple number 
of the same item (e.g., two bottles of milk), the cashier 
scans only one item and enter the number of times that item 
was bought (e.g., scan a bottle of milk and type in ‘x2’). 

Let us assume the data about the cashiers scanning activities 
is stored in a list, with items in the order of their position 
on the belt.

Note that multiple copies of the same item may not 
be together on the belt.

Example shopping cart:
cart = ["milk", "sugar", "milk", "x3", "sugar", "beer", "x12", "bread", "milk", "butter",
"x2", "salad", "x3", "juice", "sugar", "x2", "juice", "butter", "sugar", "flour"]
Write a python function called printBill, that takes a price list of items and a list of
scanned items and returns the total price.
Example price list:

pricelist = {"milk":1.3, "sugar":1.6, "beer":1.25, "bread":2.6,
"butter":1.99, "salad":0.89, "flour":1.2, "juice":1.2}
printBill(cart, pricelist) Returns : 44.34
"""

cart = ["milk", "sugar", "milk", "x3", "sugar", "beer", "x12", "bread", "milk", "butter", "x2", "salad", "x3", "juice", "sugar", "x2", "juice", "butter", "sugar", "flour"]
pricelist = {"milk":1.3, "sugar":1.6, "beer":1.25, "bread":2.6, "butter":1.99, "salad":0.89, "flour":1.2, "juice":1.2}

def printBill(cart, pricelist):
    temp_list = []
    total = 0

    for item in cart:
        if item[1:].isdigit and item[0] == "x":
            mult = int(item[1:])
            for i in range(mult-1):
                temp_list.append(temp_list[-1])
        else:
            temp_list.append(item)


    for item in temp_list:
        total += pricelist[item]

    print(total)

printBill(cart, pricelist)