import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Quadruped",  page_icon="img/N.png")


st.title("Quadruped")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/quadurped.gif")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: July 2022 - Aug 2022")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Designed a 12-DOF quadruped robot utilizing Dynamixel actuators and Jetson.</li> <li>Implemented the trot, crawl-walking gait using semi-elliptical trajectory and inverser kinematics for a single quadruped leg on hardware using ROS.</li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3>Code :</h3>",unsafe_allow_html=True )
st.markdown("<li><a href=https://github.com/IvLabs/Quadruped_Robotics>Github</a></li>" ,unsafe_allow_html=True )
