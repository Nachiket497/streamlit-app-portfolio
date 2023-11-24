import streamlit as st
from PIL import Image
from support_fun import local_css
from intro import make_intro
from edu import make_edu
from exp import make_exp
from project import make_project
from contact import make_contact
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="Nachiket-Portfolio", page_icon="img/N.png", layout="wide", initial_sidebar_state="collapsed" )
local_css("style/style.css")

st.markdown("""<script type="text/javascript">
    window.onbeforeunload = function() {
        return "Dude, are you sure you want to leave? Think of the kittens!";
    }
</script>""", unsafe_allow_html=True)




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

screen_width = streamlit_js_eval(js_expressions='window.innerWidth',want_output = True, key = 'SCR')

if screen_width is None:
    screen_width = 1100
    print("screen_width is None")


with st.container():
    make_project(screen_width)
    st.markdown("-----")
     
# ---- CONTACT ----
with st.container():
    make_contact()