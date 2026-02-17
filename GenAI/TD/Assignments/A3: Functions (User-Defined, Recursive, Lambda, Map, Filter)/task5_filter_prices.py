# Task 5: Using filter() - Filter expensive vs cheap products
prices = [100, 250, 400, 1200, 50, 2000, 850]

above_500 = list(filter(lambda p: p > 500, prices))
at_or_below_500 = list(filter(lambda p: p <= 500, prices))

print("Prices > 500:", above_500)
print("Prices <= 500:", at_or_below_500)
