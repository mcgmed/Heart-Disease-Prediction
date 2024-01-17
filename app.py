import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
best_rf_model = joblib.load('/app/best_rf_model.pkl')

# Function to preprocess user input
def preprocess_input(age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs,
                     resting_ecg, max_hr, exercise_angina, oldpeak, st_slope):
    # One-hot encode categorical variables
    input_data = pd.DataFrame({
        'Age': [age],
        'RestingBP': [resting_bp],
        'Cholesterol': [cholesterol],
        'FastingBS': [fasting_bs],
        'MaxHR': [max_hr],
        'Oldpeak': [oldpeak],
        'Sex_F': [1 if sex == 'F' else 0],
        'Sex_M': [1 if sex == 'M' else 0],
        'ChestPainType_ASY': [1 if chest_pain_type == 'ASY' else 0],
        'ChestPainType_ATA': [1 if chest_pain_type == 'ATA' else 0],
        'ChestPainType_NAP': [1 if chest_pain_type == 'NAP' else 0],
        'ChestPainType_TA': [1 if chest_pain_type == 'TA' else 0],
        'RestingECG_LVH': [1 if resting_ecg == 'LVH' else 0],
        'RestingECG_Normal': [1 if resting_ecg == 'Normal' else 0],
        'RestingECG_ST': [1 if resting_ecg == 'ST' else 0],
        'ExerciseAngina_N': [1 if exercise_angina == 'N' else 0],
        'ExerciseAngina_Y': [1 if exercise_angina == 'Y' else 0],    
        'ST_Slope_Down': [1 if st_slope == 'Down' else 0],
        'ST_Slope_Flat': [1 if st_slope == 'Flat' else 0],
        'ST_Slope_Up': [1 if st_slope == 'Up' else 0]
    })
    return input_data

# Streamlit app
st.title("Heart Disease Prediction App")

# Get user input
age = st.slider("Select Age:", min_value=20, max_value=80, value=40)
sex = st.selectbox("Select Gender:", ['M', 'F'])
chest_pain_type = st.selectbox("Select Chest Pain Type:", ['ATA', 'NAP', 'ASY', 'TA'])
resting_bp = st.slider("Select Resting Blood Pressure:", min_value=90, max_value=200, value=120)
cholesterol = st.slider("Select Cholesterol Level:", min_value=100, max_value=400, value=200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl:", [0, 1])
resting_ecg = st.selectbox("Select Resting ECG Result:", ['Normal', 'ST', 'LVH'])
max_hr = st.slider("Select Max Heart Rate:", min_value=60, max_value=200, value=150)
exercise_angina = st.selectbox("Exercise-Induced Angina:", ['N', 'Y'])
oldpeak = st.slider("Select Oldpeak (ST Depression):", min_value=0.0, max_value=6.2, value=0.0)
st_slope = st.selectbox("Select ST Slope:", ['Up', 'Flat', 'Down'])

# Add a "Predict" button
if st.button("Predict"):
    # Preprocess user input
    input_data = preprocess_input(age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs,
                                  resting_ecg, max_hr, exercise_angina, oldpeak, st_slope)

    # Make prediction
    prediction = best_rf_model.predict(input_data)[0]

    # Display result
    st.subheader("Prediction Result:")
    if prediction == 1:
        st.success("The model predicts that the patient may have heart disease.")
    else:
        st.success("The model predicts that the patient may not have heart disease.")
