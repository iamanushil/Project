# Task 3: Lambda Function - GST Calculator (18% GST)
gst = lambda price: price + (0.18 * price)

print(gst(100))  # 118.0

# Extra: lambda for final price after GST and discount (e.g. 10% discount after GST)
gst_then_discount = lambda price, discount_pct=10: gst(price) * (1 - discount_pct / 100)

print(gst_then_discount(100))           # 118 * 0.9 = 106.2
print(gst_then_discount(100, 5))        # 118 * 0.95 = 112.1
