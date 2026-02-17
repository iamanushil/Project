# Task 4: Using map() - Apply GST to list of prices
# Uses gst lambda from Task 3

gst = lambda price: price + (0.18 * price)

prices = [100, 250, 400, 1200, 50]
prices_with_gst = list(map(gst, prices))

print("Original prices:", prices)
print("Prices with GST:", prices_with_gst)
