# main.py - Task 1, 2, 4: import and test math_utils, string_utils, shop_package

# --- Task 1: math_utils ---
import math_utils
from math_utils import square

print("--- math_utils ---")
print("math_utils.add(3, 5) =", math_utils.add(3, 5))
print("math_utils.subtract(10, 4) =", math_utils.subtract(10, 4))
print("math_utils.square(4) =", math_utils.square(4))
print("square(6) =", square(6))

# --- Task 2: string_utils ---
import string_utils

print("\n--- string_utils ---")
print("capitalize_words('hello world') =", string_utils.capitalize_words("hello world"))
print("reverse_string('abc') =", string_utils.reverse_string("abc"))
print("word_count('one two three') =", string_utils.word_count("one two three"))

# --- Task 4: shop_package ---
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

print("\n--- shop_package ---")
print("disc.apply_discount(1000, 10) =", disc.apply_discount(1000, 10))
print("disc.flat_discount(200) =", disc.flat_discount(200))
print("calculate_total([100, 200, 300]) =", calculate_total([100, 200, 300]))
print("apply_tax(1000) =", apply_tax(1000))
