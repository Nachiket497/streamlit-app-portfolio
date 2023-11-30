import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="CXL-PCIe Controller Verification",  page_icon="img/N.png")


st.title("CXL-PCIe Controller Verification")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/cxl.png")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: Feb 2023 - Present")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Performed verification of the 68B mode CXL Link layer and Arb Mux layer, ensuring protocol compliance and functionality.</li><li>Designed 256B mode CXL Arb Mux with a weightage round-robin module and L0p support.</li><li>Currently working on verification of the LTSSM in the PHY layer of PCIe controller.</li>", unsafe_allow_html=True)
st.markdown("")


