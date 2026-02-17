# Task 5: Create Product Info File (User Input)
# 3 products: name and price; write "ProductName | Price" to products.txt, then read and print.
import os
_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_script_dir)

products = []
for i in range(3):
    name = input(f"Product {i + 1} name: ").strip()
    price = input(f"Product {i + 1} price: ").strip()
    products.append((name, price))

with open("products.txt", "w") as f:
    for name, price in products:
        f.write(f"{name} | {price}\n")

print("\nContents of products.txt:")
with open("products.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            print(line)
