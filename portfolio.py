import csv

ticker = input("(AAPL): ")
buy_price = float(input("(Buy Price:) "))
shares = float(input("(Shares): "))

current_price = 180.0

invested_capital = shares * buy_price
current_value = shares * current_price
gain_loss_pct = ((current_value - invested_capital) / invested_capital) * 100

print("\n")
print(f":${invested_capital}")
print(f":${current_value}")
print(f":{gain_loss_pct:.2f}%")

with open("portfolio_summary.csv", mode="w", newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["Ticker", "shares", "buy_price", "invested_capital", "current_value", "Gain_loss %"])

    writer.writerow([ticker,shares, buy_price,current_price, invested_capital,current_value, f"{gain_loss_pct:.2f}%"])
print("\n 'portfolio_summary.csv'!")