# Task 3: Append New Sales to sales_data.txt
# Run task1 (and optionally task2) first so the file has content.
import os
_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_script_dir)

new_sales = [5000, 2500, 1700]

with open("sales_data.txt", "a") as f:
    for amount in new_sales:
        f.write(str(amount) + "\n")

with open("sales_data.txt", "r") as f:
    contents = f.read()
    print("Updated file contents:")
    print(contents)

# Extra: total number of lines after appending
with open("sales_data.txt", "r") as f:
    line_count = len(f.readlines())
print("Total number of lines:", line_count)
