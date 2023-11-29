import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="PID Controller using Op-Amp",  page_icon="img/N.png", initial_sidebar_state="collapsed")


st.title("PID Controller using Op-Amp")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/Circuit_diagram.jpeg")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: April 2021")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Designed a PID control system using Op-Amp which regulate the voltage drop across the system.</li> <li>Implemented the controller in multisim12 and performed the transient analysis for the different set-points.</li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3> Code: </h3> <p>https://github.com/Nachiket497/PID_Controller_using_OP-Amp</p>",unsafe_allow_html=True )
