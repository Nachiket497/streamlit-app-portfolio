import streamlit as st
from support_fun import local_css
from support_fun import img_to_bytes
from support_fun import glich
from support_fun import project_dict
import math



def make_card(img_path, title, code, tab, col):
    with tab :
        with col :
            ip = f"""
                  
                <div class="card" " style="width: 98%; height : 98%; border : 1px solid black; text-align:center; box-shadow: 4px 4px 8px 0px rgba(0, 0, 0, 0.2), 6px 6px 20px 0px rgba(0, 0, 0, 0.19);" >
                    <img src='data:image/png;base64,{img_to_bytes(img_path)}' alt="Avatar" style="width: 80%; padding: 5% 5% 5% 5%;  border-radius: 5px;">
                    <h4 id="demo" ><b>{title}</b></h4>
                    <div style="padding: 0% 0% 4% 0%;">
                    <button onclick="window.open('{title.replace(" ","_")}', '_blank')">Know More</button>
                     </div>
                </div>
                 
                """
            st.components.v1.html(ip, width=300, height=365)

            
      
def make_project(screen_width):

    num_columns = math.floor(screen_width/270)
    print(num_columns, screen_width)
    # create 4 tabs
    tabs_name = ['All', 'Robotics', 'Electronics/Control Systems', 'Software Development']
    st.markdown("<h1 class='f60' >Projects</h1>", unsafe_allow_html=True)
    


    t_all, t_robotics, t_vlsi, t_software = st.tabs(tabs_name)

    cols = []

    tabs = [t_all, t_robotics, t_vlsi, t_software]

    for tab in tabs:
        cols.append(tab.columns(num_columns))
    
    # glich()
    count = [0, 0, 0, 0]
    for title in project_dict.keys():
        # try :
            if project_dict[title]['categaory'] == 'Robotics':
                make_card(project_dict[title]['img'], title, project_dict[title]['code'], t_robotics,   cols[1][count[1]%num_columns] )
                count[1] += 1
            
            elif project_dict[title]['categaory'] == 'Electronics/Control Systems':
                make_card(project_dict[title]['img'], title, project_dict[title]['code'],   t_vlsi, cols[2][count[2]%num_columns]  )
                count[2] += 1
            
            elif project_dict[title]['categaory'] == 'Software Development':
                make_card(project_dict[title]['img'], title, project_dict[title]['code'], t_software, cols[3][count[3]%num_columns]  )
                count[3] += 1

            else:
                print("Invalid category")
        
        
            make_card(project_dict[title]['img'], title,project_dict[title]['code'], t_all, cols[0][count[0]%num_columns] )
            count[0] += 1

        # except Exception as e:
        #     print(e)
    

          




