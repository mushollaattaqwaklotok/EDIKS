import streamlit as st

def show_header():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("assets/logo_ediks.png", width=90)
    with col2:
        st.markdown("## **EDIKS**")
        st.markdown(
            "Etalase Digital Klotok Simogirang  \n"
            "*Dikelola oleh Remaja Musholla At-Taqwa*"
        )
    st.divider()
