
import streamlit as st
import pickle
import pandas as pd

with open("LRM.pickle", "rb") as f:
    model = pickle.load(f)

st.title("Salary Predictor")
experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.1)

if st.button("Predict Salary"):
    input_df = pd.DataFrame([[experience]], columns=["YearsExperience"])
    prediction = model.predict(input_df)
    st.success(f"Predicted Salary: {prediction[0]:.2f} Rupees")
