import streamlit as st
import pandas as pd
from pathlib import Path
import importlib.util

# =====================================================
#  LOAD image_process.py SECARA LANGSUNG (ANTI ERROR)
# =====================================================
BASE_DIR = Path(__file__).resolve().parents[1]
IMAGE_PROCESS_PATH = BASE_DIR / "utils" / "image_process.py"

spec = importlib.util.spec_from_file_location(
    "image_process",
    IMAGE_PROCESS_PATH
)
image_process = importlib.util.module_from_spec(spec)
spec.loader.exec_module(image_process)

process_image = image_process.process_image
DATA_FILE = Path("data/produk.csv")
ASSET_DIR = Path("assets")

ASSET_DIR.mkdir(exist_ok=True)
DATA_FILE.parent.mkdir(exist_ok=True)

def show_seller():
    st.subheader("👩‍🍳 Input Produk Penjual")

    nama = st.text_input("Nama Produk")
    penjual = st.text_input("Nama Penjual")
    harga = st.number_input("Harga Dasar (Rp)", min_value=0)
    foto = st.file_uploader("Upload Foto Produk", type=["jpg", "png"])

    if st.button("Simpan Produk"):
        if not (nama and penjual and foto):
            st.warning("Lengkapi semua data.")
            return

        output_path = ASSET_DIR / f"{nama.replace(' ', '_')}.png"
        process_image(foto, nama, harga, output_path)

        data = {
            "nama_produk": nama,
            "harga": harga,
            "foto": str(output_path),
            "penjual": penjual
        }

        if DATA_FILE.exists():
            df = pd.read_csv(DATA_FILE)
            df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
        else:
            df = pd.DataFrame([data])

        df.to_csv(DATA_FILE, index=False)
        st.success("Produk berhasil ditambahkan ✅")
