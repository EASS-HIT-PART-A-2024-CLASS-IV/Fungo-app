import streamlit as st
import httpx as re 
import json

def main_page():
    st.set_page_config("Fungo App")
    st.title("Fungo 🚗")


    #localhost run
    
    #r = re.get("http://localhost:8080/v1/main_page/")
    r = re.get("http://backend:8080/v1/main_page/")

    js_data = r.text
    message = json.loads(js_data)
    message = message["message"]
    st.subheader(message)
        
    st.write("Your parking journey begins now. Easily manage your reserved spots.\nWith our app, parking in Tel Aviv is not just a convenient - it's a seamless experiece tailored to your needs\n\Happy parking!")
    st.write("So... what do you want to do next?")
    
    
    col1, col2, col3= st.columns(3)
    
    with col1:
        parking_link = st.button("Start Parking")
    with col2:
        user_link = st.button("User information")
    with col3:
        log_out = st.button("log out")
        
    if parking_link:
        st.session_state.page = "start_parking"
        st.rerun()
    if user_link:
        st.session_state.page = "user_info"
        st.rerun() 
    if log_out:
        st.session_state.page = "login"
        st.rerun()