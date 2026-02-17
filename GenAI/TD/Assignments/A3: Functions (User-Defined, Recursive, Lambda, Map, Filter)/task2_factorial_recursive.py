# Task 2: Recursive Function - Factorial Utility

def factorial(n):
    if n < 0:
        print("Error: factorial not defined for negative numbers.")
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Tests
print(factorial(5))   # 120
print(factorial(0))    # 1
print(factorial(-3))   # Error message, None
