# Task 6: Read File Safely (Error handling via condition check only)
# Use os.path.exists(); no exceptions beyond file-related safeguards.
import os

_script_dir = os.path.dirname(os.path.abspath(__file__))

filename = input("Enter filename to open: ").strip()

# If no path separator, look in script folder (A4) so e.g. sales_data.txt is found there
filepath = os.path.join(_script_dir, filename) if os.sep not in filename and filename else filename

if os.path.exists(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    print(content)
else:
    print("File not found. Please check the filename.")
