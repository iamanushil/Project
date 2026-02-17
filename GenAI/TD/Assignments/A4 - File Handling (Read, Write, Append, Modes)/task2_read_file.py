# Task 2: Read File in Different Ways (sales_data.txt)
# Run task1_write_sales.py first so the file exists.
import os
_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_script_dir)

# 1. Read entire file with .read()
with open("sales_data.txt", "r") as f:
    full = f.read()
print("Using .read():")
print(full)

# 2. Read first line with .readline()
with open("sales_data.txt", "r") as f:
    first_line = f.readline()
print("First line (.readline()):", first_line.strip())

# 3. Read all lines with .readlines(), convert to list of integers
with open("sales_data.txt", "r") as f:
    lines = f.readlines()
amounts = [int(line.strip()) for line in lines if line.strip()]
print("List of integers (.readlines()):", amounts)
