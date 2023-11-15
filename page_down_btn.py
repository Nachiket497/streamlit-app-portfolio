import streamlit as st

custom_button = """
    <style>
        .scroll-button-container {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 999;
        }

        .scroll-button {
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            font-size: 24px;
            cursor: pointer;
        }
    </style>

    <div class="scroll-button-container">
        <button class="scroll-button" onclick="scrollPage()">
            &#8595;
        </button>
    </div>

    <script>
        function scrollPage() {
            window.scrollBy({
                top: window.innerHeight,
                left: 0,
                behavior: 'smooth'
            });
        }
    </script>
"""

# Inject custom HTML, CSS, and JavaScript
def make_down_btn():
    st.markdown(custom_button, unsafe_allow_html=True)

