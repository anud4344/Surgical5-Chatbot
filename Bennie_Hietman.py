import streamlit as st 
from PIL import Image
from base64 import b64encode
import io

# Set Background Color of page. 
# background-color: #97c4f7; /* Replace with your desired color */

def get_base64_image(path):
    with open(path, "rb") as img_file:
      return "data:image/jpeg;base64," + b64encode(img_file.read()).decode()

img = get_base64_image("./pages/images/bennie_hietman.png")

page_bg_color = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #97c4f7; 
    background-image: linear-gradient(to right, #f0f0f0, #97c4f7); /* Your gradient */
    margin: 0 !important; /* Remove default margins */
    padding: 0 !important; /* Remove default padding */
    width: 100vw !important; /* Full viewport width */

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
st.markdown("<h1  style='color: #007bff;'>Bennie Hietman</h1>", unsafe_allow_html=True)

# Section 1: Profile Photo

try:
    st.write(f""" 
    <div class="image-container">
    <img class="profile-image"; src="{img}" alt = "Bennie Hietman">

    </div>
    """,unsafe_allow_html=True)
   
except FileNotFoundError:
    st.error("Error: Profile image not found. Please make sure 'profile.jpg' is in the correct location.")
except Exception as e:
    st.error(f"An error occurred: {e}")
    
    
# Section 2: Bio
bio_html = """
<div>
    <h2 style='color: #007bff;'>About Me</h2>
    <p>This is a paragraph of <strong>important</strong> information about me.
    I have a passion for <i>building things</i> and learning new technologies.</p>
    <ul>
        <li>Experience in Python</li>
        <li>Knowledge of Streamlit</li>
        <li>Eager to collaborate</li>
    </ul>
</div>
"""
st.markdown(bio_html, unsafe_allow_html=True)

# Section 3: Biographic Details
# st.subheader("Biographic Details")
st.markdown("<h3 style='color: #ffc107;'>Biographic Details</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Date of Birth:**")
    st.markdown("February 19, 2007")
    st.markdown("**Home Country**")
    st.markdown("The United States of America")
    st.markdown("**Nick Name:**")
    st.markdown("BlackHat")
    
    # ... and so on

with col2:
    st.markdown("**Hobbies:**")
    st.markdown("Robotics, Technology, Volunteering")
    st.markdown("**Education:**")
    st.markdown("Xavier Educational Academy; St. Thomas University starting 2025-2026 school year")
    # ... and so on
    
# Section 4: Career Highlights
# st.subheader("Educational and Personal Highlights")
st.markdown("<h3 style='color: #dc3545;'>Career Highlights</h3>", unsafe_allow_html=True)

st.markdown("**Awards:**")
st.markdown("A school althetic medal for Soccer")
st.markdown("**Achievement:**")
st.markdown("Graduated Xavier Educational Academy with the High School Diploma")
# ... your career highlights here