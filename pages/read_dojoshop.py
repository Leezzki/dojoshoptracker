import csv

def load_items(filename="items.csv"):
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        items = []
        for row in reader:
            # convert strings to ints where needed
            row["price"] = int(row["price"])
            row["initial_stock"] = int(row["initial_stock"])
            row["current_stock"] = int(row["current_stock"])
            items.append(row)
        return items


def load_purchase_log(filename="purchase_log.csv"):
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)