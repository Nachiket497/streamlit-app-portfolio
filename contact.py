import streamlit as st

def make_contact():



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
        