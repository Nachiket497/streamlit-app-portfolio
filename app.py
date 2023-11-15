import streamlit as st
from PIL import Image
from support_fun import local_css
from intro import make_intro
from edu import make_edu
from exp import make_exp
from project import make_project
from contact import make_contact


st.set_page_config(page_title="Nachiket-Portfolio", page_icon="img/N.png", layout="wide" )
local_css("style/style.css")
    

with st.container():
    # code for nav bar
    pass

with st.container():
    make_intro()
    st.markdown("-----")

# with st.container():
#     make_edu()
#     st.markdown("-----")

with st.container():
    make_exp()
    st.markdown("-----")

with st.container():
    make_project()
    st.markdown("-----")
     
# ---- CONTACT ----
with st.container():
    make_contact()