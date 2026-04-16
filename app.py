import streamlit as st
import requests
import pandas as pd

st.title("📈 Google Stock Prediction App")

st.write("Enter number of days to predict:")

days = st.slider("Days", 1, 60, 10)

if st.button("Predict"):
    url = "https://stock-api-hzc7.onrender.com/predict"
    
    response = requests.get(url, params={"days": days})
    
    if response.status_code == 200:
        data = response.json()
        
        df = pd.DataFrame(data)
        
        st.subheader("Prediction Data")
        st.write(df)
        
        st.subheader("Prediction Graph")
        st.line_chart(df["yhat"])
    
    else:
        st.error("API Error")
