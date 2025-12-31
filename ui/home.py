import streamlit as st
import pandas as pd
from pathlib import Path
import urllib.parse

DATA_FILE = Path("data/products.csv")
ADMIN_WA = "6281234567890"  # ganti nomor ini


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

            st.markdown(f"### {row['nama']}")
            st.write(f"💰 **Rp {int(row['harga']):,}**")
            st.caption(f"👩‍🍳 {row['penjual']}")

            pesan = f"Assalamu’alaikum, saya mau pesan {row['nama']}."
            pesan_encoded = urllib.parse.quote(pesan)

            wa_link = f"https://wa.me/{ADMIN_WA}?text={pesan_encoded}"

            st.markdown(
                f"""
                <a href="{wa_link}" target="_blank">
                    <button style="
                        background-color:#25D366;
                        color:white;
                        border:none;
                        padding:8px 12px;
                        border-radius:6px;
                        cursor:pointer;
                        width:100%;
                        font-size:14px;
                    ">
                        📲 Pesan via WhatsApp
                    </button>
                </a>
                """,
                unsafe_allow_html=True
            )
