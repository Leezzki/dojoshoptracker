import streamlit as st
from pages.read_dojoshop import load_items
from pages.save_dojoshop import save_items

st.set_page_config(
    page_title="Dojo Shop Tracker",
    page_icon="🛒",
    layout="wide",
)


data_table = load_items()
save_items(data_table)


admin_view = st.Page(
   page="pages/Adminview.py",  # Path relative to app.py
   title="Admin view",
)

dojo_page = st.Page(
    page="pages/Dojoshop.py",  # Path relative to app.py
    title="Dojo Shop",
)

pg = st.navigation(pages=[dojo_page, admin_view])
pg.run()
    