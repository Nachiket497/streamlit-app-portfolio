import streamlit as st
from support_fun import load_text

def make_intro():
    col1, col2 = st.columns([8,5])
    component_contact = load_text('contact.html')
    with col1:
        st.markdown("<h1 class='f60'>Nachiket Sawwalakhe</h1>", unsafe_allow_html=True)
        st.markdown("<p class='f30'>ASIC Verification Engineer At Ceremorphic</p>", unsafe_allow_html=True)

        st.markdown("""<p class='f18 pad-right'> Hey there! I'm a graduate of batch 2023 from Visvesvaraya National Institute of Technology Nagpur <a href="https://vnit.ac.in/">(VNIT)</a>  with a degree in Electronics and Communication Engineering and a CGPA of 9.18/10. My academic journey has been all about dedication and staying motivated. I love diving into solo and collaborative projects, always on the lookout for chances to grow. </p> """, unsafe_allow_html=True)

        st.markdown(""" <p class='f18 pad-right'> Being a core member of IvLabs, the robotics and AI community at VNIT, has been an exciting ride. I've been deep into researching algorithms for robot manipulation and locomotion in complex environments. Now, with a solid foundation I am eager to apply these skills to real-world challenges in the dynamic fields of electronics and robotics. </p>""", unsafe_allow_html=True)


        st.markdown(""" <p class='f18 pad-right'> Join me on this journey of turning ideas into action and tackling the cool stuff in electronics and robotics! </p> """, unsafe_allow_html=True)

        st.components.v1.html(component_contact, height=50)

    with col2:
        st.markdown("")
        st.markdown("")
        st.image("img/self.jpeg", width=1, use_column_width=True)

        


