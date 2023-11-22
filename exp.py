import streamlit as st
from support_fun import *

def make_exp():

    col1, col11, col2 = st.columns([5, 1, 8 ])

    with col1 :
        # make Education as heading of 60px in center of col1
        st.markdown("")
        st.markdown("<h1 class='f60' style='text-align: left;'>Experience</h1>", unsafe_allow_html=True)

    with col11 :
        pass

    with col2 :

        # read from job dict and write cards here
        for key in job_dict.keys():
            st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)
            st.markdown( '<div class=job-des > <p class=job style="font-size: 30px; line-height: 1.2;  " >{}  @ {} </br> </p> <p class="f18" >       <i class="fa fa-calendar" style="font-size:18px"></i> {} </p> </div>'.format( job_dict[key]["Job_title"], job_dict[key]["Job_place"], job_dict[key]["Job_date"]), unsafe_allow_html=True )


