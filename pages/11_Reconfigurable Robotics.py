import streamlit as st
from app import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Reconfigurable Robotics",  page_icon="img/N.png", initial_sidebar_state="collapsed")


st.title("Reconfigurable Robotics")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/q2h1.gif")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: April 2021 - May 2021")


st.markdown("")
st.markdown("### Description:")


st.markdown("  <li>Designed a reconfigurable robotic system that transforms between serpentine, wheeled-quadrupedal, and humanoidal locomotion modes without any rearrangement.</li> <li>Developed transition gaits for reconfiguration between serpentine, wheeled-quadruped and biped.</li>  <li>Implemented geometric locomotion gaits of serpentine for linear progression, lateral undulation, rolling and rotation and walking gaits of wheeled quadruped for crawling and trotting. </li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("### Code: https://drive.google.com/file/d/1WklsGTju2-ZOsPBwW0gTP8u28iZbrFs0/view")
