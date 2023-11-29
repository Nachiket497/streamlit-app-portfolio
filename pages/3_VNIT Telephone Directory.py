import streamlit as st
from app import screen_width
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


st.markdown(" <li>Developed an android application to find extention number of the faculty and staff of VNIT.</li> <li>Implemented relaltime connection between excel sheet, firebase database and android application.</li><li>Designed various feactures like optimise search by name, quick call etc.</li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3> Code: </h3> <p>https://github.com/IDS-VNIT/vnit_telephone_app</p>",unsafe_allow_html=True )
