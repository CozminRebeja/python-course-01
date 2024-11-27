# Example data for ticket prices
ticket_prices = {
"Standard": 10.50, # Price per ticket for Standard seats
"Premium": 15.99, # Price per ticket for Premium seats
"VIP": 25.0 # Price per ticket for VIP seats
}

total_sales = 0.0

def book_ticket(category, quantity):
    global total_sales
    total_sales += ticket_prices[category] * quantity

book_ticket("Premium", 2)

print(total_sales)