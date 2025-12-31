import streamlit as st
import json
import os

DATA_PATH = "data/umkm_profile.json"

def load_profile():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "nama_toko": "",
        "pemilik": "",
        "wa": "",
        "alamat": ""
    }

def save_profile(data):
    os.makedirs("data", exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def show_umkm_profile():
    st.subheader("🏪 Profil UMKM")

    profile = load_profile()

    with st.form("form_umkm"):
        nama_toko = st.text_input("Nama Toko", profile["nama_toko"])
        pemilik = st.text_input("Nama Pemilik", profile["pemilik"])
        wa = st.text_input("Nomor WhatsApp", profile["wa"])
        alamat = st.text_area("Alamat", profile["alamat"])

        simpan = st.form_submit_button("💾 Simpan Profil")

    if simpan:
        save_profile({
            "nama_toko": nama_toko,
            "pemilik": pemilik,
            "wa": wa,
            "alamat": alamat
        })
        st.success("Profil UMKM berhasil disimpan")
