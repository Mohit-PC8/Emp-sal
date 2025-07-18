# app.py
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('salary_model.pkl')

# Title
st.title("💰 Employee Salary Predictor")
st.subheader("Predict salaries based on employee characteristics")

# Input form
with st.form("salary_form"):
    age = st.number_input("Age", min_value=18, max_value=70, value=30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])
    job_title = st.text_input("Job Title", "Software Engineer")
    experience = st.slider("Years of Experience", 0.0, 30.0, 5.0)
    
    # Feature engineering
    seniority = 1 if 'senior' in job_title.lower() else 0
    management = 1 if any(word in job_title.lower() for word in ['manager', 'director', 'vp', 'head', 'chief']) else 0
    
    submitted = st.form_submit_button("Predict Salary")
    
    if submitted:
        input_data = pd.DataFrame({
            'Age': [age],
            'Gender': [gender],
            'Education Level': [education],
            'Job Title': [job_title],
            'Years of Experience': [experience],
            'Seniority': [seniority],
            'Management': [management]
        })
        
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Salary: ${prediction:,.2f}")

# Instructions
st.markdown("""
### Instructions
1. Fill in all employee details
2. Click 'Predict Salary'
3. Job titles should be specific (e.g. 'Senior Software Engineer')
""")