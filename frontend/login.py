import streamlit as st
import time
import httpx as re 


##LOGIN PAGE##
def login_page():
    st.set_page_config("Welcome to Fungo!")
    st.title("Welcome to Fungo! 🚗")
    st.subheader("Fungo is a web application that lets you rent a parking spot in Tel Aviv by minutes only by choosing the regions where you want to park your car.", divider="rainbow")
    st.write("Unlock seamless parking in the heart of Tel Aviv with out app,\nfind, reserve, and pay for your parking spot effortlessly,\nensuring a stress-free experience.\nYour convenient parking solution is just at tap away!")
    st.text("Please, for your own use, register or login below:")
    st.write("Login:")
    email = st.text_input(label="Email")
    password = st.text_input(label="Password", type="password")
    
    js_data = {
        "email":email,
        "password":password
    }
    if st.button("Log in") and email and password:
        
        #localhost run
        #r = re.post("http://localhost:8080/v1/login/", json=js_data)
        r = re.post("http://backend:8080/v1/login/", json=js_data)
        if r.status_code == 401:
            st.error("Invalid credentials, email or password is incorrect")
        elif r.status_code == 200:
            with st.spinner("Login in, please wait..."):
                time.sleep(2)   
            st.session_state.page = "main_page"
            st.rerun()
    st.divider()
    st.write("Not Registered? please press register below:")
    if st.button("Register"):
        st.session_state.page = "register"
        st.rerun()