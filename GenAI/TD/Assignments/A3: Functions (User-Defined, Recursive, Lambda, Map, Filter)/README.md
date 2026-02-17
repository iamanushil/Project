# GenAI - Assignment 3: Functions (User-Defined, Recursive, Lambda, Map, Filter)

Reusable functions for billing/utility tasks. No classes, packages, exceptions, or file handling.

## Which file runs which task

| File | Task |
|------|------|
| `task1_price_after_discount.py` | **Task 1** — `apply_discount(price, discount_percent=5)`, cap 60% |
| `task2_factorial_recursive.py` | **Task 2** — Recursive `factorial(n)`, edge cases 0/1, negative error |
| `task3_gst_lambda.py` | **Task 3** — Lambda `gst` (18% GST); extra: GST + discount lambda |
| `task4_map_gst.py` | **Task 4** — `map(gst, prices)` → `prices_with_gst` |
| `task5_filter_prices.py` | **Task 5** — `filter()` for >500 and ≤500 |
| `task6_process_prices.py` | **Task 6** — `process_prices(prices)`: map 10% discount, filter >300 |
| `task7_menu_functions.py` | **Task 7** — Menu using add_price, get_average_price, get_max_price |

## How to run

From this folder:

```bash
python task1_price_after_discount.py
python task2_factorial_recursive.py
python task3_gst_lambda.py
python task4_map_gst.py
python task5_filter_prices.py
python task6_process_prices.py
python task7_menu_functions.py   # interactive menu
```
