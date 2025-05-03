import time

print("🩺 Welcome to QuickHealth Pro Max – Terminal Edition\n")
time.sleep(1)

# Step 1: User info
name = input("👤 Enter your name: ").strip()

gender = input("⚧️ Enter your gender (male/female/other): ").lower().strip()
if gender not in ["male", "female", "other"]:
    print("❌ Invalid gender. Exiting.")
    exit()

age_input = input("🎂 Enter your age: ")
if not age_input.isdigit():
    print("❌ Age must be a number. Exiting.")
    exit()
age = int(age_input)

city = input("📍 Enter your city (e.g., New York, Phoenix): ").strip()

# Step 2: Health info
print("\n🤒 Select your main symptom from the list below:")
print("Options: fever, cough, fatigue, headache, chest pain, breathlessness")
symptom = input("Main symptom: ").lower().strip()

temp_input = input("🌡️ Enter your body temperature (°F): ")
if "." in temp_input:
    temp_check = temp_input.replace(".", "", 1)
else:
    temp_check = temp_input
if not temp_check.isdigit():
    print("❌ Temperature must be a valid number. Exiting.")
    exit()
temp = float(temp_input)

days_input = input("📅 How many days have you felt unwell? ")
if not days_input.isdigit():
    print("❌ Sick days must be a number. Exiting.")
    exit()
days = int(days_input)

smoker = input("🚬 Do you smoke? (yes/no): ").lower().strip()
if smoker not in ["yes", "no"]:
    print("❌ Invalid input for smoking. Exiting.")
    exit()

sleep_input = input("🛌 Hours of sleep last night: ")
if not sleep_input.isdigit():
    print("❌ Sleep hours must be a number. Exiting.")
    exit()
sleep_hours = int(sleep_input)

print("🧠 Current mood options: calm, anxious, sad, irritable")
mood = input("Your current mood: ").lower().strip()

conditions = input("❗ Do you have any pre-existing conditions (yes/no)? ").lower().strip()
if conditions not in ["yes", "no"]:
    print("❌ Invalid input. Exiting.")
    exit()

# Step 3: Simulated analysis
print("\n🔍 Processing your inputs...")
time.sleep(2)

# Step 4: Risk calculation
risk_score = 0

if symptom == "fever":
    if temp >= 102 or days > 3:
        risk_score += 3
    elif age >= 60:
        risk_score += 2
    else:
        risk_score += 1
elif symptom == "cough":
    if days >= 5:
        risk_score += 2
    else:
        risk_score += 1
elif symptom == "fatigue":
    if age > 30:
        risk_score += 2
    else:
        risk_score += 1
elif symptom == "headache":
    if temp > 100:
        risk_score += 2
    else:
        risk_score += 1
elif symptom == "chest pain":
    risk_score += 3
elif symptom == "breathlessness":
    risk_score += 4
else:
    print("❓ Symptom not recognized. Using general assessment.")
    risk_score += 1

# Lifestyle additions
if smoker == "yes":
    risk_score += 2
if sleep_hours < 6:
    risk_score += 1
if mood in ["anxious", "sad", "irritable"]:
    risk_score += 1
if conditions == "yes":
    risk_score += 2

# Step 5: Output Results
print("\n🧾 Health Summary for", name + ":")

if risk_score >= 7:
    print("🔴 High risk! Please consult a healthcare provider immediately.")
elif risk_score >= 4:
    print("🟠 Moderate risk. Monitor your symptoms and seek advice if needed.")
else:
    print("🟢 Low risk. You seem fine. Rest, hydrate, and check again in a day or two.")

# Step 6: Personalized Advice
print("\n📌 Personalized Recommendations:")

if gender == "female" and age >= 45:
    print("- Consider scheduling regular health screenings.")
if gender == "male" and smoker == "yes":
    print("- Quitting smoking can reduce long-term health risks.")
if conditions == "yes":
    print("- Manage chronic conditions carefully during illness.")
if mood == "anxious":
    print("- Try deep breathing or a short walk to relax.")
if sleep_hours < 6:
    print("- Aim for at least 7 hours of sleep for better recovery.")
print("- If you're in", city + ", the nearest urgent care is open till 10 PM.")

# Final Tip
print("\n🧠 Mental Health Tip:")
if mood == "calm":
    print("Keep it up! Share your positivity with others.")
elif mood == "sad":
    print("Talk to someone you trust. You're not alone.")
elif mood == "anxious":
    print("Try box breathing: inhale 4s, hold 4s, exhale 4s, hold 4s.")
elif mood == "irritable":
    print("Take a 10-minute break. Silence, music, or nature can help.")

# End
time.sleep(1)
print("\n✅ Thank you for using QuickHealth Pro Max,", name + "!")
print("Stay safe and take care. 💙")
