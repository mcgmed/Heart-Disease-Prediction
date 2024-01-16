import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the pre-trained model
model_path = 'best_rf_model.pkl'
best_rf_model = joblib.load(model_path)

# Function to predict heart disease based on user input
def predict_heart_disease(age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope):
    # Convert categorical input to one-hot encoded format
    input_data = pd.DataFrame({
        'Age': [age],
        'Sex': [sex],
        'ChestPainType': [chest_pain_type],
        'RestingBP': [resting_bp],
        'Cholesterol': [cholesterol],
        'FastingBS': [fasting_bs],
        'RestingECG': [resting_ecg],
        'MaxHR': [max_hr],
        'ExerciseAngina': [exercise_angina],
        'Oldpeak': [oldpeak],
        'ST_Slope': [st_slope]
    })

    input_data_encoded = pd.get_dummies(input_data, columns=['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope'])
    
    # Make prediction
    prediction = best_rf_model.predict(input_data_encoded)

    return prediction[0]

# Streamlit UI
def main():
    st.title("Heart Disease Prediction App")

    # User input form
    age = st.slider("Select Age:", min_value=20, max_value=80, value=40, step=1)
    sex = st.selectbox("Select Gender:", ["Male", "Female"])
    chest_pain_type = st.selectbox("Select Chest Pain Type:", ["ATA", "NAP", "ASY", "TA"])
    resting_bp = st.slider("Select Resting Blood Pressure:", min_value=80, max_value=200, value=120, step=1)
    cholesterol = st.slider("Select Cholesterol Level:", min_value=85, max_value=603, value=200, step=1)
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl:", ["No", "Yes"])
    resting_ecg = st.selectbox("Select Resting ECG Result:", ["Normal", "ST", "LVH"])
    max_hr = st.slider("Select Maximum Heart Rate:", min_value=60, max_value=202, value=150, step=1)
    exercise_angina = st.selectbox("Exercise-Induced Angina:", ["No", "Yes"])
    oldpeak = st.slider("Select ST Depression Induced by Exercise Relative to Rest:", min_value=0.0, max_value=6.2, value=1.0, step=0.1)
    st_slope = st.selectbox("Select ST Slope:", ["Up", "Flat", "Down"])

    # Make prediction
    if st.button("Predict"):
        gender_mapping = {'Male': 'M', 'Female': 'F'}
        fasting_bs_mapping = {'No': 0, 'Yes': 1}
        exercise_angina_mapping = {'No': 'N', 'Yes': 'Y'}

        sex = gender_mapping[sex]
        fasting_bs = fasting_bs_mapping[fasting_bs]
        exercise_angina = exercise_angina_mapping[exercise_angina]

        prediction = predict_heart_disease(age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope)

        # Display prediction
        st.subheader("Prediction Result:")
        if prediction == 1:
            st.success("The model predicts that the individual has heart disease.")
        else:
            st.success("The model predicts that the individual does not have heart disease.")

if __name__ == "__main__":
    main()
