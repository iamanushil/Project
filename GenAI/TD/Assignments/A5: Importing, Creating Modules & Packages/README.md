# GenAI - Assignment 5: Importing, Creating Modules & Packages

Structure: `main.py`, `math_utils.py`, `string_utils.py`, `shop_package/` with `__init__.py`, `discount.py`, `billing.py`.

## Tasks

- **Task 1 – math_utils**: `add(a, b)`, `subtract(a, b)`, `square(n)`; in main: `import math_utils` and `from math_utils import square`.
- **Task 2 – string_utils**: `capitalize_words(text)`, `reverse_string(text)`, `word_count(text)`; imported and tested in main.
- **Task 3 – shop_package**: `discount.py` has `apply_discount(price, percent)` and `flat_discount(price)`; `billing.py` has `calculate_total(prices)` and `apply_tax(amount)`; `__init__.py` re-exports them.
- **Task 4 – main.py**: `import shop_package.discount as disc`, `from shop_package.billing import calculate_total, apply_tax`; calls every package function.

## How to run

From this folder:

```bash
python main.py
```

No OOP, exceptions, or file I/O. Simple function logic only.
