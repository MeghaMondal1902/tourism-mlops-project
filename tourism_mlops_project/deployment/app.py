
import streamlit as st
import pandas as pd
import joblib

from huggingface_hub import hf_hub_download

# Download the trained model from Hugging Face

MODEL_PATH = hf_hub_download(
    repo_id="meghamondal1902/tourism-package-model",
    filename="tourism_model.pkl",
    repo_type="model"
)

# Load the trained model

model = joblib.load(MODEL_PATH)

# Create the application title

st.title("Tourism Package Prediction")

st.write(
    "Predict whether a customer is likely to purchase a tourism package."
)

# Collect customer information

Age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

TypeofContact = st.selectbox(
    "Type of Contact",
    ["Self Enquiry", "Company Invited"]
)

CityTier = st.selectbox(
    "City Tier",
    [1, 2, 3]
)

DurationOfPitch = st.number_input(
    "Duration of Pitch",
    value=15
)

Occupation = st.selectbox(
    "Occupation",
    [
        "Salaried",
        "Small Business",
        "Large Business",
        "Free Lancer"
    ]
)

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

NumberOfPersonVisiting = st.number_input(
    "Number of Persons Visiting",
    min_value=1,
    value=2
)

NumberOfChildrenVisiting = st.number_input(
    "Number of Children Visiting",
    min_value=0,
    value=0
)

MaritalStatus = st.selectbox(
    "Marital Status",
    ["Single", "Married", "Divorced"]
)

MonthlyIncome = st.number_input(
    "Monthly Income",
    value=30000
)

# Generate prediction when the button is clicked

if st.button("Predict"):

    # Create engineered feature

    FamilySize = (
        NumberOfPersonVisiting +
        NumberOfChildrenVisiting
    )

    # Prepare model input

    input_df = pd.DataFrame({

        "Age": [Age],
        "TypeofContact": [TypeofContact],
        "CityTier": [CityTier],
        "DurationOfPitch": [DurationOfPitch],
        "Occupation": [Occupation],
        "Gender": [Gender],
        "NumberOfPersonVisiting":
            [NumberOfPersonVisiting],
        "NumberOfChildrenVisiting":
            [NumberOfChildrenVisiting],
        "MaritalStatus":
            [MaritalStatus],
        "MonthlyIncome":
            [MonthlyIncome],
        "FamilySize":
            [FamilySize]
    })

    # Make prediction

    prediction = model.predict(input_df)[0]

    # Display prediction result

    if prediction == 1:

        st.success(
            "Customer is likely to purchase the package."
        )

    else:

        st.error(
            "Customer is unlikely to purchase the package."
        )
