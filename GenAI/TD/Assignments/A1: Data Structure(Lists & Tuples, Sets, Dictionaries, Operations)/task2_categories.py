# Task 2: Categories (Sets)
# Using parallel list since product names don't contain categories
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"]
categories = ["Electronics", "Electronics", "Electronics", "Electronics", "Audio", "Electronics"]

# 1. Create set of categories from parallel list
categories_set = set(categories)
print("Categories set:", categories_set)

# 2. Add new category; adding duplicate shows it's ignored
categories_set.add("Accessories")
print("After adding 'Accessories':", categories_set)
categories_set.add("Accessories")  # duplicate
print("After adding duplicate 'Accessories':", categories_set)

# 3. Check if category exists (boolean)
print("'Electronics' in set:", "Electronics" in categories_set)
print("'Books' in set:", "Books" in categories_set)

# Extra: Total number of unique categories
print("Total unique categories:", len(categories_set))
