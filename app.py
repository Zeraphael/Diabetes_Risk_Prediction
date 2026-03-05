import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the model and feature columns
model = joblib.load('diabetes_model.pkl')
feature_columns = joblib.load('model_columns.pkl')

# Create the web interface
st.title("🩺 Diabetes Risk Assessment Tool")
st.markdown("Enter patient information to predict diabetes risk category")

# Create input fields (grouped in columns for better layout)
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=20, max_value=84, value=45)
    bmi = st.number_input("BMI", min_value=16.0, max_value=50.0, value=25.0, step=0.1)
    blood_pressure = st.number_input("Blood Pressure", min_value=91, max_value=200, value=120)

with col2:
    fasting_glucose = st.number_input("Fasting Glucose Level", min_value=60, max_value=281, value=95)
    insulin = st.number_input("Insulin Level", min_value=2.0, max_value=55.9, value=10.0, step=0.1)
    hba1c = st.number_input("HbA1c Level", min_value=4.1, max_value=11.0, value=5.5, step=0.1)

with col3:
    cholesterol = st.number_input("Cholesterol Level", min_value=139, max_value=309, value=200)
    triglycerides = st.number_input("Triglycerides Level", min_value=50, max_value=383, value=150)
    waist_circumference = st.number_input("Waist Circumference (cm)", min_value=60.0, max_value=150.0, value=90.0, step=0.1)

# Lifestyle factors in a separate section
st.subheader("Lifestyle Factors")
col4, col5, col6 = st.columns(3)

with col4:
    daily_calories = st.number_input("Daily Calorie Intake", min_value=1200, max_value=5249, value=2200)
    sugar_intake = st.number_input("Sugar Intake (g/day)", min_value=0.0, max_value=255.0, value=40.0, step=0.1)

with col5:
    sleep_hours = st.number_input("Sleep Hours", min_value=4.0, max_value=10.0, value=7.0, step=0.1)
    stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)

with col6:
    physical_activity = st.selectbox("Physical Activity Level", ["Low", "Moderate", "High"])
    family_history = st.selectbox("Family History of Diabetes", ["No", "Yes"])
    gender = st.selectbox("Gender", ["Male", "Female"])

# When user clicks the predict button
if st.button("Predict Diabetes Risk", type="primary"):
    # Create a dataframe with all input values
    input_data = {
        'age': age,
        'bmi': bmi,
        'blood_pressure': blood_pressure,
        'fasting_glucose_level': fasting_glucose,
        'insulin_level': insulin,
        'HbA1c_level': hba1c,
        'cholesterol_level': cholesterol,
        'triglycerides_level': triglycerides,
        'daily_calorie_intake': daily_calories,
        'sugar_intake_grams_per_day': sugar_intake,
        'sleep_hours': sleep_hours,
        'stress_level': stress_level,
        'waist_circumference_cm': waist_circumference,
        'gender_Female': 1 if gender == "Female" else 0,
        'gender_Male': 1 if gender == "Male" else 0,
        'physical_activity_level_High': 1 if physical_activity == "High" else 0,
        'physical_activity_level_Low': 1 if physical_activity == "Low" else 0,
        'physical_activity_level_Moderate': 1 if physical_activity == "Moderate" else 0,
        'family_history_diabetes_No': 1 if family_history == "No" else 0,
        'family_history_diabetes_Yes': 1 if family_history == "Yes" else 0
    }
    
    # Convert to DataFrame and ensure correct column order
    input_df = pd.DataFrame([input_data])
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)
    
    # Make prediction
    risk_code = model.predict(input_df)[0]
    risk_map = {0: "Prediabetes", 1: "Low Risk", 2: "High Risk"}
    
    # Try to get probability if model supports it
    try:
        probabilities = model.predict_proba(input_df)[0]
        confidence = max(probabilities) * 100
        confidence_text = f" (Confidence: {confidence:.1f}%)"
    except:
        confidence_text = ""
    
    # Show result with color coding
    result = risk_map[risk_code]
    if result == "High Risk":
        st.error(f"## Prediction: {result}{confidence_text}")
    elif result == "Prediabetes":
        st.warning(f"## Prediction: {result}{confidence_text}")
    else:
        st.success(f"## Prediction: {result}{confidence_text}")