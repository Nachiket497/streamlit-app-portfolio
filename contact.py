import streamlit as st
from support_fun import load_text

def make_contact():


    st.markdown("")
    st.markdown("")

    contact_form = """
    <form action="https://formsubmit.co/1000nachiket@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with right_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with left_column:
        st.markdown("")
        st.header("Any Queries ?")
        
        st.markdown("<p class='f18'>Feel free to contact me. I will get back to you as soon as possible. Also check me on :</p>", unsafe_allow_html=True)
        component_contact = load_text('contact.html')
        st.components.v1.html(component_contact, height=50) 
