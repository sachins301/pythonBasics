#1. Grocery Budget Tracker (3 points)

fruit_price = float(input("Enter the cost of fruits: "))
veggies_proce = float(input("Enter the cost of vegetables: "))
meat_price = float(input("Enter the cost of meat: "))
dairy_price = float(input("Enter the cost of dairy products: "))

total_price = fruit_price + veggies_proce + meat_price + dairy_price
print(f"Total Cost: {total_price}$")

#2. Book Purchase in Euros (3 points)
book_price_euro = float(input("Enter the book price in Euros €: "))
book_nos = int(input("Enter the number of book: "))
eurusd = float(input("Enter the current Euros to USD exchange rate: "))

book_total = book_nos * book_price_euro * eurusd
print(f"The total cost of books is {book_total:.2f}$")

