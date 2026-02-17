# Task 5: Loop Control (break & continue)
# -1 = corrupted (break), 0 = no sales (continue), else add to total_sales.

daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

for value in daily:
    if value == -1:
        print("Corrupted data (-1). Stopping.")
        break
    if value == 0:
        continue
    total_sales = total_sales + value
    print("Running total:", total_sales)

print("Final total sales:", total_sales)
