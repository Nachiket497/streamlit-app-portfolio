import streamlit as st
from app import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="CommonRoad",  page_icon="img/N.png")


st.title("CommonRoad")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/common.gif")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: May 2022 - July 2022")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Implemented a futurifier for the linear temporal logic(LTL) by using rtamt python liberary and tested with the help of NuSMV Tester.</li>   <li>Generated random LTL models and LTL specifications from the tree to verify the results of the futurifier using NuSMV.</li> <li>Visualized and implemented the single-trailer truck model in CommonRoad-io liberary.</li>", unsafe_allow_html=True)
st.markdown("")


