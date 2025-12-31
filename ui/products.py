import streamlit as st
import pandas as pd
import os

DATA_PATH = "data/products.csv"

def load_products():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    return pd.DataFrame(columns=[
        "nama_produk",
        "harga",
        "stok",
        "status"
    ])

def save_products(df):
    os.makedirs("data", exist_ok=True)
    df.to_csv(DATA_PATH, index=False)

def show_products():
    st.subheader("📦 Produk UMKM")

    df = load_products()

    # =========================
    # FORM TAMBAH PRODUK
    # =========================
    with st.expander("➕ Tambah Produk Baru"):
        with st.form("form_produk"):
            nama = st.text_input("Nama Produk")
            harga = st.number_input("Harga", min_value=0, step=1000)
            stok = st.number_input("Stok", min_value=0, step=1)
            status = st.selectbox("Status", ["Aktif", "Habis"])

            simpan = st.form_submit_button("💾 Simpan Produk")

        if simpan:
            if nama.strip() == "":
                st.warning("Nama produk tidak boleh kosong")
            else:
                new_data = {
                    "nama_produk": nama,
                    "harga": harga,
                    "stok": stok,
                    "status": status
                }
                df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                save_products(df)
                st.success("Produk berhasil ditambahkan")
                st.rerun()

    # =========================
    # TAMPILKAN DATA
    # =========================
    if df.empty:
        st.info("Belum ada produk")
    else:
        st.dataframe(df, use_container_width=True)
