import streamlit as st
import pandas as pd
from pathlib import Path

DATA_FILE = Path("data/products.csv")


def show_home():
    st.title("🛒 Etalase UMKM Warga")
    st.caption("Produk rumahan warga Klotok – Simogirang")

    if not DATA_FILE.exists():
        st.info("Produk belum tersedia")
        return

    df = pd.read_csv(DATA_FILE)

    cols = st.columns(3)
    for i, row in df.iterrows():
        with cols[i % 3]:
            st.image(row["foto"], use_column_width=True)
            st.markdown(f"**{row['nama']}**")
            st.write(f"Rp {int(row['harga']):,}")
            st.caption(row["penjual"])
