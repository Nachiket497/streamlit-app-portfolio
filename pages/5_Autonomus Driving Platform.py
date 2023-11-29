import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Autonomus Driving Platform",  page_icon="img/N.png", initial_sidebar_state="collapsed")


st.title("Autonomus Driving Platform")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/adp.gif")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: Sep 2022")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Designed a platform for autonomous driving using ROS and Gazebo.</li><li>Implemented the colour detection and following using OpenCV.</li><li>Developed a PID controller for steering and speed control of the vehicle.</li>", unsafe_allow_html=True)
st.markdown("")


