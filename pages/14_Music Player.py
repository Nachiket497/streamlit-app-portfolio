import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Music Player",  page_icon="img/N.png")


st.title("Music Player")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/mus.jpg")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: Aug 2020 - Nov 2020")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Designed a simple music player using android studio with basic features <ul> <li>Full list of all songs in the device.</li> <li>Separate player for playing the songs with cover photo and other details.</li> <li>Interactive notification widgets and works in the background. </li> </ul> </li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3>Code :</h3>",unsafe_allow_html=True )
st.markdown("<li><a href=https://github.com/Nachiket497/Music_Player>Github</a></li>" ,unsafe_allow_html=True )
