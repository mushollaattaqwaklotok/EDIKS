import streamlit as st

# ================================
# IMPORT UI MODULE
# ================================
from ui.header import show_header
from ui.home import show_home
from ui.products import show_products
from ui.seller import show_seller

# ================================
# KONFIGURASI HALAMAN
# ================================
st.set_page_config(
    page_title="EDIKS – Etalase Digital Klotok Simogirang",
    page_icon="🛍",
    layout="wide"
)

# ================================
# HEADER
# ================================
show_header()

# ================================
# SIDEBAR MENU
# ================================
st.sidebar.title("📌 Menu EDIKS")

menu = st.sidebar.radio(
    "",
    [
        "🏠 Beranda",
        "🛍 Produk",
        "👩‍🍳 Penjual"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "Dikelola oleh **Remaja Musholla At-Taqwa**\n\n"
    "Dusun Klotok – Simogirang"
)

# ================================
# ROUTING HALAMAN
# ================================
if menu == "🏠 Beranda":
    show_home()

elif menu == "🛍 Produk":
    show_products()

elif menu == "👩‍🍳 Penjual":
    show_seller()
