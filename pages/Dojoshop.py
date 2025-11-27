import streamlit as st
from pages.read_dojoshop import load_items, load_purchase_log
from pages.save_dojoshop import save_items, append_purchase
from datetime import datetime
import base64

# Function for embedding images inside HTML
def get_base64_image(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

logo_base64 = get_base64_image("fsb_logo.jpg")

# Inject custom CSS to center everything
st.markdown("""
<style>
.header-banner {
    width: 100%;
    text-align: center;
    margin-bottom: 25px;
}

.header-inner {
    display: inline-flex;
    align-items: center;
    gap: 20px;
    background-color: #0e1117;
    padding: 15px 30px;
    border-radius: 12px;
    box-shadow: 0 0 12px rgba(0,0,0,0.4);
}

.header-logo {
    border-radius: 8px;
}

.header-title {
    font-size: 38px;
    margin: 0;
    padding: 0;
    font-weight: 600;
}

.header-subtitle {
    margin: 4px 0 0 0;
    font-size: 16px;
    color: #cccccc;
}
</style>
""", unsafe_allow_html=True)

# HTML Banner
st.markdown(
    f"""
    <div class="header-banner">
        <div class="header-inner">
            <img src="data:image/jpg;base64,{logo_base64}" width="120" class="header-logo">
            <div>
                <h1 class="header-title">🛒 Dojo Shop Tracker</h1>
                <p class="header-subtitle">Record student purchases, track stock, and keep the Dojo Shop organised.</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")



col1, col2 = st.columns([2, 3])

#if data_table is not in the sesion state which it isn't the first time the program runs, the block will run and load
#the CSV 'load_items

if "data_table" not in st.session_state:
    st.session_state.data_table = load_items()

#loops through data_table (the items csv) and looks for the key 'name' then stores that 'name' back into the variable item_names

item_names = [item["name"] for item in st.session_state.data_table]

#checks to see if the purchase log is not in the session state, first time it runs it wont be, so the block runs and an empty
#dictionary is made

if "purchase_log" not in st.session_state:
    st.session_state.purchase_log = []

#splits the shop into a column
with col1:
    st.markdown("### ✏️ Record a purchase")

    #variable names, selection boxes 
    option_year = st.selectbox(
        "Year group",
        ("Year 3", "Year 4", "Year 5", "Year 6"),
        index=None,
        placeholder="Choose your year group",
    )

    option_item = st.selectbox(
        "Item name",
        item_names,
        index=None,
        placeholder="Choose the item",
    )

    #allows the user to insert a number has a preset min value
    number = st.number_input(
        "Insert an amount", min_value=1, placeholder="Type a number..."
    )

    #if the user presses the button the block runs, it loops through the data table and stores data inside the 'item' variable, 
    #checks if the option_item (slime as an example) matches the slime(name), then replaces current stock with initial stock
    #if number the user enters (3) is greater than initial_stock (2) prints there isn't enough and breaks out the loop
    #If that is false it does the math, initial - number, store inside current stock var 
    # If current_stock is 4, it replaces the value of current_stock with 4

    if st.button("Record purchase"):
        for item in st.session_state.data_table:
            if item["name"] == option_item:
                initial_stock = item["current_stock"]
                if number > initial_stock:
                    st.error("There is not enough stock for that purchase.")
                    break

                current_stock = initial_stock - number
                item["current_stock"] = current_stock

                purchase = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "year_group": option_year,
                    "item_name": option_item,
                    "quantity": number,
                    "price": item["price"],
                    "total_cost": number * item["price"],
                }

                #nice green button 
                st.success(f"You recorded {option_year} buying {number} x {option_item}")

                #appends this purchase to the purchase log csv
                st.session_state.purchase_log.append(purchase)
                append_purchase(purchase)
                save_items(st.session_state.data_table) #saves
                break


with col2:
    st.markdown("### 📦 Shop overview")

    # Little summary line
    total_items = len(st.session_state.data_table)
    low_stock = sum(1 for item in st.session_state.data_table if item["current_stock"] <= 3)

    st.markdown(
        f"<p style='color:#dddddd;'>Items in shop: <b>{total_items}</b> &nbsp; | &nbsp; Low stock (3 or less): <b>{low_stock}</b></p>",
        unsafe_allow_html=True,
    )

    # Nicer table
    import pandas as pd
    df = pd.DataFrame(st.session_state.data_table)

    # Reorder / rename columns a bit
    df = df[["name", "price", "current_stock", "initial_stock"]]
    df = df.rename(
        columns={
            "name": "Item",
            "price": "Price (dojo)",
            "current_stock": "In stock",
            "initial_stock": "Initial stock",
        }
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=400,
    )





