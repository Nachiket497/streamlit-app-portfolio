import streamlit as st
from support_fun import img_to_bytes

st.set_page_config(page_title="Plotting Demo", page_icon="📈", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #b9bec7;
    }
    
</style>
""", unsafe_allow_html=True)


st.markdown("# Plotting Demo")

st.markdown("")
# add a image here
st.image("img/bg.jpg", width=100, use_column_width=False)





