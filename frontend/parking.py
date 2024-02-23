import streamlit as st
import time
import pandas as pd
import httpx as re 
import json
from data import data, dataPrice

df = pd.DataFrame(data, columns =["Minutes", "In hours"])
df_price = pd.DataFrame(dataPrice,columns = ["Region", "Price"])

def start_parking():
    st.set_page_config("Parking")
    st.header("Hello Parker!")
    st.subheader("Upgrade your parking experience in Tel Aviv!\nElevate your city adventures with hassle-free parking,\nbecause convenience should always come standard.")
    st.divider()
    region = st.selectbox(
        "Please select the region where you want to rent your parking spot:",
        ("North Tel Aviv", "West Tel Aviv", "East Tel Aviv", "South Tel Aviv"),
        index=None,
        placeholder="Region selection"
        )
    
    st.divider()
    #DataFrame representing the hours that the app can give the user.
    col1, col2 = st.columns(2)
    with col1:
        st.write("Hour by minutes table explanation:")
        st.dataframe(df)
    with col2:
        st.write("Prices for each region per minutes:")
        st.dataframe(df_price)
    
    st.text("Please select amount time by minutes\nthat you want to rent the parking spot:")
    minutes = st.slider("Amount minutes selection, default is 30 minutes: ", min_value=30, max_value=240, value=30, step=1)
    
    js_data = {
        "region":region,
        "time_parking":minutes
    }
    
    btn_calc = st.button("Calculate amount")
    if btn_calc:
        if region:

            value = re.post("http://backend:8080/v1/startparking/", json=js_data)

            cost_value = value.text
            cost_value = json.loads(cost_value)
            price = cost_value["price"]
            st.write(f"This parking spot costs: {price}₪")
        else:
            st.error("Please select region first!")

    btn_payment = st.button("Payment")

    if btn_payment:
        time.sleep(2)
        st.success("Payment is done!")
        time.sleep(3)
        st.rerun()

    home_btn = st.button("Back to home page")

    if home_btn:
        st.session_state.page = "main_page"
        st.rerun()