import streamlit as st
import time
import httpx as re 
import json

def register_page():
    st.set_page_config("Register Page")
    st.write("Register:")
    email_reg = st.text_input(label="Email",placeholder="Email")
    password_reg = st.text_input(label="Password", type="password", placeholder="Password", help="Please type a strong password at least 8 characters")
    name_reg = st.text_input(label="Username", placeholder="Username")
    phone_number_reg = st.text_input(label="Phone number", placeholder="Phone")
    car_number_reg = st.number_input(label="Car number", placeholder="Car number",  min_value=1000000, max_value=99999999, value=None, step=1)
    
    js_data = {
        "email" : email_reg,
        "password": password_reg,
        "username":name_reg,
        "phone_number": phone_number_reg,
        "car_number":car_number_reg
    }    

    if st.button("Register") and email_reg and password_reg and name_reg and phone_number_reg and car_number_reg:


        #localhost run:
        #r = re.post("http://localhost:8080/v1/register/", json=js_data)
        r = re.post("http://backend:8080/v1/register/", json=js_data)
        js_data_r = r.text
        js_data_r = json.loads(js_data_r)

        if r.status_code == 200 and js_data_r["message"] == "Email is already in use":
            st.error("Email is already in use, please use a different email")

        else:
            with st.spinner("Creating user, please wait..."):
                time.sleep(2)

            st.toast("User is Registered successfully\n redirecting to login...",  icon="✅")
            time.sleep(2)
            st.session_state.page = "login"
            st.rerun()
            
    else:
        st.error("Please insert all fields!")
        
    if st.button("Go back"):
        with st.spinner("Please wait"):
            time.sleep(1)

        st.session_state.page = "login"
        st.rerun()