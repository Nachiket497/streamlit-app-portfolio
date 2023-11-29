import streamlit as st
from app import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Cruise Controller",  page_icon="img/N.png")


st.title("Cruise Controller")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/task2_without_slope.jpeg")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: July 2020 - Aug 2020")


st.markdown("")
st.markdown("### Description:")


st.markdown("  <li>Designed a cruise controller for a planar mobile robot to achieve the desired velocity based on PID control law in MATLAB.</li> <li> Extended the controller to adapt to changes in the terrain slope, friction, and setpoint changes in the desired velocity.</li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3> Code: </h3> <p>https://github.com/Nachiket497/CRUISE-CONTROLLER</p>",unsafe_allow_html=True )
