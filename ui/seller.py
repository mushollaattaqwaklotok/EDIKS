import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

DATA_DIR = Path("data")
IMG_DIR = Path("assets/products")
DATA_DIR.mkdir(exist_ok=True)
IMG_DIR.mkdir(parents=True, exist_ok=True)

DATA_FILE = DATA_DIR / "products.csv"


def show_seller():
    st.title("👩‍🍳 Upload Produk UMKM")
    st.write("Unggah produk UMKM warga Klotok – Simogirang")

    with st.form("form_produk"):
        nama = st.text_input("Nama Produk")
        harga = st.number_input("Harga (Rp)", min_value=0, step=500)
        penjual = st.text_input("Nama Penjual")
        foto = st.file_uploader("Foto Produk", type=["png", "jpg", "jpeg"])

        submit = st.form_submit_button("💾 Simpan Produk")

    if submit:
        if not nama or not penjual or foto is None:
            st.warning("⚠️ Lengkapi semua data")
            return

        # simpan foto
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{foto.name}"
        img_path = IMG_DIR / filename
        with open(img_path, "wb") as f:
            f.write(foto.getbuffer())

        # simpan data
        data_baru = {
            "nama": nama,
            "harga": harga,
            "penjual": penjual,
            "foto": str(img_path)
        }

        if DATA_FILE.exists():
            df = pd.read_csv(DATA_FILE)
            df = pd.concat([df, pd.DataFrame([data_baru])], ignore_index=True)
        else:
            df = pd.DataFrame([data_baru])

        df.to_csv(DATA_FILE, index=False)
        st.success("✅ Produk berhasil disimpan")
