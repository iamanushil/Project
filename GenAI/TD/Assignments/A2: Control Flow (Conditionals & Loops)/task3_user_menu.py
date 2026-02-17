# Task 3: User Menu (while loop + break/continue)
# Menu: 1 = add order, 2 = show orders and total after discounts, q = quit.

orders = []

while True:
    print("\n--- Menu ---")
    print("1: Add order amount")
    print("2: Show all orders and total (after discounts)")
    print("q: Quit")
    choice = input("Choice: ").strip().lower()

    if choice == "q":
        break

    if choice == "1":
        user_input = input("Enter order amount: ")
        try:
            amount = float(user_input)
            orders.append(amount)
            print("Order added.")
        except ValueError:
            print("Invalid number. Try again.")
        continue

    if choice == "2":
        if len(orders) == 0:
            print("No orders yet.")
        else:
            total_after_discounts = 0
            print("Orders and final amount after discount:")
            for order_amount in orders:
                if order_amount >= 2000:
                    discount_pct = 15
                elif order_amount >= 1500:
                    discount_pct = 10
                elif order_amount >= 1000:
                    discount_pct = 7
                else:
                    discount_pct = 0
                final = order_amount * (1 - discount_pct / 100)
                total_after_discounts = total_after_discounts + final
                print("  ", order_amount, "->", discount_pct, "% ->", round(final, 2))
            print("Total (after discounts):", round(total_after_discounts, 2))
        continue

    # Invalid option: re-show menu
    print("Invalid option. Please choose 1, 2, or q.")
    continue

print("Goodbye.")
