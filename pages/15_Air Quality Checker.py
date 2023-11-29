import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Air Quality Checker",  page_icon="img/N.png")


st.title("Air Quality Checker")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/new.jpg")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: Aug 2020 - Nov 2020")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Established a circuit to read the data from the sensor MQ-135 and display it on an android app. </li> <li>The connection is developed between an android app and Arduino via ThingSpeak using Wi-Fi Module  ESP8266-01</li> <li> The application is capable of monitoring air quality in real time. </li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3> Code: </h3> <p>https://github.com/Nachiket497/IOT_Base_Air_Qulity_checker</p>",unsafe_allow_html=True )
