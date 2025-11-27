import streamlit as st


st.title("Admin Panel")
st.subheader("Restock")



# Builds list of item names from my actual data table

item_names = [item["name"] for item in st.session_state.data_table]

# Restock section 
restock_item = st.selectbox(
  "Item name",
  item_names,
  index=None,
  placeholder="Choose the item",
)

restock_number = st.number_input(
    "Insert an amount", min_value= 1, placeholder="Type a number..."
)

# Restock section increasing stock

if st.button("Add Stock"):
    if restock_item is None:
      st.warning("Please choose an item first.")
    else:  
      for item in st.session_state.data_table:  
        if item["name"] == restock_item:
          item["current_stock"] += restock_number
          st.success(f"You have added {restock_number} {restock_item}")
          break

# Price section 
st.subheader("Change Price")
item_price_select = st.selectbox(
  "Item names",
  item_names,
  index=None,
  placeholder="Choose the item",
)

new_price = st.number_input(
    "Insert new price", min_value= 1, placeholder="Type a number..."
)

# Price section updating price
if st.button("Update Price"):
  for item in st.session_state.data_table:
    if item["name"] == item_price_select:
      item["price"] = new_price
      st.success(f"You have changed the price of {item_price_select} to {new_price}")

# New item section 

new_item = st.text_input("New item name", key="placeholder")
new_item_price = st.number_input("Price", min_value= 1, placeholder="Type a number...")
new_item_stock = st.number_input("Stock", min_value=0, step=1, key="placeholdder")

# Stock section adding new item
if st.button("Add item"):
  st.session_state.data_table.append({"name": new_item, "price": new_item_price, "initial_stock": new_item_stock, "current_stock": new_item_stock})
  st.success(f"You have added {new_item_stock} {new_item}")

if st.button("Restore Multicolored Pen"):
    st.session_state.data_table.insert(0, {
        "name": "🖊️Multicolored pen",
        "price": 10,
        "initial_stock": 10,
        "current_stock": 10
    })
    st.success("Restored Multicolored Pen at the top of the list")

item_to_delete = st.selectbox(
    "Delete an item",
    [item["name"] for item in st.session_state.data_table]
)

if st.button("Delete item"):
    st.session_state.data_table = [
        item for item in st.session_state.data_table
        if item["name"] != item_to_delete
    ]
    st.success(f"Deleted {item_to_delete}")
