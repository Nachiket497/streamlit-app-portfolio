import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="UVM_TB_GEN_Python",  page_icon="img/N.png")


st.title("UVM_TB_GEN_Python")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/uvm.png")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: Jan 2024")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Developed a Python script to automate the generation of a compile-free Universal Verification Methodology (UVM) based testbench, streamlining the setup process for complex digital designs.</li><li>Automated generation of the DUT environment (dut_env), encompassing the declaration of all requisite agents for the DUT.</li><li>Dynamic creation of agent files, seamlessly integrating components such as driver, monitor, and sequencer for each agent.</li><li>Generated base_test, interfaces and top file for integration of dut with interfaces.</li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3>Code :</h3>",unsafe_allow_html=True )
st.markdown("<li><a href=https://github.com/Nachiket497/uvm_tb_gen_python>Github</a></li>" ,unsafe_allow_html=True )
