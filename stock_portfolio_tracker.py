stock_prices = {
    "AAPL": 180,   
    "TSLA": 250,   
    "GOOGL": 2800, 
    "MSFT": 350,   
    "AMZN": 130    
}

num_stocks = int(input("How many different stocks do you own? "))
portfolio = {}
for i in range(num_stocks):
    stock_name = input(f"Enter stock name ({i+1}): ").upper()  
    quantity = int(input(f"Enter quantity of {stock_name}: "))
    if stock_name in stock_prices:
        portfolio[stock_name] = quantity
    else:
        print(f"❌ {stock_name} is not in our stock list. Skipping it.")
total_value = 0

print("\n📊 Your Stock Portfolio:")
print("---------------------------")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares × ₹{price} = ₹{value}")

print("---------------------------")
print(f"💰 Total Investment Value: ₹{total_value}")

save = input("\nDo you want to save this report to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Your Stock Portfolio:\n")
        file.write("---------------------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ₹{price} = ₹{value}\n")
        file.write("---------------------------\n")
        file.write(f"Total Investment Value: ₹{total_value}\n")
    print("✅ Report saved as 'portfolio_report.txt'")

