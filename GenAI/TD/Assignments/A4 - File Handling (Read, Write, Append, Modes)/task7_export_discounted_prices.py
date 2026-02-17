# Task 7: Mini Project - Export Discounted Prices
# prices dict → user discount % → discount_report.txt (Product | Original | Discounted), then read and print.
import os
_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_script_dir)

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000,
}

discount_pct = float(input("Enter discount percentage: ").strip())
discounted_list = []

with open("discount_report.txt", "w") as f:
    for product, original in prices.items():
        discounted = original * (1 - discount_pct / 100)
        discounted_list.append(discounted)
        f.write(f"{product} | {original} | {round(discounted, 2)}\n")
    # Extra: summary at bottom
    f.write(f"\nTotal Items: {len(prices)}\n")
    avg_discounted = sum(discounted_list) / len(discounted_list) if discounted_list else 0
    f.write(f"Average Discounted Price: {round(avg_discounted, 2)}\n")

print("\nContents of discount_report.txt:")
with open("discount_report.txt", "r") as f:
    print(f.read())
