import streamlit as st
import time

# Page config
st.set_page_config(page_title="QuickHealth Pro Max", page_icon="🩺", layout="centered")

st.title("🩺 QuickHealth Pro Max – Interactive Symptom Checker")
st.caption("No loops. No functions. Just pure beginner Python logic ✨")

# Greeting based on session
st.markdown("👋 Hello there! Let's check how you're doing today.")

# User Info Section
st.markdown("## 👤 Personal Details")
name = st.text_input("Your name:")
gender = st.radio("Gender:", ["Male", "Female", "Other"])
age = st.slider("Age:", 1, 100, 28)

# Location selector for personalized suggestion
location = st.selectbox("📍 Your city (for nearby care suggestions):", ["Select", "New York", "Los Angeles", "Phoenix", "Austin", "Chicago"])

# Symptom Selection
st.markdown("## 🤒 Symptoms & Health Info")
symptoms = st.multiselect("Select all symptoms you're experiencing:", ["Fever", "Cough", "Fatigue", "Headache", "Chest Pain", "Shortness of Breath"])
main_symptom = st.selectbox("Which one is the most troubling?", ["Select"] + symptoms if symptoms else ["Select"])

# Additional Info
temp = st.number_input("🌡️ Body Temperature (°F):", 90.0, 110.0, 98.6)
days_sick = st.slider("📅 Days you’ve felt unwell:", 0, 14, 2)
smoker = st.radio("🚬 Do you smoke?", ["Yes", "No"])
sleep_hours = st.slider("🛌 Hours of sleep last night:", 0, 12, 6)
mood = st.selectbox("🧠 Current Mood:", ["Calm", "Anxious", "Sad", "Irritable"])
existing_conditions = st.checkbox("Do you have any pre-existing conditions (like diabetes, asthma, heart issues)?")

# Trigger Button
if st.button("🧠 Run Health Evaluation"):
    
    if name.strip() == "" or main_symptom == "Select":
        st.error("Please enter your name and choose at least one main symptom.")
    else:
        with st.spinner("Analyzing..."):
            time.sleep(2)
        
        risk_score = 0
        
        # Base logic
        if main_symptom == "Fever":
            if temp >= 102 or days_sick > 3:
                risk_score += 3
            elif age >= 60:
                risk_score += 2
            else:
                risk_score += 1
        elif main_symptom == "Cough":
            if days_sick >= 5:
                risk_score += 2
            else:
                risk_score += 1
        elif main_symptom == "Fatigue":
            if age > 30:
                risk_score += 2
            else:
                risk_score += 1
        elif main_symptom == "Headache":
            if temp > 100:
                risk_score += 2
            else:
                risk_score += 1
        elif main_symptom == "Chest Pain":
            risk_score += 3
        elif main_symptom == "Shortness of Breath":
            risk_score += 4
        else:
            risk_score += 1

        # Lifestyle impact
        if smoker == "Yes":
            risk_score += 2
        if sleep_hours < 6:
            risk_score += 1
        if mood in ["Anxious", "Sad", "Irritable"]:
            risk_score += 1
        if existing_conditions:
            risk_score += 2

        # Final Risk Summary
        st.markdown("## 🧾 Your Health Summary")
        if risk_score >= 7:
            st.error("🔴 **High Risk:** Please consult a doctor immediately.")
        elif risk_score >= 4:
            st.warning("🟠 **Moderate Risk:** Monitor closely. Seek advice if it continues.")
        else:
            st.success("🟢 **Low Risk:** You're likely okay. Stay hydrated and rested.")

        # Personalized suggestions
        st.markdown("## 📌 Personalized Advice")
        if gender == "Female" and age >= 45:
            st.info("🔹 Consider scheduling a routine health screening.")
        if gender == "Male" and smoker == "Yes":
            st.info("🔹 Quitting smoking can significantly improve your future health.")
        if existing_conditions:
            st.info("🔹 Manage your chronic conditions carefully during illness.")
        if mood == "Anxious":
            st.info("🔹 Try breathing exercises or mindfulness apps.")

        if sleep_hours < 6:
            st.info("🔹 Aim for 7–8 hours of quality sleep to recover well.")

        # Location-based suggestion
        if location != "Select":
            st.markdown(f"🏥 Nearest urgent care in **{location}**: *City Health Center, open till 10 PM.*")

        # Mental Health Tip (Static choice from 3)
        st.markdown("## 🧠 Mental Wellness Tip")
        if mood == "Calm":
            st.info("Keep it up! Maybe share your positivity with someone else today.")
        elif mood == "Sad":
            st.info("Take a short walk, call a friend, or write down 3 things you're grateful for.")
        elif mood == "Anxious":
            st.info("Try box breathing: 4 sec in, hold 4, out 4, hold 4 — repeat 3x.")
        elif mood == "Irritable":
            st.info("Take 10 minutes for yourself. Music, meditation, or even silence can help.")

        st.markdown("---")
        st.success(f"✅ Thank you {name} for using QuickHealth Pro Max. Get well soon! 💙")
