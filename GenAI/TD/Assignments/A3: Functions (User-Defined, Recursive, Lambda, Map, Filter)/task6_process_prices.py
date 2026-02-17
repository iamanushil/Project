# Task 6: Combined Utility - map 10% discount, then filter prices > 300

def process_prices(prices):
    discounted_prices = list(map(lambda p: p * 0.9, prices))
    filtered_prices = list(filter(lambda p: p > 300, discounted_prices))
    return discounted_prices, filtered_prices


# Test
discounted, filtered = process_prices([100, 500, 900, 50, 750])
print("Discounted prices (10% off):", discounted)
print("Filtered (discounted > 300):", filtered)
