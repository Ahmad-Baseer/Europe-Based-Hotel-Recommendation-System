import streamlit as st
from streamlit_lottie import st_lottie
import requests as req
import import_ipynb
from Hotel_Recommendation_System import recommender

st.set_page_config(page_title="Hotel Recommendation System",page_icon=":hotel:",layout="wide")

with st.container():
    st.title("Welcome to Hotel Recommendation System :hotel:")
    st.subheader("Author: Ahmad Baseer")
    st.write("You can find the code [here](https://github.com/Ahmad-Baseer/AI-Projects)")

def ret_country(country):
    if(country=="Netherlands"):
        return "NL"
    if(country=="United Kingdom"):
        return "UK"
    if(country=="France"):
        return "FR"
    if(country=="Spain"):
        return "ES"
    if(country=="Italy"):
        return "IT"
    if(country=="Austria"):
        return "AT"

def load_lottieurl(url):
    r=req.get(url)
    if r.status_code !=200:
        None
    return r.json()

lottie_hotel=load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_xrptzsed.json")
    
with st.container():
    st.write("---")
    left_col,midl_col,right_col=st.columns(3)
    
    with left_col:
        st.write("##")
        st.write("##")
        country=ret_country(st.selectbox("Country",('Netherlands','United Kingdom','France','Spain','Italy','Austria')))
        st.write(country)
        
    with midl_col:
        st.write("##")
        st.write("##")
        description = st.text_area("Description", placeholder="Enter a description of your trip (e.g. [' Leisure trip ', ' Group ', ' Duplex Double Room ', ' Stayed 1 night '])")
        
    with right_col:
        st_lottie(lottie_hotel,height=250,key="hotel")
        
    with midl_col:
        st.write("##")
        button=st.button("Recommend",help="Will Recommend hotels based on their ratings!")
        
    with st.container():
        if(button):
            st.dataframe(recommender(country,description))
            st.balloons()
            st.snow()
        
    with st.container():
        st.write("##")
        st.header("Get in Touch with me!")
        st.write("##")
        contact_form="""
        <form action="https://formsubmit.co/asfars305@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false" required>
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your Message Here" required></textarea>
     <button type="submit">Send</button>
     </form>
        """
        ul_col,ur_col=st.columns(2)
        
        with ul_col:
            st.markdown(contact_form, unsafe_allow_html=True)
            
        with ur_col:
            st.empty()
            
#using local css to design contact form
def local_css_for_contact_form(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
        
local_css_for_contact_form("style.css")
