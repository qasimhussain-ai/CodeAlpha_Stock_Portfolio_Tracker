prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

total = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("Enter stock symbol (AAPL, TSLA...) or 'done': ").upper()
    if stock == "DONE":
        break
    
    if stock not in prices:
        print("Stock not found!")
        continue
    
    qty = int(input("Enter quantity: "))
    total += prices[stock] * qty

print("\nTotal Investment =", total)

# Save to file
with open("portfolio_result.txt", "w") as f:
    f.write(f"Total Portfolio Investment = {total}")

print("\nSaved to portfolio_result.txt")
