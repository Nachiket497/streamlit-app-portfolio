import streamlit as st
from pathlib import Path
import base64


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_text(file_path):
    """A convenience function for reading in the files used for the site's text"""
    with open(file_path) as in_file:
        return in_file.read()
    
tabs_name = ['All', 'Robotics', 'Electronics/Control Systems', 'Software Development']

project_dict = { 

    "CXL-PCIe Controller Verification" : {
        "img" : "img/cxl.png",
        "description" : "<li>Performed verification of the 68B mode CXL Link layer and Arb Mux layer, ensuring protocol compliance and functionality.</li><li>Designed 256B mode CXL Arb Mux with a weightage round-robin module and L0p support</li><li>Currently working on verification of the LTSSM in the PHY layer of PCIe controller</li>",
        "duration" : "Feb 2023 - Present",
        "code" : "",
        "categaory" : "Electronics/Control Systems"
    },

    "Enquiry Registration App" : {
        "img" : "img/Enquiry.png",
        "description" : "<li>Developed an android application for the enquiry registration of the customors.</li> <li>Implemented the application using the Firebase Realtime Database for storing the data.</li><li>ALso developed a client side application for the admin to view and manage the enquiries.</li>",
        "duration" : "May 2023",
        "code" : "https://github.com/Nachiket497/Enquiry-App",
        "categaory" : "Software Development"
    },

    "VNIT Telephone Directory" : {
        "img" : "img/VTD.jpeg",
        "description" : "<li>Developed an android application to find extention number of the faculty and staff of VNIT.</li> <li>Implemented relaltime connection between excel sheet, firebase database and android application.</li><li>Designed various feactures like optimise search by name, quick call etc.</li>",
        "duration" : "Dec 2022",
        "code" : "https://github.com/IDS-VNIT/vnit_telephone_app",
        "categaory" : "Software Development"
    },

    "Autonomous Fertiliser bot" : {
        "img" : "img/image1.gif",
        "description" : "<li>Designed  ground robot with a rocker bogie mechanism to optimize fertilizer application, reducing waste by delivering nutrients directly to plant roots.</li><li>Developed small-scale farming, the compact and lightweight design ensures seamless navigation through tight spaces, offering an efficient and cost-effective solution for fertilization process.</li><li>Implemented a plantation layout following algorithum using OpenCV.</li> <li> Published research paper titled 'Design and Implementation of an Autonomous Plantation Layout Follower Fertilizer Bot for Advanced Farming' at the PCEMS Conference.  </li>",
        "duration" : "Aug 2022 - Dec 2022",
        "code" : "https://github.com/Nachiket497/AFB_code https://ieeexplore.ieee.org/document/10136100",
        "categaory" : "Robotics"
    },
 
    "Autonomus Driving Platform" : {
        "img" : "img/adp.gif",
        "description" : "<li>Designed a platform for autonomous driving using ROS and Gazebo.</li><li>Implemented the colour detection and following using OpenCV.</li><li>Developed a PID controller for steering and speed control of the vehicle.</li>",
        "duration" : "Sep 2022",
        "code" : "",
        "categaory" : "Robotics"
    },

    "Quadruped" : {
        "img" : "img/quadurped.gif",
        "description" : "<li>Designed a quadruped robot with 12 degrees of freedom </li> <li>Implemented the trot, crawl-walking gait using semi-elliptical trajectory and inverser kinematics for a single quadruped leg on hardware using ROS.</li>",
        "duration" : "July 2022 - Aug 2022",
        "code" : "https://github.com/IvLabs/Quadruped_Robotics",
        "categaory" : "Robotics"
    }, 

    "CommonRoad" : {
        "img" : "img/common.gif",
        "description" : "<li>Implemented a futurifier for the linear temporal logic(LTL) by using rtamt python liberary and tested with the help of NuSMV Tester.</li>   <li>Generated random LTL models and LTL specifications from the tree to verify the results of the futurifier using NuSMV.</li> <li>Visualized and implemented the single-trailer truck model in CommonRoad-io liberary.</li>",
        "duration" : "May 2022 - July 2022",
        "code" : "",
        "categaory" : "Software Development"
    },

    "Quadrupilot" : {
        "img" : "img/vecros.jpg",
        "description" : "<li>Added the remote control and developed a successful communication between the Pixhawk and actuators via Mission Planner using the CAN-Bus protocol.</li>  <li>Implemented the trot, crawl-walking gait using semi-elliptical trajectory and inverser kinematics for a single quadruped leg on hardware.</li> ",
        "duration" : "Dec 2021 - Feb 2022",
        "code" : "",
        "categaory" : "Robotics"
    },

    "Trajectory generation for bipedal walking" : {
        "img" : "img/Multistep_3D.gif",
        "description" : "T<li>Implemented a 3D linear inverted pendulum model for bipedal walking and generated trajectories for the centre of mass and swing foot. </li> <li>Developed a time sequence of states given a constant COM height trajectory for locomotion.</li>",
        "duration" : "June 2021 - July 2021",
        "code" : "https://github.com/Nachiket497/biped_walking",
        "categaory" : "Robotics"
    },

    "Trajectory Optimization of Cart Pole" : {
        "img" : "img/optimize1.gif",
        "description" : "<li>Generated an optimal swing-up trajectory for a cart-pole system with minimum energy objective and boundary constraints in state and time.</li> <li>Obtained the solution of optimization problem using CasADi Toolbox and simulated the generated trajectories using Matplotlib.</li>",
        "duration" : "May 2021 - June 2021",
        "code" : "https://github.com/Nachiket497/trajectory_optimization",
        "categaory" : "Robotics"
    },

    "Reconfigurable Robotics" : {
        "img" : "img/q2h1.gif",
        "description" : " <li>Designed a reconfigurable robotic system that transforms between serpentine, wheeled-quadrupedal, and humanoidal locomotion modes without any rearrangement.</li> <li>Developed transition gaits for reconfiguration between serpentine, wheeled-quadruped and biped.</li>  <li>Implemented geometric locomotion gaits of serpentine for linear progression, lateral undulation, rolling and rotation and walking gaits of wheeled quadruped for crawling and trotting. </li>",
        "duration" : "April 2021 - May 2021",
        "code" : "https://drive.google.com/file/d/1WklsGTju2-ZOsPBwW0gTP8u28iZbrFs0/view",
        "categaory" : "Robotics"
    },

    "PID Controller using Op-Amp" : {
        "img" : "img/Circuit_diagram.jpeg",
        "description" : "<li>Designed a PID control system using Op-Amp which regulate the voltage drop across the system.</li> <li>Implemented the controller in multisim12 and performed the transient analysis for the different set-points.</li>",
        "duration" : "April 2021",
        "code" : "https://github.com/Nachiket497/PID_Controller_using_OP-Amp",
        "categaory" : "Electronics/Control Systems"
    },

    "Manipulation of Robotic Arm" : {
        "img" : "img/pick_place1.gif",
        "description" : " <li>Implemented the forward dynamics, forward kinematics, inverse kinematics and position control of serial link manipulators.</li><li>Accomplished an end effector trajectory control for a ‘straight line follower' task using inverse kinematics based on Newton-Raphson method.</li> <li> Developed an algorithm for 'Pick & Place' task for UR5 manipulator using PyBullet. </li>",
        "duration" : "Nov 2020 - April 2021",
        "code" : "https://github.com/IvLabs/manipulation",
        "categaory" : "Robotics"
    },

    "Music Player" : {
        "img" : "img/mus.jpg",
        "description" : "<li>Designed a simple music player using android studio with basic features <ul> <li>Full list of all songs in the device.</li> <li>Separate player for playing the songs with cover photo and other details.</li> <li>Interactive notification widgets and works in the background. </li> </ul> </li>",
        "duration" : "Aug 2020 - Nov 2020",
        "code" : "https://github.com/Nachiket497/Music_Player",
        "categaory" : "Software Development"
    },

    "Air Quality Checker" : {
        "img" : "img/new.jpg",
        "description" : "<li>Established a circuit to read the data from the sensor MQ-135 and display it on an android app. </li> <li>The connection is developed between an android app and Arduino via ThingSpeak using Wi-Fi Module  ESP8266-01</li> <li> The application is capable of monitoring air quality in real time. </li>",
        "code" : "https://github.com/Nachiket497/IOT_Base_Air_Qulity_checker",
        "duration" : "Aug 2020 - Nov 2020",
        "categaory" : "Software Development"
    },

    "Cruise Controller" : {
        "img" : "img/task2_without_slope.jpeg",
        "description" : " <li>Designed a cruise controller for a planar mobile robot to achieve the desired velocity based on PID control law in MATLAB.</li> <li> Extended the controller to adapt to changes in the terrain slope, friction, and setpoint changes in the desired velocity.</li>",
        "duration" : "July 2020 - Aug 2020",
        "code" : "https://github.com/Nachiket497/CRUISE-CONTROLLER",
        "categaory" : "Electronics/Control Systems"
    },

    "Data Synchronization Via Firebase" : {
        "img" : "img/sm.jpg",
        "description" : " <li>Implemented synchronization of textual data between an android device and a python script on the  desktop PC using the Firebase Database in real-time.</li><li>Created a real-time database on the firebase console via browser. The application connects to the database on startup.</li>",
        "duration" : "July 2020 - Aug 2020",
        "code" : "https://github.com/Nachiket497/FirebaseAPK",
        "categaory" : "Software Development"
    }
}



job_dict = {
    "job1": {
        "Job_title": "VLSI Verification Engineer",
        "Job_role": "Full Time & Internship",
        "Job_place": "Ceremorphic, Inc.",
        "Job_date": "Feb 2023 - Present"
    },
    "job3": {
        "Job_title": "Research Intern",
        "Job_role": "Internship",
        "Job_place": "TU Munich",
        "Job_date": "May 2022 - July 2022"
    },
    "job4": {
        "Job_title": "Robotics Intern",
        "Job_role": "Internship",
        "Job_place": "VECROS TECH",
        "Job_date": "Dec 2021 - Jan 2022"
    },
    "job5": {
        "Job_title": "Summer Intern",
        "Job_role": "Internship",
        "Job_place": "IvLabs, VNIT",
        "Job_date": "July 2020 - Aug 2020"
    } 
}



def glich():
    st.components.v1.html("""
    <script>
    function checkElements() {
        const tabs = window.parent.document.querySelectorAll('button[data-baseweb="tab"] p');
        const tab_panels = window.parent.document.querySelectorAll('div[data-baseweb="tab-panel"]');

        if (tabs && tab_panels) {

            tabs.forEach(function (tab, index) {
                const tab_panel_child = tab_panels[index].querySelectorAll("*");

                function set_visibility(state) {
                    tab_panels[index].style.visibility = state;
                    tab_panel_child.forEach(function (child) {
                        child.style.visibility = state;
                    });
                }

                tab.addEventListener("click", function (event) {
                    set_visibility('hidden')

                    let element = tab_panels[index].querySelector('div[data-testid="stVerticalBlock"]');
                    let main_block = window.parent.document.querySelector('section.main div[data-testid="stVerticalBlock"]');
                    const waitMs = 1;

                    function waitForLayout() {
                        if (element.offsetWidth === main_block.offsetWidth) {
                            set_visibility("visible");
                        } else {
                            setTimeout(waitForLayout, waitMs);
                        }
                    }

                    waitForLayout();
                });
            });
        } else {
            setTimeout(checkElements, 100);
        }
    }

    checkElements()
    </script>
    """, height=0)
