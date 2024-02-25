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


st.markdown(" <li>Conducted thorough verification of the link layer & Arbmux in 68 Byte mode for Compute Express Link (CXL), ensuring robust functionality and adherence to specifications.</li><li> Implemented 256b Byte mode CXL Arbmux, featuring a bespoke Weighted Round Robin algorithm for efficient arbitation. Also implemented L0p ALMP negotiation feature.</li><li>Currently engaged in the validation of the Physical Layer for PCIe 6.0, focusing on the Link Training and Status State Machine (LTSSM) & MAC using Avery VIP as well as a custom UVM Testbench.</li><li>Dveloped versatile UVM Testbenchs capable of generating stimuli as APB master and APB slave as per APB5 protocol</li>", unsafe_allow_html=True)
st.markdown("")


