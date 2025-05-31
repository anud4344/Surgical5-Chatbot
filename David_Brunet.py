import streamlit as st 
from PIL import Image
from base64 import b64encode
import io

# Set Background Color of page. 
# background-color: #97c4f7; /* Replace with your desired color */

def get_base64_image(path):
    with open(path, "rb") as img_file:
      return "data:image/jpeg;base64," + b64encode(img_file.read()).decode()

img = get_base64_image("./pages/images/David_Brunet.jpeg")

page_bg_color = """
<style>
[data-testid="stAppViewContainer"] {
    background-color:  #4a90e2;
    # background-image: linear-gradient(to right, #f0f0f0, #97c4f7); /* Your gradient */
    margin: 0 !important; /* Remove default margins */
    padding: 0 !important; /* Remove default padding */
    width: 100vw !important; /* Full viewport width */
    color: white;
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

# st.title("David Brunet")
st.markdown("<h1  style='color: #ffffff;; font-weight: bold;'>David Brunet</h1>", unsafe_allow_html=True)

# Section 1: Profile Photo

try:
    st.write(f""" 
    <div class="image-container">
    <img class="profile-image"; src="{img}" alt = "David Brunet">

    </div>
    """,unsafe_allow_html=True)
   
except FileNotFoundError:
    st.error("Error: Profile image not found. Please make sure 'profile.jpg' is in the correct location.")
except Exception as e:
    st.error(f"An error occurred: {e}")
    
    
# Section 2: Bio
bio_html = """
<div>
    <h2 style='color: #ccff00; font-weight: bold;'>About Me</h2>
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
st.markdown("<h2 style='color: 	#00ffff; font-weight: bold;'>Biographic Details</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div style='font-size: 23px;'>
        <p><strong>Date of Birth:</strong><br>July 23, 1973</p>
        <p><strong>Home Country:</strong><br>Canada</p>
        <p><strong>Nick Name:</strong><br>SuperDave, Blue, Sprocket</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='font-size: 23px;'>
        <p><strong>Hobbies:</strong><br>Robotics, Technology, Volunteering</p>
        <p><strong>Work:</strong><br>DLZP Group - VP R&D, Innovation Spark - Volunteer</p>
    </div>
    """, unsafe_allow_html=True)
    
# Section 4: Career Highlights
# st.subheader("Career Highlights")
st.markdown("<h2 style='color: 	#bf40bf; font-weight: bold;'>Career Highlights</h2>", unsafe_allow_html=True)

st.markdown("""
<div style='font-size: 23px;'>
    <p><strong>Awards:</strong><br>Top 10% Consultants at Oracle</p>
    <p><strong>Achievement:</strong><br>Started HACR Combat Robotics, Innovation Spark, Houston Maker Faire</p>
</div>
""", unsafe_allow_html=True)