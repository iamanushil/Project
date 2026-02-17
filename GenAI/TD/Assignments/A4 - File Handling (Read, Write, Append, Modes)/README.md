# GenAI - Assignment 4: File Handling (Read, Write, Append, Modes)

Retail analytics file utilities. No pandas, no csv module; use `with open()` only.

## Which file runs which task

| File | Task |
|------|------|
| `task1_write_sales.py` | **Task 1** — Write sales list to `sales_data.txt` (one per line), reopen and print |
| `task2_read_file.py` | **Task 2** — .read(), .readline(), .readlines() → list of integers |
| `task3_append_sales.py` | **Task 3** — Append new sales, reopen and print; extra: line count |
| `task4_summary_report.py` | **Task 4** — Read sales_data.txt, print total/highest/lowest/average |
| `task5_product_info_file.py` | **Task 5** — User inputs 3 products (name, price), write to products.txt, read and print |
| `task6_read_file_safely.py` | **Task 6** — User enters filename; if exists read and print, else "File not found" (os.path.exists) |
| `task7_export_discounted_prices.py` | **Task 7** — prices dict, user discount %, write discount_report.txt, read and print; extra: summary (total items, avg discounted) |

## How to run

Run from this folder. Task 1–3 create/update `sales_data.txt`; Task 4 reads it.

```bash
python task1_write_sales.py
python task2_read_file.py
python task3_append_sales.py
python task4_summary_report.py
python task5_product_info_file.py   # interactive: 3 products
python task6_read_file_safely.py    # interactive: enter filename
python task7_export_discounted_prices.py   # interactive: discount %
```

Files created: `sales_data.txt`, `products.txt`, `discount_report.txt` (in this folder).
