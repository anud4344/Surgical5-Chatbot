import streamlit as st 
from PIL import Image
from base64 import b64encode
import io

# Set Background Color of page. 
# background-color: #97c4f7; /* Replace with your desired color */

def get_base64_image(path):
    with open(path, "rb") as img_file:
      return "data:image/jpeg;base64," + b64encode(img_file.read()).decode()

img = get_base64_image("./pages/Avery_Martin.jpeg")

page_bg_color = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #a5d6a7;
    # background-image: linear-gradient(to right, #e3f2fd, #fdfdfd); /* Light blue to white */
    margin: 0 !important;
    padding: 0 !important;
    width: 100vw !important;
    color: black;
}

/* Style the image container to center the image */
.image-container {
    display: flex;
    justify-content: center;
    padding: 5px; /* Add some vertical padding if needed */
    background-image: linear-gradient(to right, #104f9c, #28b4fd);
    border-radius: 5px;
}

.profile-image {
    max-width: 300px; /* Adjust as needed */
    height: auto;
    width: 200px;
    border-radius: 5px; /* Optional: round image corners */
    box-shadow: 2px 2px 5px #ccc; /* Optional: add a subtle shadow */
}

</style>
"""
# imaage style="max-width: 100%; height: auto;" width="200"; 
# style="background-image: linear-gradient(to right, #104f9c, #28b4fd); padding: 10px; border-radius: 5px; display: flex; justify-content: center;" 
st.markdown(page_bg_color, unsafe_allow_html=True)

# st.title("Avery Martin")
st.markdown("<h1  style='color: #004d40;'>Avery Martin </h1>", unsafe_allow_html=True)

# Section 1: Profile Photo

try:
    st.write(f""" 
    <div class="image-container">
    <img class="profile-image"; src="{img}" alt = "Avery Martin">

    </div>
    """,unsafe_allow_html=True)
   
except FileNotFoundError:
    st.error("Error: Profile image not found. Please make sure 'profile.jpg' is in the correct location.")
except Exception as e:
    st.error(f"An error occurred: {e}")
    
    
# Section 2: Bio
bio_html = """
<div>
    <h2 style='color: black;'>About Me</h2>
    <div style='font-size: 23px;'>
    <p>This is a paragraph of <strong>important</strong> information about me.
    I have a passion for <i>building things</i> and learning new technologies.</p>
    <ul>
        <li>Experience in Python</li>
        <li>Knowledge of Streamlit</li>
        <li>Eager to collaborate</li>
    </ul>
    </div>
</div>
"""
st.markdown(bio_html, unsafe_allow_html=True)

# Section 3: Biographic Details
# st.subheader("Biographic Details")
st.markdown("<h2 style='color: 	#1b3b0f;'>Biographic Details</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
      st.markdown("""
    <div style='font-size: 23px;'>
        <p><strong>Date of Birth:</strong><br>February 12, 2008</p>
        <p><strong>Home Country:</strong><br>Texas</p>
        <p><strong>Nick Name:</strong><br>Ave</p>
    </div>
    """, unsafe_allow_html=True)
    # st.markdown("**Date of Birth:**")
    # st.markdown("February 12, 2008")
    # st.markdown("**Home Country**")
    # st.markdown("Texas")
    # st.markdown("**Nick Name:**")
    # st.markdown("Ave")
    
    # ... and so on

with col2:
    st.markdown("""
    <div style='font-size: 23px;'>
        <p><strong>Hobbies:</strong><br>Working on Computer Science items, Coding, Spending time with family, Watching movies, Working on Tech Applications</p>
        <p><strong>School:</strong><br>Harmony school of innovation</p>
    </div>
    """, unsafe_allow_html=True)
   
st.markdown("<h2 style='color: #3e2723'>Leadership & Service</h2>", unsafe_allow_html=True)
st.markdown("""
<div style='font-size: 23px;'>
    <p><strong>Service:</strong><br>Leadership in Training YMCA</p>
</div>
""", unsafe_allow_html=True)
# st.markdown("**Service:**")
# st.markdown("Leadership in Training YMCA")
bio_html1 = """
<div>
     <div style='font-size: 23px;'>
    <h2 style='color: #283593'>Community service</h2>
    <p>This is a paragraph of my community service.
    I have a passion for <i>building things</i> and learning new technologies.</p>
    <ul>
        <li>Leaders in Training in a positive social support</li>
        <li>Volunteered and helped with day care services</li>
        <li>Volunteered and checked each person entering and exiting the YMCA</li>
    </ul>
    </div>
</div>
"""
st.markdown(bio_html1, unsafe_allow_html=True)
#st.markdown("Leaders in Training in a positive social support. Volunteered and helped with day care services. Volunteered and checked each person entering and exiting the ymca. volunteered and helped assisted in the work out facility. Volunteered and helped with after summer school activities. Volunteered and helped with pick up after summer sessions")
# ... your career highlights here