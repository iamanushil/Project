# Task 1: Safe Division Utility
# try/except ValueError, ZeroDivisionError; result in else; "Operation Complete" in finally.

numerator = input("Enter numerator: ")
denominator = input("Enter denominator: ")

try:
    num = float(numerator)
    den = float(denominator)
    result = num / den
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")
else:
    print("Result:", result)
finally:
    print("Operation Complete")
