# Task 3: Product Pricing (Dictionaries) — generic add, remove, average methods

def add_product(d, name, price):
    """Add or update a product. Modifies d in place; returns None."""
    d[name] = price

def remove_product(d, name):
    """Remove product by name. No error if name not in d."""
    if name in d:
        del d[name]
        return True
    return False

def average_price(d):
    """Average of all prices. Returns 0 if d is empty. Dict + basic arithmetic only."""
    if not d:
        return 0
    return sum(d.values()) / len(d)

# 1. Dictionary: product name -> price (at least 6 entries)
price_dict = {
    "Laptop": 899.99,
    "Mouse": 29.99,
    "Keyboard": 79.99,
    "Monitor": 249.99,
    "Headphones": 59.99,
    "Webcam": 89.99,
}
print("Initial price_dict:", price_dict)

# 2a. Add a new product with price
add_product(price_dict, "USB Hub", 24.99)
print("After adding USB Hub:", price_dict)

# 2b. Update the price of an existing product
add_product(price_dict, "Laptop", 799.99)
print("After updating Laptop price:", price_dict)

# 2c. Remove a product by name (graceful if not present)
remove_product(price_dict, "Webcam")
remove_product(price_dict, "Unknown Product")  # no error
print("After removals:", price_dict)

# 3. Average price
print("Average price of all products:", round(average_price(price_dict), 2))

# Extra: Product with max and min price
print("Product with max price:", max(price_dict, key=price_dict.get))
print("Product with min price:", min(price_dict, key=price_dict.get))
