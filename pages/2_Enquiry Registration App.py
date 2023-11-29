import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Enquiry Registration App",  page_icon="img/N.png", initial_sidebar_state="collapsed")


st.title("Enquiry Registration App")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/Enquiry.png")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: May 2023")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Developed an android application for the enquiry registration of the customors.</li> <li>Implemented the application using the Firebase Realtime Database for storing the data.</li><li>ALso developed a client side application for the admin to view and manage the enquiries.</li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3> Code: </h3> <p>https://github.com/Nachiket497/Enquiry-App</p>",unsafe_allow_html=True )
