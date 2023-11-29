import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Autonomous Fertiliser bot",  page_icon="img/N.png")


st.title("Autonomous Fertiliser bot")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/image1.gif")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: Aug 2022 - Dec 2022")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Designed  ground robot with a rocker bogie mechanism to optimize fertilizer application, reducing waste by delivering nutrients directly to plant roots.</li><li>Developed small-scale farming, the compact and lightweight design ensures seamless navigation through tight spaces, offering an efficient and cost-effective solution for fertilization process.</li><li>Implemented a plantation layout following algorithum using OpenCV.</li> <li> Published research paper titled 'Design and Implementation of an Autonomous Plantation Layout Follower Fertilizer Bot for Advanced Farming' at the PCEMS Conference.  </li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3>Code :</h3>",unsafe_allow_html=True )
st.markdown("<li><a href=https://github.com/Nachiket497/AFB_code>Github</a></li>" ,unsafe_allow_html=True )
st.markdown("<li><a href=https://ieeexplore.ieee.org/document/10136100>IEEE Paper</a></li>",unsafe_allow_html=True )
