import yfinance as yf
from datetime import datetime

users = {}  # {username: password}
portfolios = {}  # {username: {symbol: {'shares': x, 'price': y, 'date': z}}}


def get_current_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1d")
        return hist['Close'].iloc[-1] if not hist.empty else None
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None


def register():
    username = input("Choose a username: ").strip()
    password = input("Choose a password: ").strip()
    if username in users:
        print("Username already exists!")
    else:
        users[username] = password
        portfolios[username] = {}
        print("Registered successfully!")


def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    if users.get(username) == password:
        print(f"Welcome, {username}!")
        return username
    else:
        print("Invalid credentials")
        return None


def add_stock(user):
    symbol = input("Stock symbol: ").upper().strip()
    try:
        shares = float(input("Number of shares: "))
        price = float(input("Purchase price: "))
        date = input("Purchase date (YYYY-MM-DD): ")
        datetime.strptime(date, "%Y-%m-%d")

        portfolios[user][symbol] = {
            'shares': shares,
            'price': price,
            'date': date
        }
        print(f"Added {shares} shares of {symbol}")
    except ValueError:
        print("Invalid input.")


def remove_stock(user):
    symbol = input("Stock symbol to remove: ").upper().strip()
    if symbol in portfolios[user]:
        del portfolios[user][symbol]
        print(f"Removed {symbol}")
    else:
        print("Stock not found in your portfolio.")


def view_portfolio(user):
    if not portfolios[user]:
        print("Portfolio is empty.")
        return

    total_value = 0
    total_cost = 0
    print("\nYour Portfolio:")

    for symbol, data in portfolios[user].items():
        price = get_current_price(symbol)
        if price is None:
            print(f"Could not fetch price for {symbol}")
            continue

        shares = data['shares']
        cost = shares * data['price']
        value = shares * price
        gain = value - cost

        total_cost += cost
        total_value += value

        print(f"{symbol}: {shares} shares | Avg Price: ${data['price']:.2f} | "
              f"Current: ${price:.2f} | Gain/Loss: ${gain:.2f}")

    print(f"\nTotal Invested: ${total_cost:.2f}")
    print(f"Current Value: ${total_value:.2f}")
    print(f"Net Gain/Loss: ${total_value - total_cost:.2f}")


def main():
    while True:
        print("\n=== Stock Portfolio Tracker ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user:
                while True:
                    print("\n--- Portfolio Menu ---")
                    print("1. Add Stock")
                    print("2. Remove Stock")
                    print("3. View Portfolio")
                    print("4. Logout")

                    action = input("Choose an action: ").strip()
                    if action == '1':
                        add_stock(user)
                    elif action == '2':
                        remove_stock(user)
                    elif action == '3':
                        view_portfolio(user)
                    elif action == '4':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
