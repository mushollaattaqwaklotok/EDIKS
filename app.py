# =====================================================
#  EDIKS
#  Etalase Digital Klotok Simogirang
#  Dikelola oleh Remaja Musholla At-Taqwa
# =====================================================

import streamlit as st
import pandas as pd
from pathlib import Path

# =====================================================
#  KONFIGURASI DASAR
# =====================================================
BASE_DIR = Path(".")
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"

DATA_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)

PENJUAL_FILE = DATA_DIR / "penjual.csv"
PRODUK_FILE = DATA_DIR / "produk.csv"

ADMIN_PASSWORD = "ediks123"  # bisa diganti

# =====================================================
#  FUNGSI UTILITAS
# =====================================================
def load_csv(file, columns):
    if file.exists():
        return pd.read_csv(file)
    else:
        return pd.DataFrame(columns=columns)

def save_csv(df, file):
    df.to_csv(file, index=False)

# =====================================================
#  LOAD DATA
# =====================================================
penjual_df = load_csv(
    PENJUAL_FILE,
    ["id", "nama", "dusun", "no_wa"]
)

produk_df = load_csv(
    PRODUK_FILE,
    ["id", "penjual_id", "nama_produk", "kategori", "harga", "deskripsi", "foto"]
)

# =====================================================
#  SET PAGE
# =====================================================
st.set_page_config(
    page_title="EDIKS – Etalase Digital Klotok Simogirang",
    page_icon="🛒",
    layout="wide"
)

# =====================================================
#  HEADER
# =====================================================
st.title("🛒 EDIKS")
st.subheader("Etalase Digital Klotok Simogirang")
st.caption(
    "Dari warga, oleh warga, untuk warga • "
    "Dikelola oleh Remaja Musholla At-Taqwa"
)

st.divider()

# =====================================================
#  MENU
# =====================================================
menu = st.sidebar.radio(
    "Menu",
    [
        "🏠 Beranda",
        "🍱 Produk",
        "🧑‍🍳 Penjual",
        "🔐 Admin"
    ]
)

# =====================================================
#  BERANDA
# =====================================================
if menu == "🏠 Beranda":
    st.markdown("""
    ### Selamat Datang 👋

    **EDIKS** adalah etalase digital sederhana untuk warga Dusun  
    **Klotok & Simogirang** yang berjualan makanan dan kebutuhan harian.

    🔹 Pesan langsung ke penjual via WhatsApp  
    🔹 Tidak ada biaya aplikasi  
    🔹 Mendukung UMKM rumahan desa  

    > Aplikasi ini dikelola secara mandiri  
    > oleh **Remaja Musholla At-Taqwa**
    """)

# =====================================================
#  PRODUK
# =====================================================
elif menu == "🍱 Produk":
    st.subheader("Daftar Produk Warga")

    kategori_list = ["Semua"] + sorted(
        produk_df["kategori"].dropna().unique().tolist()
    )

    kategori = st.selectbox("Pilih Kategori", kategori_list)

    if kategori != "Semua":
        data = produk_df[produk_df["kategori"] == kategori]
    else:
        data = produk_df

    if data.empty:
        st.info("Belum ada produk ditampilkan.")
    else:
        for _, row in data.iterrows():
            penjual = penjual_df[penjual_df["id"] == row["penjual_id"]]

            if penjual.empty:
                continue

            penjual = penjual.iloc[0]

            with st.container(border=True):
                st.markdown(f"### {row['nama_produk']}")
                st.write(row["deskripsi"])
                st.write(f"💰 Harga: Rp {int(row['harga']):,}")
                st.write(f"👩‍🍳 Penjual: {penjual['nama']} ({penjual['dusun']})")

                pesan = f"Saya ingin pesan {row['nama_produk']}"
                wa_link = f"https://wa.me/{penjual['no_wa']}?text={pesan.replace(' ', '%20')}"
                st.link_button("📲 Pesan via WhatsApp", wa_link)

# =====================================================
#  PENJUAL
# =====================================================
elif menu == "🧑‍🍳 Penjual":
    st.subheader("Daftar Penjual")

    if penjual_df.empty:
        st.info("Belum ada penjual terdaftar.")
    else:
        for _, row in penjual_df.iterrows():
            with st.container(border=True):
                st.markdown(f"### {row['nama']}")
                st.write(f"📍 Dusun: {row['dusun']}")
                st.write(f"📞 WhatsApp: {row['no_wa']}")

# =====================================================
#  ADMIN
# =====================================================
elif menu == "🔐 Admin":
    st.subheader("Admin EDIKS")

    password = st.text_input("Password Admin", type="password")

    if password == ADMIN_PASSWORD:
        tab1, tab2 = st.tabs(["➕ Penjual", "➕ Produk"])

        # ---------------- PENJUAL ----------------
        with tab1:
            st.markdown("### Tambah Penjual")
            nama = st.text_input("Nama Penjual")
            dusun = st.text_input("Dusun")
            wa = st.text_input("No WhatsApp (628xxxx)")

            if st.button("Simpan Penjual"):
                if nama and dusun and wa:
                    new_id = 1 if penjual_df.empty else penjual_df["id"].max() + 1
                    penjual_df.loc[len(penjual_df)] = [new_id, nama, dusun, wa]
                    save_csv(penjual_df, PENJUAL_FILE)
                    st.success("Penjual berhasil ditambahkan")
                else:
                    st.warning("Lengkapi semua data")

        # ---------------- PRODUK ----------------
        with tab2:
            st.markdown("### Tambah Produk")

            if penjual_df.empty:
                st.warning("Tambahkan penjual terlebih dahulu")
            else:
                penjual_id = st.selectbox(
                    "Penjual",
                    penjual_df["id"],
                    format_func=lambda x: penjual_df.loc[
                        penjual_df["id"] == x, "nama"
                    ].values[0]
                )

                nama_produk = st.text_input("Nama Produk")
                kategori = st.selectbox(
                    "Kategori",
                    ["Snack", "Kue", "Nasi", "Sayur", "Minuman", "Lainnya"]
                )
                harga = st.number_input("Harga", min_value=0, step=500)
                deskripsi = st.text_area("Deskripsi Produk")

                if st.button("Simpan Produk"):
                    if nama_produk and harga > 0:
                        new_id = 1 if produk_df.empty else produk_df["id"].max() + 1
                        produk_df.loc[len(produk_df)] = [
                            new_id,
                            penjual_id,
                            nama_produk,
                            kategori,
                            harga,
                            deskripsi,
                            ""
                        ]
                        save_csv(produk_df, PRODUK_FILE)
                        st.success("Produk berhasil ditambahkan")
                    else:
                        st.warning("Nama dan harga wajib diisi")

    else:
        st.info("Akses admin hanya untuk pengelola")
