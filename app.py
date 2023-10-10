from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# 1. started by installing streamlit in terminal: pip install streamlit
# 2. get some emojis from webfx.com
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ------------load asset--------------
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_vnikrcia.json")
img_contact_forms = Image.open("images/datascience.jpeg")
img_contact_animation = Image.open("images/datascience1.jpeg")
img_contact_place = Image.open("images/ui.jpeg")
# In terminal install lottie : pip install streamlit-lottie
# Also in the terminal install requests : pip install requests
#--------------------- Header -------------------------
with st.container(): 
    st.subheader("Hi, I am Daniel :wave:")
    st.title("A computer programmer with Python Language Skills")
    st.write("I am passionate about coding. Come let's build websites with python language")
    st.write("[learn More >](https://twitter.com/DannyT_841)")
# ----------------- About me -------------------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2) #4. division of column in this section
    with left_column: #5. for the left column 
        st.subheader("What can we do?")
        st.write("##")
        st.write(
            """
            Let's begin our coding journey:"
            - Start a career with python 
            - Take a beginner's tutorial to enhance your skills
            - Follow Up on your daily discovers
            - Join let's build incredible projects
            """
        )
        st.write("[Follow for more >](https://twitter.com/DannyT_841)")
    #head over to lottieFiles.com for get your animation format
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")
#-------------PROJECT-------------
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    # insert image
    with image_column:
        st.image(img_contact_animation)
    # to insert images in our file install pillow in the terminal : pip install pilloww
    with text_column:
        st.header("Advance Your Skills and taking career to the next level")
        st.write(
            """
            Learn how to use python to Grow your business!
            Develop advance skills and build creative projects
            """
        )
        st.markdown("[watch Video >](https://twitter.com/DannyT_841)")
    with st.container():
        image_column,text_column = st.columns((1,2))
        
        with image_column:
            st.image(img_contact_place)
        with text_column:
            st.write(
                """
                Learn how to connect your websites to database with Python!
                Develop a strong backend connection and server-line with python to support your projects.
                 """
            )

            st.markdown("[Watch Video...](https://twitter.com/DannyT_841)")
    # ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/youremail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
    # run the code using streamlit run with file name in this case app.py (streamlit run app.py)