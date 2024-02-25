import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="VNIT Telephone Directory",  page_icon="img/N.png")


st.title("VNIT Telephone Directory")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/VTD.jpeg")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: Dec 2022")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Developed a Android application for retrieving extension numbers of faculty and staff at VNIT.</li><li> Implemented features such as optimized search by name and quick call functionality for enhanced user accessibility.</li> <li>Implemented a seamless real-time connection between Excel sheets, Firebase database, and the Android application, ensuring up-to-date and synchronized information for a reliable and dynamic user experience.</li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3>Code :</h3>",unsafe_allow_html=True )
st.markdown("<li><a href=https://github.com/IDS-VNIT/vnit_telephone_app>Github</a></li>" ,unsafe_allow_html=True )
