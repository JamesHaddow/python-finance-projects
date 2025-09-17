# Stock Portfolio Tracker – beginner-friendly and portable

import subprocess
import sys

# Try to import yfinance, install if missing
try:
    import yfinance as yf
except ImportError:
    print("yfinance not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])
    import yfinance as yf

print("Welcome to the Stock Portfolio Tracker!\n")

# Example portfolio – editable
# Format: ("TICKER", quantity, purchase_price_per_share)
portfolio = [
    ("AAPL", 10, 150.0),
    ("MSFT", 5, 280.0),
    ("GOOGL", 2, 120.0)
]

total_value = 0
total_cost = 0

# Print table header
print(f"{'Ticker':<8}{'Qty':<6}{'Purchase':<12}{'Current':<12}{'Value':<12}{'Gain/Loss':<12}")
print("-" * 62)

for ticker, quantity, purchase_price in portfolio:
    stock = yf.Ticker(ticker)
    # Use iloc to avoid FutureWarning
    price = stock.history(period="1d")['Close'].iloc[-1]
    value = price * quantity
    gain_loss = (price - purchase_price) * quantity
    total_value += value
    total_cost += purchase_price * quantity
    print(f"{ticker:<8}{quantity:<6}{purchase_price:<12.2f}{price:<12.2f}{value:<12.2f}{gain_loss:<12.2f}")

total_gain_loss = total_value - total_cost

print("\nTotal Portfolio Value: £{:.2f}".format(total_value))
print("Total Gain/Loss: £{:.2f}".format(total_gain_loss))
