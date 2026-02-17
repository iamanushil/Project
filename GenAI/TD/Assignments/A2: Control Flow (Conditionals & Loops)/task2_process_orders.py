# Task 2: Process Multiple Orders (for loop)
# Apply Task 1 discount rules to each order; print table and total revenue.

orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
orders_with_discount = 0

print("order_amount -> discount% -> final_amount")
print("-" * 45)

for order_amount in orders:
    if order_amount >= 2000:
        discount_pct = 15
    elif order_amount >= 1500:
        discount_pct = 10
    elif order_amount >= 1000:
        discount_pct = 7
    else:
        discount_pct = 0

    if discount_pct > 0:
        orders_with_discount = orders_with_discount + 1

    final_amount = order_amount * (1 - discount_pct / 100)
    total_revenue = total_revenue + final_amount
    print(order_amount, "->", discount_pct, "% ->", round(final_amount, 2))

print("-" * 45)
print("Total revenue after discounts:", round(total_revenue, 2))
# Extra: number of orders that received a discount
print("Orders that received a discount:", orders_with_discount)
