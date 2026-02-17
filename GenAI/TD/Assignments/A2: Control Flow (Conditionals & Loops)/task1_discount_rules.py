# Task 1: Discount Rules (if/elif/else)
# Order processing: read order_amount, apply discount, print final amount.

user_input = input("Enter order amount: ")
try:
    order_amount = float(user_input)
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

# Apply discount (conditionals only)
if order_amount >= 2000:
    discount_pct = 15
elif order_amount >= 1500:
    discount_pct = 10
elif order_amount >= 1000:
    discount_pct = 7
else:
    discount_pct = 0

subtotal = order_amount * (1 - discount_pct / 100)
print("Discount:", discount_pct, "%")
print("Subtotal after discount:", round(subtotal, 2))

# Extra: 5% tax after discount
tax_rate = 5
tax = subtotal * (tax_rate / 100)
final_total = subtotal + tax
print("Tax (5%):", round(tax, 2))
print("Final total:", round(final_total, 2))
