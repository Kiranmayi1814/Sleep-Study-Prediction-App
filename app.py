import streamlit as st
import numpy as np
import pickle

# Load trained model and scaler
model = pickle.load(open("sleep_model.sav", "rb"))
scaler = pickle.load(open("sleep_scaler.sav", "rb"))

st.set_page_config(page_title="Sleep Study Prediction", layout="centered")

st.title("😴 Sleep Study Prediction App")
st.write("Predict whether you are getting **Enough Sleep** based on daily habits.")

st.markdown("---")

# Input fields
Hours = st.number_input("Hours of Sleep", min_value=0.0, max_value=24.0, step=0.5)
PhoneReach = st.selectbox("Phone Reachable While Sleeping?", ("No", "Yes"))
PhoneTime = st.selectbox("Used Phone Before Sleep?", ("No", "Yes"))
Tired = st.slider("Tired Level (1 = Fresh, 5 = Very Tired)", 1, 5)
Breakfast = st.selectbox("Had Breakfast?", ("No", "Yes"))

# Encode categorical inputs
PhoneReach = 1 if PhoneReach == "Yes" else 0
PhoneTime = 1 if PhoneTime == "Yes" else 0
Breakfast = 1 if Breakfast == "Yes" else 0

# Predict button
if st.button("Predict Sleep Quality 🚀"):
    input_data = np.array([[Hours, PhoneReach, PhoneTime, Tired, Breakfast]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    # 🎉 GLITTER BLAST
    st.balloons()
    if prediction == 1:
        st.success("✅ Prediction: Enough Sleep 😴💙")
    else:
        st.error("❌ Prediction: Not Enough Sleep 😵‍💫")

st.markdown("---")
st.caption("Developed by Your kiranmayi")