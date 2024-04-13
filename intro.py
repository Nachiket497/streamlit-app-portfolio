import streamlit as st
from support_fun import load_text

def make_intro():
    col1, col2 = st.columns([8,5])
    component_contact = load_text('contact.html')
    with col1:
        st.markdown("<h1 class='f60'>Nachiket Sawwalakhe</h1>", unsafe_allow_html=True)
        st.markdown("<p class='f30'>ASIC Verification Engineer At Ceremorphic</p>", unsafe_allow_html=True)

        st.markdown("""<p class='f18 pad-right'> Hey there! I'm a graduate of batch 2023 from Visvesvaraya National Institute of Technology Nagpur <a href="https://vnit.ac.in/">(VNIT)</a>  with a degree in Electronics and Communication Engineering and a CGPA of 9.18/10. My academic journey has been all about dedication and staying motivated. I love diving into solo and collaborative projects, always on the lookout for chances to grow. </p> """, unsafe_allow_html=True)

        st.markdown(""" <p class='f18 pad-right'> Being a part of Ceremorphic, has been an exhilarating journey. I've been deeply immersed in UVM-based design verification of PCIe 6.0 and CXL 3.0 controllers, ensuring their robust functionality and compliance. Additionally, my experience in scripting with Python has allowed me to automate tasks, streamline processes, and enhance efficiency in verification workflows. </p>""", unsafe_allow_html=True)


        st.markdown(""" <p class='f18 pad-right'> Now, armed with a solid foundation in ASIC design verification and scripting, I am eager to tackle real-world challenges in these dynamic fields. Let's collaborate to drive innovation and achieve excellence in ASIC design verification.</p> """, unsafe_allow_html=True)

        st.components.v1.html(component_contact, height=50)

    with col2:
        st.markdown("")
        st.markdown("")
        st.image("img/self.jpeg", width=1, use_column_width=True)

        


