import streamlit as st
from pathlib import Path

def show_header():
    col1, col2 = st.columns([1, 5])

    logo_path = Path("assets/logo_ediks.png")

    with col1:
        if logo_path.exists():
            st.image(str(logo_path), width=90)
        else:
            st.markdown("### 🛒")

    with col2:
        st.markdown("## **EDIKS**")
        st.markdown(
            "Etalase Digital Klotok Simogirang  \n"
            "*Dikelola oleh Remaja Musholla At-Taqwa*"
        )

    st.divider()
