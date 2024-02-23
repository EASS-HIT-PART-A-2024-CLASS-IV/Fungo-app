import streamlit as st
from login import login_page
from register import register_page
from main_pg import main_page
from parking import start_parking
from info import user_info_page

def main():
    if "page" not in st.session_state:
        st.session_state.page = "login"

    if st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "register":
        register_page()
    elif st.session_state.page == "main_page":
        main_page()
    elif st.session_state.page == "start_parking":
        start_parking()
    elif st.session_state.page == "user_info":
        user_info_page()

        

if __name__ == "__main__":
    main()