import sys
from pathlib import Path

# =====================================================
#  FIX PATH AGAR UI & UTILS TERBACA
# =====================================================
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# =====================================================
#  IMPORT
# =====================================================
import streamlit as st
from ui.header import show_header
from ui.home import show_home
from ui.produk import show_produk
from ui.seller import show_seller

# =====================================================
#  KONFIGURASI HALAMAN
# =====================================================
st.set_page_config(
    page_title="EDIKS – Etalase Digital Klotok Simogirang",
    layout="wide"
)

# =====================================================
#  HEADER
# =====================================================
show_header()

# =====================================================
#  MENU
# =====================================================
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
