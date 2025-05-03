# 🩺 QuickHealth Pro Max – Python Project 2

## 📚 Project Overview

This is a beginner-level terminal-based Python project designed to simulate a health checker application using only fundamental Python concepts.

You’ll build a command-line tool that:

1. Takes user inputs step-by-step

2. Performs manual validations

3. Processes the data using simple if/elif/else logic

4.Calculates a health risk score

5. Displays personalized health advice

🚫 Important Rule: You are not allowed to use loops, functions, lists, or exception handling in this project.

## 🧠 Required Features

You must implement the following logic and features in your script:

### 👤 1. User Profile
Collect:
- Name
- Age (must be numeric)
- Gender (only male, female, or other)
- City (any string)

### 🤒 2. Health Inputs
Ask the user for:
- Main symptom (choose from: fever, cough, fatigue, headache, chest pain, breathlessness)
- Body temperature in Fahrenheit (must be a valid number)
- Number of sick days (numeric)
- Smoking habit (yes/no)
- Sleep hours (numeric)
- Mood (choose from: calm, anxious, sad, irritable)
- Pre-existing conditions (yes/no)

### ⚙️ 3. Risk Scoring Logic

Assign points using `if` conditions:

| Condition                             | Points |
|--------------------------------------|--------|
| Fever ≥ 102°F or sick > 3 days       | +3     |
| Age ≥ 60 with fever                  | +2     |
| Cough ≥ 5 days                       | +2     |
| Fatigue (age > 30)                   | +2     |
| Headache with temp > 100°F           | +2     |
| Chest pain                           | +3     |
| Breathlessness                       | +4     |
| Smoker                               | +2     |
| Sleep < 6 hrs                        | +1     |
| Mood = anxious/sad/irritable         | +1     |
| Pre-existing conditions = yes        | +2     |

---

### 📊 4. Health Risk Result

Based on total score, print a health warning:

- `0–3` → 🟢 Low Risk  
- `4–6` → 🟠 Moderate Risk  
- `7+` → 🔴 High Risk

---

### 🩺 5. Personalized Advice

Use `if` conditions to offer personalized suggestions:

- Female and age ≥ 45 → recommend health screening
- Male and smoker → suggest quitting smoking
- Sleep < 6 → suggest getting more rest
- Mood = anxious → suggest relaxation/breathing
- Pre-existing conditions → suggest medical attention
- Always mention nearest urgent care in their city

---

### 🧘 6. Mental Health Tip

Based on mood:
- Calm → Encourage positivity
- Sad → Suggest talking to someone
- Anxious → Teach box breathing
- Irritable → Suggest taking a break

---

## 🚀 How to Run This App

### Step 1: Save the script
Save the file as `quickhealth.py`.

### Step 2: Open terminal or command prompt.

### Step 3: Run the scripts.
```bash
python quickhealth.py
