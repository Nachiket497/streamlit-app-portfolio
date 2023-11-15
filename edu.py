import streamlit as st


def make_edu():

    col1, col2 = st.columns([5, 8 ])

    with col1 :
        # make Education as heading of 60px in center of col1
        st.markdown("")
        st.markdown("<h1 class='f60' style='text-align: center;'>Education</h1>", unsafe_allow_html=True)


    with col2 :
        st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)

        st.markdown("<div style='line-height: normal'> <p class=f30 >Visvesvaraya National institute of Technology Nagpur (VNIT)</p> <p class=f18 >Bachelor of Technology in Electronics and Communication Engineering</p></div>", unsafe_allow_html=True)
        st.markdown("<p class=f18 ><i class='fa fa-calendar' style='font-size:24px'></i> June 2019 - May 2023 </br>CGPA : 9.18/10 </p>", unsafe_allow_html=True)

            