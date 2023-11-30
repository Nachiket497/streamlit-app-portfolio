import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Enquiry Registration App",  page_icon="img/N.png")


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


st.markdown(" <li>Developed an Android application for efficient customer enquiry registration, streamlining the process and enhancing user experience.</li> <li>Implemented backend using Firebase Realtime Database, ensuring secure and real-time storage of customer enquiry data.</li><li>Created a dedicated client-side application for administrators, providing a user-friendly interface to view and manage customer enquiries.</li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3>Code :</h3>",unsafe_allow_html=True )
st.markdown("<li><a href=https://github.com/Nachiket497/Enquiry-App>Github</a></li>" ,unsafe_allow_html=True )
