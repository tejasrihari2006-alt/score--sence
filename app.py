import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="GPA Predictor", layout="centered")

model = joblib.load("model.pkl")

st.title("🎓 Student GPA Predictor")

sleep = st.slider("Sleep Hours", 0, 12, 7)
social = st.slider("Social Media Hours", 0, 12, 3)
study = st.slider("Study Hours", 0, 12, 5)
attendance = st.slider("Attendance Percentage", 0, 100, 80)

if st.button("Predict GPA"):
    data = np.array([[sleep, social, study, attendance]])
    result = model.predict(data)
    st.success(f"Predicted GPA: {result[0]:.2f}")