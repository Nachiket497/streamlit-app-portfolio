import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Manipulation of Robotic Arm",  page_icon="img/N.png", initial_sidebar_state="collapsed")


st.title("Manipulation of Robotic Arm")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/pick_place1.gif")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: Nov 2020 - April 2021")


st.markdown("")
st.markdown("### Description:")


st.markdown("  <li>Implemented the forward dynamics, forward kinematics, inverse kinematics and position control of serial link manipulators.</li><li>Accomplished an end effector trajectory control for a ‘straight line follower' task using inverse kinematics based on Newton-Raphson method.</li> <li> Developed an algorithm for 'Pick & Place' task for UR5 manipulator using PyBullet. </li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3> Code: </h3> <p>https://github.com/IvLabs/manipulation</p>",unsafe_allow_html=True )
