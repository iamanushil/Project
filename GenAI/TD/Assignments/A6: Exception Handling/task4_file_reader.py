# Task 4: File Reader with Exception Handling
# FileNotFoundError, PermissionError; print first 3 lines; finally "File operation attempted."

filename = input("Enter filename: ").strip()

try:
    with open(filename, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines[:3]):
        print(line.rstrip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File operation attempted.")
