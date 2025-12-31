import streamlit as st
import pandas as pd
from pathlib import Path

DATA_FILE = Path("data/produk.csv")

def show_produk():
    st.subheader("🛍 Daftar Produk Warga")

    if not DATA_FILE.exists():
        st.warning("Belum ada data produk.")
        return

    df = pd.read_csv(DATA_FILE)

    if df.empty:
        st.info("Produk masih kosong.")
        return

    cols = st.columns(3)

    for i, row in df.iterrows():
        with cols[i % 3]:
            if row["foto"]:
                st.image(row["foto"], use_column_width=True)
            st.markdown(f"**{row['nama_produk']}**")
            st.markdown(f"💰 Rp {row['harga']:,}")
            st.caption(f"Penjual: {row['penjual']}")
