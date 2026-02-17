# Task 2: Bill Calculator with Error Handling
# Sum only valid positive prices; TypeError for non-numbers, raise ValueError for negative.

prices = [120, 350, "abc", 500, -200, 800]
total = 0

for p in prices:
    try:
        print("\nItem:", p)
        if p < 0:
            raise ValueError("Negative price not allowed")
        total = total + p
        print("Running total:", total)
    except TypeError:
        pass  # skip non-numeric (e.g. 'abc')
    except ValueError as e:
        print(e)

print("Final total:", total)
