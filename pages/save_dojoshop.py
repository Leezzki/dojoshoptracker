import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ITEMS_FILE = BASE_DIR / "items.csv"
PURCHASE_LOG_FILE = BASE_DIR / "purchase_log.csv"

def save_items(items):
    fieldnames = ["name", "price", "initial_stock", "current_stock"]
    with open(ITEMS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)

def append_purchase(purchase):
    fieldnames = ["timestamp", "year_group", "item_name", "quantity", "price", "total_cost"]
    file_exists = PURCHASE_LOG_FILE.exists()

    with open(PURCHASE_LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(purchase)
