import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Quadrupilot",  page_icon="img/N.png")


st.title("Quadrupilot")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/vecros.jpg")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: Dec 2021 - Feb 2022")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Added the remote control and developed a successful communication between the Pixhawk and actuators via Mission Planner using the CAN-Bus protocol.</li>  <li>Implemented the trot, crawl-walking gait using semi-elliptical trajectory and inverser kinematics for a single quadruped leg on hardware.</li> ", unsafe_allow_html=True)
st.markdown("")


