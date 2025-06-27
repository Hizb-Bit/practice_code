#BMI Webpage

import streamlit as st
import pandas as pd

def bmi_calculator():
    st.title("BMI Calculator")

    weight = st.number_input("Enter your weight (kg):", min_value=0.0)
    height = st.number_input("Enter your height (m):", min_value=0.0)

    if weight > 0 and height > 0:
        bmi = weight / (height * height)
        st.success(f"Your BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        st.write(f"BMI Category: {category}")

        data = {'BMI': [bmi], 'Category': [category]}
        df = pd.DataFrame(data)
        st.table(df)

bmi_calculator()