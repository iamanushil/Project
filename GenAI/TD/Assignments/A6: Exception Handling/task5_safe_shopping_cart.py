# Task 5: Mini Program - Safe Shopping Cart
# Loop: input prices until 'q'; ValueError for non-numeric; raise for negative; print count and total.

cart = []

while True:
    user_input = input("Enter price (or 'q' to finish): ").strip()
    if user_input.lower() == "q":
        break
    try:
        price = float(user_input)
        if price < 0:
            raise ValueError("Negative price not allowed")
        cart.append(price)
    except ValueError as e:
        print(e)

print("Number of items:", len(cart))
print("Total bill:", round(sum(cart), 2))
