import streamlit as st
from ui.header import show_header
from ui.home import show_home
from ui.produk import show_produk
from ui.seller import show_seller

st.set_page_config(
    page_title="EDIKS – Etalase Digital Klotok Simogirang",
    layout="wide"
)

show_header()

menu = st.sidebar.radio(
    "Menu",
    ["🏠 Beranda", "🛍 Produk", "👩‍🍳 Penjual"]
)

if menu == "🏠 Beranda":
    show_home()
elif menu == "🛍 Produk":
    show_produk()
elif menu == "👩‍🍳 Penjual":
    show_seller()
