import streamlit as st
from base64 import b64encode


st.set_page_config(page_title  = "Anuraag's web portfolio", layout = "wide")

st.write(f"""
<style>
         
    .title-bar {{
        background-color: green;
        color: white;
        font-size: 32px;
        padding: 15px 0;
        margin: 10px;
        text-align: center;
        width: 100vw;
        margin-left: -3.5rem;
        margin-right: -3.5rem;
    }}
</style>

<div class="title-bar">
    Anuraag's Web Portfolio
</div>
""", unsafe_allow_html=True)



def get_base64_image(path):
    with open(path, "rb") as img_file:
      return "data:image/jpeg;base64," + b64encode(img_file.read()).decode()

img = get_base64_image("Anuraag_Deepak.jpg")

st.write(f""" 
<div style = "justify-content: center; display: flex;">

<img src="{img}" alt = "Anuraag Deepak" style = "width: 300px; height: 300px; border-radius: 10%; margin: 10px; border-color: red">

</div>
""",
unsafe_allow_html=True)

st.write(f"""
         <div style = "text-align:center; margin: 10px;"> Texas A&M Computer Science Student </div>""",
         unsafe_allow_html = True)

icons_data = {
   "LinkedIn": ["https://www.linkedin.com/in/anuraag-deepak-202612215/", get_base64_image("LinkedIn.jpg")], 
   "GitHub": ["https://github.com/anud4344", get_base64_image("GitHub.jpg")]
}

icons_html = [
     f"<a href='{icons_data[link][0]}' target='_blank' style='margin: 10px;' title='{link}'>"
     f"<img src='{icons_data[link][1]}' alt='{link}' style='width: 40px; height: 40px;'/>"
     f"</a>"
     for link in icons_data 
]



st.write(f"""
     <div style = "display: flex; justify-content: center; margin-bottom: 20px;">
     {''.join(icons_html)}
     </div>
   """, unsafe_allow_html=True)

st.write("##")

st.markdown("""
<div style="display: flex; justify-content: center; margin: 15px;">
  <div style="max-width: 900px; width: 100%; font-size: 18px;">
    <h2 style="text-align: center;">About Me</h2>
    <hr style="margin: 30px 0;">
    <ul style="line-height: 2.0;">
        <li>I am 21 years old and my nickname is Anu.</li>
        <li>I recently completed my third year of my <b>Computer Science</b> degree at <b>Texas A&M University</b>. I am also doing a minor in <b>Statistics</b>. I am an incoming senior student.</li>
        <li>My hobbies include using and researching Technology, reading about Geography, exercising, and watching documentaries.</li>
        <li>I am deeply interested in Computer Science and its applications in many fields and sectors. I intend on being a future <b>Software Engineer</b> after graduating.</li>
        <li>I am from Richmond, TX.</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="display: flex; justify-content: center; margin: 20px; padding: 10px;">
  <div style="max-width: 900px; width: 100%; font-size: 18px;">
    <h2 style="text-align: center;">My Experiences and Qualifications</h2>
    <hr style="margin: 30px;">
    <ul style="line-height: 1.6;">
        <li>I am a motivated Computer Science student with a keen interest for developing innovative software solutions.</li>
        <li>With a 3.7 GPA, I have a strong foundation in data structures, programming, algorithms, system design, and programming languages like Python, C++, and Java.</li>
        <li>I enjoy tackling complex problems, whether through software engineering, network programming, or cybersecurity concepts. My coursework has allowed me to work on real-world projects using Agile methodologies, React, PostgreSQL, and full-stack tools.</li>
        <li>SEC Directed Internship (Student Engineers' Council): R&D Engineering Intern at <b>Arkisys </b> (3 months). (summer 2023)</li>
        <li>HR Administrator Intern at City of Missouri City (2 months). (Summer 2023)</li>
        <li>Graduated Summa Cum Laude (top 5.6%) from <b>Stephen F. Austin High School </b> (34/600) in Spring 2022.</li>
        <li>Going to do a 1-month remote internship for <b>HCL Tech</b>.</li>
        <li>101- Introduction to Cluster Computing with the University of Houston's Hewlett Packard Enterprise Data Science Institute. I received this certificate in Summer 2022.</li>
        <li> Going to complete the AWS Certified Cloud Practitioner Certification. (Cloud Computing)</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="display: flex; justify-content: center; margin: 20px; padding: 10px;">
   <div style="max-width: 900px; width: 100%; font-size: 18px;">
    <h2 style="text-align: center;">Skills</h2>
    <hr style="margin: 20px 0;">
     <ul style="columns: 2; -webkit-columns: 2; -moz-columns: 2; list-style-position: inside; padding-left: 20px;">
       <li>HTML</li>
       <li>CSS</li>
       <li>Python</li>
       <li>C++</li>
       <li>Java</li>
       <li>React JS</li>
       <li>PostgreSQL</li>
       <li>R Studio</li>
       <li>SymPy</li>
       <li>Git</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="display: flex; justify-content: center; margin: 20px; padding: 10px;">
   <div style="max-width: 900px; width: 100%; font-size: 18px;">
    <h2 style="text-align: center;">Projects</h2>
    <hr style="margin: 30px;">
    <ul style="text-align: left; list-style-position: outside;">
       <li>Created a Wordle Game using Java and Java FX</li>
       <li>Created a Resume website using HTML, CSS, and JavaScript</li> 
       <li> Developed an inventory system to reduce overhead, track customer orders, analyze ordering trends, and manage restocking. 
            The database was generated in AWS using a Python script and evaluated through SQL queries to analyze sales history, peak sales periods, and menu item inventory levels. 
            A graphical user interface (GUI) was implemented to support customer, cashier, and manager functionalities, including order submission, item and price updates, inventory restocking, employee management, and report generation. 
            The frontend was designed using React JS for building user interfaces and React Router for navigation between pages. 
            The backend was developed with Node JS for server-side logic and API integration, PostgreSQL for data storage, and Axios for handling API requests.
      </li>    
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)

