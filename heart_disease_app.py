import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

# Title
st.title("❤️ Heart Disease Risk Predictor")
st.markdown("*Enter patient details to assess heart disease risk*")

# Load model and feature columns
@st.cache_resource
def load_models():
    try:
        model = joblib.load('heart_disease_model.pkl')
        feature_columns = joblib.load('features.pkl')

        return model, feature_columns

    except FileNotFoundError as e:
        st.error(f"Model file not found: {e}")
        st.info("Make sure these files are in the same directory:")
        st.code("""
        - heart_disease_model.pkl
        - features.pkl
        """)
        return None, None


# Load model
model, feature_columns = load_models()

if model is not None:

    # Sidebar
    st.sidebar.header("📋 Patient Information")

    def user_input_features():

        # Numerical inputs
        age = st.sidebar.slider("Age", 20, 100, 54)

        resting_bp = st.sidebar.number_input(
            "Resting Blood Pressure (mm Hg)",
            80,
            200,
            130
        )

        cholesterol = st.sidebar.number_input(
            "Cholesterol (mg/dl)",
            100,
            600,
            240
        )

        max_hr = st.sidebar.number_input(
            "Maximum Heart Rate",
            60,
            220,
            150
        )

        oldpeak = st.sidebar.number_input(
            "ST Depression (Oldpeak)",
            0.0,
            6.0,
            1.0,
            0.1
        )

        # Categorical inputs
        sex = st.sidebar.selectbox(
            "Sex",
            ["M", "F"]
        )

        chest_pain = st.sidebar.selectbox(
            "Chest Pain Type",
            ["ATA", "NAP", "ASY", "TA"]
        )

        fasting_bs = st.sidebar.selectbox(
            "Fasting Blood Sugar > 120 mg/dl",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )

        resting_ecg = st.sidebar.selectbox(
            "Resting ECG",
            ["Normal", "ST", "LVH"]
        )

        exercise_angina = st.sidebar.selectbox(
            "Exercise Angina",
            ["N", "Y"]
        )

        st_slope = st.sidebar.selectbox(
            "ST Slope",
            ["Up", "Flat", "Down"]
        )

        # Create dataframe
        data = {
            'Age': age,
            'Sex': sex,
            'ChestPainType': chest_pain,
            'RestingBP': resting_bp,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_bs,
            'RestingECG': resting_ecg,
            'MaxHR': max_hr,
            'ExerciseAngina': exercise_angina,
            'Oldpeak': oldpeak,
            'ST_Slope': st_slope
        }

        return pd.DataFrame(data, index=[0])

    # Get user input
    input_df = user_input_features()

    # Display user data
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Patient Information")
        st.dataframe(input_df, use_container_width=True)

    # Preprocess input
    def preprocess_input(df):

        df_processed = df.copy()

        categorical_cols = [
            'Sex',
            'ChestPainType',
            'RestingECG',
            'ExerciseAngina',
            'ST_Slope'
        ]

        # One-hot encode categorical variables
        df_encoded = pd.get_dummies(
            df_processed,
            columns=categorical_cols
        )

        # Add missing columns
        for col in feature_columns:
            if col not in df_encoded.columns:
                df_encoded[col] = 0

        # Keep same column order as training
        df_encoded = df_encoded[feature_columns]

        return df_encoded

    # Prediction button
    if st.button(
        "🔍 Predict Heart Disease Risk",
        type="primary",
        use_container_width=True
    ):

        with st.spinner("Analyzing patient data..."):

            # Preprocess input
            processed_input = preprocess_input(input_df)

            # Predict
            prediction = model.predict(processed_input)
            prediction_proba = model.predict_proba(processed_input)

            # Results
            st.markdown("---")
            st.subheader("📊 Prediction Results")

            result_col1, result_col2, result_col3 = st.columns([1, 1, 1])

            with result_col1:

                if prediction[0] == 1:
                    st.error("## ⚠️ HIGH RISK")
                    st.markdown("**Heart Disease Likely**")

                else:
                    st.success("## ✅ LOW RISK")
                    st.markdown("**Heart Disease Unlikely**")

            with result_col2:

                st.metric(
                    "Risk Probability",
                    f"{prediction_proba[0][1]:.1%}"
                )

                st.progress(float(prediction_proba[0][1]))

            with result_col3:

                st.markdown("### Confidence Scores")

                st.write(
                    f"🟢 Low Risk: {prediction_proba[0][0]:.1%}"
                )

                st.write(
                    f"🔴 High Risk: {prediction_proba[0][1]:.1%}"
                )
                
else:
    st.error("Failed to load model files.")