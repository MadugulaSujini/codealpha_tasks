stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total = 0

print("Available Stocks:")
print(stocks)

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stocks:
    total = stocks[stock_name] * quantity
    print("Total Investment Value =", total)

else:
    print("Stock not found")