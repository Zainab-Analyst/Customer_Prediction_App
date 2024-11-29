import streamlit as st
import joblib
import pandas as pd

#load your model
model_9_features = joblib.load("model_9_features.pkl")

#lets create a manual mapping for the education col
education_mapping ={
    "Basic": 0,
    "Graduation": 1,
    "2n Cycle": 2,
    "Master": 3,
    "PhD": 4
}

#app title
st.title("Customer Purchase Prediction")
st.write("Predict whether a customer will respond positively to your marketing campaign.")

#Input form for customer data
st.sidebar.header("Input Customer Details")
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30)
income = st.sidebar.number_input("Income", min_value=1000, max_value=100000, value=30000)
education = st.sidebar.selectbox("Education Level", ["Basic", "Graduation", "2n Cycle", "Masters", "PhD"])
num_web_visits_month = st.sidebar.number_input("Number of Web Visits Per Month", min_value=0, max_value=30, value=5)
recency = st.sidebar.number_input("Recency (days since last purchase)", min_value=0,  max_value=365, value=10)
num_store_purchases = st.sidebar.number_input("Number of Store Purchases", min_value=0, max_value=100, value=5)
mnt_gold_prods_percentage = st.sidebar.number_input("Gold Products Purchased Percentage", min_value=0.0, max_value=100.0, value=30.0)
mnt_fish_products_percentage = st.sidebar.number_input("Fish Products Purchased Percentage", min_value=0.0, max_value=100.0, value=10.0)
store_ratio = st.sidebar.number_input("Store Purchase Ratio",min_value=0.0, max_value=1.0, value=0.5) 
    
#convert education input to numeric
education_encoded = education_mapping[education]

#format input into a df
input_data = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Education": [education_encoded],
    "NumWebVisitsMonth": [num_web_visits_month],
    "Recency": [recency],
    "NumStorePurchases": [num_store_purchases],
    "MntGoldProds_Percentage": [mnt_gold_prods_percentage],
    "MntFishProducts_Percentage": [mnt_fish_products_percentage],
    "Store_Ratio": [store_ratio]
})

#make predictions when the 'predict' button is clicked

if st.button("Predict"):
    prediction = model_9_features.predict(input_data)[0]
    if prediction == 1:
        st.success("The customer is likely to respond positively!")
    else:
        st.warning("The customer is unlikely to respond positively!")
    