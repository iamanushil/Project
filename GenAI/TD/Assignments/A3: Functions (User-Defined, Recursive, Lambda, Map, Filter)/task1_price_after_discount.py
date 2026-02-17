# Task 1: Basic Function - Price After Discount
# apply_discount(price, discount_percent) with default 5%; cap discount at 60%.

def apply_discount(price, discount_percent=5):
    if discount_percent > 60:
        discount_percent = 60
    return price * (1 - discount_percent / 100)


# Tests
print(apply_discount(1000, 10))   # 900.0
print(apply_discount(500))        # 475.0 (default 5%)
print(apply_discount(100, 70))    # 40.0 (capped at 60%)
