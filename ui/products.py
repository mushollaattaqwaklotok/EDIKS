import streamlit as st
import pandas as pd
from pathlib import Path

DATA_FILE = Path("data/products.csv")


def show_products():
    st.title("🛍 Produk UMKM")

    if not DATA_FILE.exists():
        st.info("Belum ada produk")
        return

    df = pd.read_csv(DATA_FILE)

    for i, row in df.iterrows():
        with st.container(border=True):
            col1, col2 = st.columns([1, 3])

            with col1:
                st.image(row["foto"], use_column_width=True)

            with col2:
                st.subheader(row["nama"])
                st.write(f"👩‍🍳 {row['penjual']}")
                st.write(f"💰 Rp {int(row['harga']):,}")

                if st.button("🗑 Hapus", key=f"hapus_{i}"):
                    df.drop(i, inplace=True)
                    df.to_csv(DATA_FILE, index=False)
                    st.experimental_rerun()
