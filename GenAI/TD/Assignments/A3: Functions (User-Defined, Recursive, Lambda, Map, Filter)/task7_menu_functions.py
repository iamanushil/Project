# Task 7: Mini Menu Using Functions (loops + function calls only)

def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    if len(prices_list) == 0:
        return None
    return max(prices_list)


prices_list = []

while True:
    print("\n--- Menu ---")
    print("  1: Add price")
    print("  2: Show average price")
    print("  3: Show highest price")
    print("  q: Quit")
    choice = input("Choice: ").strip().lower()

    if choice == "q":
        break
    if choice == "1":
        user_input = input("Enter price: ").strip()
        try:
            p = float(user_input)
            add_price(prices_list, p)
            print("Price added.")
        except ValueError:
            print("Invalid number.")
        continue
    if choice == "2":
        avg = get_average_price(prices_list)
        if len(prices_list) == 0:
            print("No prices yet.")
        else:
            print("Average price:", round(avg, 2))
        continue
    if choice == "3":
        mx = get_max_price(prices_list)
        if mx is None:
            print("No prices yet.")
        else:
            print("Highest price:", mx)
        continue
    print("Invalid option.")

print("Goodbye.")
