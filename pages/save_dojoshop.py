import csv

def save_items(items, filename="items.csv"):
    fieldnames = ["name", "price", "initial_stock", "current_stock"]
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)

def append_purchase(purchase, filename="purchase_log.csv"):
    fieldnames = ["timestamp", "year_group", "item_name", "quantity", "price", "total_cost"]
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(purchase)