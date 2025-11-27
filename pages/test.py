from read_dojoshop import load_items
from save_dojoshop import save_items

items = load_items()
print("Original:", items[0])

items[0]["current_stock"] -= 1
save_items(items)

items2 = load_items()
print("After:", items2[0])
