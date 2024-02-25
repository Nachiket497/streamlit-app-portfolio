import streamlit as st

langs = ['Python', 'C++', 'System Verilog', 'Verilog', 'C', 'Java']
protocols = ['APB-5', 'AXI-4', 'CAN-FD', 'CXL-3.0', 'PCIe-6.0']
softwares = ['Android Studio', 'Arduino IDE', 'Multisim', 'Verdi', 'MATLAB']
research_tools = ['ArduPilot', 'ROS', 'Gazebo', 'OpenCV', 'NumPy', 'SymPy', 'Pandas', 'SciPy', 'Matplotlib']
hardware_tools = ['Arduino', 'ESP8266-01', 'ESP-32', 'Jetson TX1 & TX2', 'R-Pi', 'Pixhawk']

def make_skills(screen_width):
    st.markdown("<h1 class='f60'>Skills</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([5, 5])

    with col1:
        # this is for Programming Languages
        st.markdown("<h2 class='f30'>Programming Languages</h2>", unsafe_allow_html=True)
        # place each lang in small card with gray background 
        cards_html = ""
        for lang in langs:
            cards_html += f"<p class='f18 smallcard'>{lang}</p>"

        st.markdown(f"<div class='cards-container'>{cards_html}</div>", unsafe_allow_html=True)

    with col2:
        # this is for protocols known
        st.markdown("<h2 class='f30'>Protocols</h2>", unsafe_allow_html=True)
        protocols_html = "" 
        for protocol in protocols:
            protocols_html += f"<p class='f18 smallcard'>{protocol}</p>"
        st.markdown(f"<div class='cards-container'>{protocols_html}</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3, 3, 3])

    with col1:
        # this is for software known
        st.markdown("<h2 class='f30'>Software</h2>", unsafe_allow_html=True)
        software_html = ""
        for software in softwares:
            software_html += f"<p class='f18 smallcard'>{software}</p>"
        st.markdown(f"<div class='cards-container'>{software_html}</div>", unsafe_allow_html=True)
     
    with col2:
        # this is for research tools worked on
        st.markdown("<h2 class='f30'>Research Tools</h2>", unsafe_allow_html=True)
        research_html = ""
        for research_tool in research_tools:
            research_html += f"<p class='f18 smallcard'>{research_tool}</p>"
        st.markdown(f"<div class='cards-container'>{research_html}</div>", unsafe_allow_html=True)

    with col3:
        # this is for hardware tools know
        st.markdown("<h2 class='f30'>Hardware Tools</h2>", unsafe_allow_html=True)
        hardware_html = ""
        for hardware_tool in hardware_tools:
            hardware_html += f"<p class='f18 smallcard'>{hardware_tool}</p>"
        st.markdown(f"<div class='cards-container'>{hardware_html}</div>", unsafe_allow_html=True)

       



