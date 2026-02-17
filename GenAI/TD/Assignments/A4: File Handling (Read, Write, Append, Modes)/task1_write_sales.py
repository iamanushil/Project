# Task 1: Write Sales Records to a File
# No pandas/csv; use with open() only.
import os
_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_script_dir)

sales = [1200, 450, 980, 1500, 3000]

with open("sales_data.txt", "w") as f:
    for amount in sales:
        f.write(str(amount) + "\n")

with open("sales_data.txt", "r") as f:
    contents = f.read()
    print("Contents of sales_data.txt:")
    print(contents)

# Extra: comma-separated format (writes to same file, overwriting)
# with open("sales_data.txt", "w") as f:
#     f.write(",".join([str(a) for a in sales]))
