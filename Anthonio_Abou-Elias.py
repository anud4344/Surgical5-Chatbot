import streamlit as st 
from PIL import Image
from base64 import b64encode
import io

# Set Background Color of page. 
# background-color: #97c4f7; /* Replace with your desired color */

def get_base64_image(path):
    with open(path, "rb") as img_file:
      return "data:image/jpeg;base64," + b64encode(img_file.read()).decode()

img = get_base64_image("./pages/Anthonio_Elias.jpg")
# img = get_base64_image("Erick_Carreno.jpg")

page_bg_color = """
<style>
[data-testid="stAppViewContainer"] {
    # background-color: #97c4f7; 
    # background-image: linear-gradient(to right, #87ceeb, #97c4f7); /* Your gradient */
    margin: 0 !important; /* Remove default margins */
    padding: 0 !important; /* Remove default padding */
    width: 100vw !important; /* Full viewport width */
    color: black;
    # background-image: linear-gradient(to right, #ffcc80, #ffe0b2);
    background-color: #ffa726;
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

# st.title("Anthonio Abou-Elias")
st.markdown("<h1  style='color: black;'>Anthonio Abou-Elias</h1>", unsafe_allow_html=True)

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
    <h2 style='color: #2e7d32; font-weight: bold;'>About Me</h2>
     <div style='font-size: 23px;'>
    <p>This is a paragraph of <strong>important</strong> information about me.
    I have a passion for <i>Theatre</i>, Walt Disney and Acting.</p>
    <ul>
        <li>Disney </li>
        <li>Knowledge of Alladin</li>
        <li>Eager to Perform in front of an audience</li>
    </ul>
   </div>
</div>
"""
st.markdown(bio_html, unsafe_allow_html=True)

# Section 3: Biographic Details
# st.subheader("Biographic Details")
st.markdown("<h2 style='color: #1565c0; font-weight: bold;'>Biographic Details</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div style='font-size: 23px;'>
        <p><strong>Date of Birth:</strong><br>July 8, 2003</p>
        <p><strong>Home Country:</strong><br>Romania</p>
        <p><strong>Nick Name:</strong><br>Aladdin</p>
    </div>
    """, unsafe_allow_html=True)


with col2:
   st.markdown("""
    <div style='font-size: 23px;'>
        <p><strong>Hobbies:</strong><br>Acting, Theatre, Disney, Traveling</p>
        <p><strong>School:</strong><br>Langham Creek High</p>
    </div>
    """, unsafe_allow_html=True)
# Section 4: Career Highlights
# st.subheader("Career Highlights")
st.markdown("<h2 style='color: #512da8; font-weight: bold;'>Community Service & Achievements</h2>", unsafe_allow_html=True)

st.markdown("""
<div style='font-size: 23px;'>
    <p><strong>Awards:</strong><br>Helping Others in my Boy Scout Group</p>
    <p><strong>Achievement:</strong><br>Boy Scout</p>
</div>
""", unsafe_allow_html=True)