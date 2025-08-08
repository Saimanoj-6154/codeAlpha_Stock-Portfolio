# Stock Portfolio Tracker

# Hardcoded dictionary for stock prices (in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "AMZN": 140,
    "MSFT": 310
}

# Function to calculate total investment
def calculate_investment():
    total_investment = 0
    portfolio = {}

    while True:
        stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print(f"❌ Stock '{stock}' not found in database.")
            continue

        try:
            qty = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("⚠ Please enter a valid number.")
            continue

        investment = stock_prices[stock] * qty
        portfolio[stock] = portfolio.get(stock, 0) + investment
        total_investment += investment

    return total_investment, portfolio

# Function to optionally save results
def save_to_file(total, portfolio):
    choice = input("Do you want to save results to a file? (y/n): ").lower()
    if choice == "y":
        file_type = input("Enter file type (.txt or .csv): ").lower()
        if file_type == ".txt":
            with open("portfolio.txt", "w") as f:
                f.write("Stock Portfolio Summary\n")
                for stock, amount in portfolio.items():
                    f.write(f"{stock}: ${amount}\n")
                f.write(f"Total Investment: ${total}\n")
            print("✅ Data saved to portfolio.txt")

        elif file_type == ".csv":
            with open("portfolio.csv", "w") as f:
                f.write("Stock,Investment\n")
                for stock, amount in portfolio.items():
                    f.write(f"{stock},{amount}\n")
                f.write(f"Total,{total}\n")
            print("✅ Data saved to portfolio.csv")
        else:
            print("⚠ Unsupported file type.")

# Main execution
if __name__ == "__main__":
    total, portfolio = calculate_investment()
    print("\n📊 Portfolio Summary:")
    for stock, amount in portfolio.items():
        print(f"{stock}: ${amount}")
    print(f"💰 Total Investment: ${total}")

    save_to_file(total, portfolio)
