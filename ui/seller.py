import streamlit as st
import pandas as pd
from pathlib import Path
import importlib.util

# =====================================================
#  LOAD utils/image_process.py SECARA LANGSUNG
#  (ANTI ModuleNotFoundError STREAMLIT CLOUD)
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

# =====================================================
#  PATH DATA
# =====================================================
DATA_FILE = BASE_DIR / "data" / "produk.csv"
ASSET_DIR = BASE_DIR / "assets"

ASSET_DIR.mkdir(exist_ok=True)
DATA_FILE.parent.mkdir(exist_ok=True)

# =====================================================
#  UI INPUT PENJUAL
# =====================================================
def show_seller():
    st.subheader("👩‍🍳 Input Produk Penjual")
    st.caption("Cukup upload foto dan isi harga, sistem akan menampilkan otomatis")

    nama = st.text_input("Nama Produk")
    penjual = st.text_input("Nama Penjual")
    harga = st.number_input(
        "Harga Dasar (Rp)",
        min_value=0,
        step=500
    )
    foto = st.file_uploader(
        "Upload Foto Produk",
        type=["jpg", "jpeg", "png"]
    )

    if st.button("💾 Simpan Produk"):
        if not nama or not penjual or not foto:
            st.warning("⚠️ Nama produk, penjual, dan foto wajib diisi.")
            return

        # nama file aman
        nama_file = nama.lower().replace(" ", "_")
        output_path = ASSET_DIR / f"{nama_file}.png"

        # proses gambar (gabung foto + harga)
        process_image(foto, nama, harga, output_path)

        data_baru = {
            "nama_produk": nama,
            "harga": harga,
            "foto": str(output_path),
            "penjual": penjual
        }

        if DATA_FILE.exists():
            df = pd.read_csv(DATA_FILE)
            df = pd.concat(
                [df, pd.DataFrame([data_baru])],
                ignore_index=True
            )
        else:
            df = pd.DataFrame([data_baru])

        df.to_csv(DATA_FILE, index=False)

        st.success("✅ Produk berhasil disimpan dan siap tampil di etalase!")
        st.image(output_path, caption=nama, width=300)
