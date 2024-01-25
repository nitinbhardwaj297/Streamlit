import streamlit as st
import time
import os
import getcmts as gc

#functions
def run_javascript(js_code):
    st.markdown(f"<script>{js_code}</script>", unsafe_allow_html=True)
port = int(os.environ.get("PORT", 8501)) 
#main 
st.set_page_config(
    page_title="scrape-comments!",
    page_icon="U+1FAE0"
)
st.title(("SCRAPE INSTAGRAM COMMENTS FOR DATA-ANALYSIS AND RESEARCH!🐍"))
image_url = '122.jpg'
st.image(image_url)
st.header("ENTER INSTAGRAM CREDENTIALS!!")
email = st.text_input("Enter your email:", type='default')
password = st.text_input("Enter your password:", type='password')
url = st.text_input("Enter a URL:", type='default')
if st.button("submit!"):
    time.sleep(1)
    st.write('processing!!!')
    time.sleep(1)
    st.write("will take atleast 5mins!!!")
    t=1
    while t<=5:
        try:
            file=gc.cmntsget(email,password,url)
            file=str(file)
            break
        except:
            st.write(f"attempt{t} failed!")
            t=t+1
    if 'file' in globals():
        st.write("sucess!")
        st.download_button("DOWNLOAD",file,'text/csv')
    else:
        st.write("process failed!!😔")
        if st.button("try again!🔁"):
            run_javascript("location.reload();")
    st.header("PROCESS EXECUTED!!🤖")