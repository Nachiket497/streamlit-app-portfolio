import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Data Synchronization Via Firebase",  page_icon="img/N.png")


st.title("Data Synchronization Via Firebase")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/sm.jpg")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: July 2020 - Aug 2020")


st.markdown("")
st.markdown("### Description:")


st.markdown("  <li>Implemented synchronization of textual data between an android device and a python script on the  desktop PC using the Firebase Database in real-time.</li><li>Created a real-time database on the firebase console via browser. The application connects to the database on startup.</li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3>Code :</h3>",unsafe_allow_html=True )
st.markdown("<li><a href=https://github.com/Nachiket497/FirebaseAPK>Github</a></li>" ,unsafe_allow_html=True )
