# ❤️ Heart Disease Risk Predictor

An interactive web application built with **Streamlit** that uses **Machine Learning** to assess the likelihood of heart disease in patients based on clinical parameters.

## 🚀 Overview
This project uses a **Random Forest Classifier** trained on heart health data to provide real-time risk assessments. It features a user-friendly sidebar for data entry and provides visual feedback on risk probability along with health recommendations.

<img width="1909" height="863" alt="image" src="https://github.com/user-attachments/assets/df1fd369-ce61-4186-8bf9-8bec64d2699f" />



## 📊 Model Performance
The underlying model was evaluated against multiple algorithms:
* **Random Forest:** ~86.4% Accuracy (Selected Model)
* **Logistic Regression:** ~85.3% Accuracy

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **Data Handling:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn
- **Model Persistence:** Joblib

## 📂 Project Structure
```text
heart-disease-predictor/
├── heart_disease_app.py
├── heart_disease_model.pkl
├── scaler.pkl
├── requirements.txt=
└── README.md
```

## ⚙️ Installation & Setup
Follow these steps to get the project running on your local machine:

### 1. Prerequisites
Ensure you have Python 3.9+ installed. You can check your version by running:
```text
python --version
```
### 3. Clone the Repository
```text
git clone [https://github.com/your-username/heart-disease-predictor.git](https://github.com/your-username/heart-disease-predictor.git)
cd heart-disease-predictor
```
### 4. Create a Virtual Environment
```text
python -m venv venv
```
#### Activate it
On Windows:
```text
venv\Scripts\activate
```
On macOS/Linux:
```text
source venv/bin/activate
```
### 5. Install Dependencies
### 6. Run the Application
Launch the Streamlit server:
```text
streamlit run heart_disease_app.py
```
The app will be available at http://localhost:8501 in your browser.
