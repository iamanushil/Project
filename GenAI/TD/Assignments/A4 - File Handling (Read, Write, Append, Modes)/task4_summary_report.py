# Task 4: Generate Summary Report from File
# Read sales_data.txt, convert to integers; print total, highest, lowest, average.
import os
_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_script_dir)

with open("sales_data.txt", "r") as f:
    lines = f.readlines()

values = [int(line.strip()) for line in lines if line.strip()]

total_sales = sum(values)
highest_sale = max(values)
lowest_sale = min(values)
average_sale = total_sales / len(values) if values else 0

print("Total Sales:", total_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Average Sale:", round(average_sale, 2))
