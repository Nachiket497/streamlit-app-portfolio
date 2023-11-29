import streamlit as st
from home import screen_width
from support_fun import local_css
from support_fun import img_to_bytes


st.set_page_config(page_title="Trajectory Optimization of Cart Pole",  page_icon="img/N.png")


st.title("Trajectory Optimization of Cart Pole")


local_css("style/project_style.css")


st.markdown("")
st.markdown(f"""
    <p align="center">
    <img  width="{int(screen_width/2.5)}" src='data:image/png;base64,
{img_to_bytes("img/optimize1.gif")}'>
    </p>""", unsafe_allow_html=True)


st.markdown("")
st.markdown("### Duration: May 2021 - June 2021")


st.markdown("")
st.markdown("### Description:")


st.markdown(" <li>Generated an optimal swing-up trajectory for a cart-pole system with minimum energy objective and boundary constraints in state and time.</li> <li>Obtained the solution of optimization problem using CasADi Toolbox and simulated the generated trajectories using Matplotlib.</li>", unsafe_allow_html=True)
st.markdown("")


st.markdown("<h3>Code :</h3>",unsafe_allow_html=True )
st.markdown("<li><a href=https://github.com/Nachiket497/trajectory_optimization>Github</a></li>" ,unsafe_allow_html=True )
