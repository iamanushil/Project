# Task 4: Combined Operations (products list + price_dict -> catalog -> category_to_products)

# Existing products list and categories (aligned with Task 1 / Task 2)
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam", "USB Hub"]
categories = ["Electronics", "Electronics", "Electronics", "Electronics", "Audio", "Electronics", "Accessories"]

# price_dict from Task 3 (after updates)
price_dict = {
    "Laptop": 799.99,
    "Mouse": 29.99,
    "Keyboard": 79.99,
    "Monitor": 249.99,
    "Headphones": 59.99,
    "USB Hub": 24.99,
}

# Step 1: catalog = list of (product_name, price, category)
catalog = []
for i, name in enumerate(products):
    if name in price_dict and i < len(categories):
        catalog.append((name, price_dict[name], categories[i]))
print("Catalog (product_name, price, category):", catalog)

# Step 2: category_to_products: category -> list of product names
category_to_products = {}
for name, price, cat in catalog:
    if cat not in category_to_products:
        category_to_products[cat] = []
    category_to_products[cat].append(name)
print("category_to_products:", category_to_products)

# Step 3: Category with max number of products, then print those products
max_category = max(category_to_products, key=lambda c: len(category_to_products[c]))
products_in_max_category = category_to_products[max_category]
print("Category with most products:", max_category)
print("Products in that category:", products_in_max_category)
