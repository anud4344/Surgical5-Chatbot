import streamlit as st 
from PIL import Image
from base64 import b64encode
import io

# Set Background Color of page. 
# background-color: #97c4f7; /* Replace with your desired color */

def get_base64_image(path):
    with open(path, "rb") as img_file:
      return "data:image/jpeg;base64," + b64encode(img_file.read()).decode()

img = get_base64_image("./pages/Erick_Carreno.jpg")

page_bg_color = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #97c4f7; 
    background-image: linear-gradient(to right, #87ceeb, #97c4f7); /* Your gradient */
    margin: 0 !important; /* Remove default margins */
    padding: 0 !important; /* Remove default padding */
    width: 100vw !important; /* Full viewport width */
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

# st.title("David Brunet")
st.markdown("<h1  style='color: #003300; font-weight: bold;'>Erick Carreno</h1>", unsafe_allow_html=True)

# Section 1: Profile Photo

try:
    st.write(f""" 
    <div class="image-container">
    <img class="profile-image"; src="{img}" alt = "Erick Carreno">

    </div>
    """,unsafe_allow_html=True)
   
except FileNotFoundError:
    st.error("Error: Profile image not found. Please make sure 'profile.jpg' is in the correct location.")
except Exception as e:
    st.error(f"An error occurred: {e}")
    
    
# Section 2: Bio
bio_html = """
<div>
    <h2 style='color: #004d40; font-weight: bold;'>About Me</h2>
    <div style='font-size: 23px;'>
    <p>I am a 15 year old student who likes to code every now and then.  Here's some information about me.
    I have a passion for <i>building things</i> and learning new technologies through the year.</p>
    <ul>
        <li>I am gaining experience in Python</li>
        <li>I now have knowledge of Streamlit</li>
        <li>Eager to collaborate</li>
        <li>I am short tempered, so dont worry about me getting mad!</li>
        <li>Finally, I am always ready to get the job done.</li>
    </ul>
   </div>
</div>
"""
st.markdown(bio_html, unsafe_allow_html=True)

# Section 3: Biographic Details
# st.subheader("Biographic Details")
st.markdown("<h3 style='color: #0d47a1; font-weight: bold;'>Biographic Details</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
      st.markdown("""
    <div style='font-size: 23px;'>
        <p><strong>Date of Birth:</strong><br>May 11th, 2009</p>
        <p><strong>Home Country:</strong><br>The United States of America</p>
        <p><strong>Nick Name:</strong><br>Erikku</p>
    </div>
    """, unsafe_allow_html=True)
    # st.markdown("**Date of Birth:**")
    # st.markdown("May 11th, 2009")
    # st.markdown("**Home Country**")
    # st.markdown("The United States of America")
    # st.markdown("**Nick Name:**")
    # st.markdown("Erikku")
    
    # ... and so on

with col2:
    st.markdown("""
    <div style='font-size: 23px;'>
        <p><strong>Hobbies:</strong><br>Chess, Retro Stuff, Soccer, etc</p>
        <p><strong>Education:</strong><br>Waltrip High School - National Honor Society Sophomore</p>
    </div>
    """, unsafe_allow_html=True)
    # st.markdown("**Hobbies:**")
    # st.markdown("Chess, Retro Stuff, Soccer, etc")
    # st.markdown("**Education:**")
    # st.markdown("Waltrip High School- National Honor Society Sophomore")
    # # ... and so on
    
# Section 4: Career Highlights
# st.subheader("Education Highlights")
st.markdown("<h3 style='color: #8e24aa; font-weight: bold;'>Education Highlights</h3>", unsafe_allow_html=True)
 
st.markdown("""
<div style='font-size: 23px;'>
    <p><strong>Awards:</strong><br>College Board First Gen Recognition</p>
    <p><strong>Achievement:</strong><br>First Special Education NHS Member at my High School, Projected as Top 10%</p>
</div>
""", unsafe_allow_html=True)
# st.markdown("**Awards:**")
# st.markdown("College Board First Gen Recognition")
# st.markdown("**Achievement:**")
# st.markdown("First Special Education NHS Member at my High School, Projected as Top 10%")
# # ... your career highlights here