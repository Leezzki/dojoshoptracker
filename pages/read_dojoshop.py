import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ITEMS_FILE = BASE_DIR / "items.csv"
PURCHASE_LOG_FILE = BASE_DIR / "purchase_log.csv"

def load_items():
    items = []
    with open(ITEMS_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append({
                "name": row["name"],
                "price": int(row["price"]),
                "initial_stock": int(row["initial_stock"]),
                "current_stock": int(row["current_stock"]),
            })
    return items

def load_purchase_log():
    purchases = []
    try:
        with open(PURCHASE_LOG_FILE, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            purchases = list(reader)
    except FileNotFoundError:
        pass
    return purchases
