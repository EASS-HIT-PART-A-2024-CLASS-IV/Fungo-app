import streamlit as st
import httpx as re 
import json

def user_info_page():
    st.set_page_config("User Information page")

    #localhost run:
    #value = re.get("http://localhost:8080/v1/user_info/")
    value = re.get("http://backend:8080/v1/user_info/")

    st.title("Fungo 🚗")
    st.header("User information:")
    js_data = value.text
    js_data = json.loads(js_data)
    username = js_data["User Name"]
    car_number = js_data["User Car Number"]
    email = js_data["User Email"]
    phone = js_data["User phone number"]
    
    st.subheader(f"Name: {username}")
    st.subheader(f"Car number: {car_number}")
    st.subheader(f"Email: {email}")
    st.subheader(f"Phone number: {phone}")
    
    st.divider()
    home_btn = st.button("Back to home page")
        
    if home_btn:
        st.session_state.page = "main_page"
        st.rerun()