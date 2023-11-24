import streamlit as st
from app import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Trajectory generation for bipedal walking",  page_icon="img/N.png", initial_sidebar_state="collapsed")


st.title("Trajectory generation for bipedal walking")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/Multistep_3D.gif")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: June 2021 - July 2021")


st.markdown("")
st.markdown("### Description:")


st.markdown(" T<li>Implemented a 3D linear inverted pendulum model for bipedal walking and generated trajectories for the centre of mass and swing foot. </li> <li>Developed a time sequence of states given a constant COM height trajectory for locomotion.</li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3> Code: </h3> <p>https://github.com/Nachiket497/biped_walking</p>",unsafe_allow_html=True )
