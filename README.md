# 🏥 AI Medical Symptom Analyser

An AI-powered Medical Symptom Checker built using **CrewAI**, **Streamlit**, and **Groq LLM**. The application uses multiple AI agents to analyze patient symptoms, assess risk, detect emergencies, and provide safe healthcare guidance.

> **Disclaimer:** This project is for educational purposes only and should not be used as a substitute for professional medical advice.

---

# 📌 Features

- 👤 Patient Information Form
- 🤖 Multi-Agent AI Medical Analysis
- 🔍 Symptom Analysis
- ⚠️ Risk Assessment
- 🚑 Emergency Detection
- 🩺 Healthcare Guidance
- 📄 Downloadable PDF Medical Report
- 🎨 Clean Streamlit User Interface

---

# 🏗️ Project Architecture

```
Patient Input
      │
      ▼
Streamlit UI
      │
      ▼
CrewAI
 │
 ├── Symptom Analyzer Agent
 ├── Risk Assessment Agent
 ├── Emergency Detection Agent
 └── Care Advisor Agent
      │
      ▼
Medical Report
      │
      ├── Display on Screen
      └── Generate PDF
```

---

# 👨‍⚕️ AI Agents

## 1️⃣ Symptom Analyzer

Responsibilities:

- Identify symptoms
- Detect symptom duration
- Suggest possible medical conditions
- Generate symptom summary

---

## 2️⃣ Risk Assessment Agent

Responsibilities:

- Analyze severity
- Assign Risk Level
- Explain the reason
- Identify warning signs

---

## 3️⃣ Emergency Detection Agent

Responsibilities:

- Detect emergency situations
- Recommend immediate medical attention if required

---

## 4️⃣ Care Advisor Agent

Responsibilities:

- Home care guidance
- Doctor consultation advice
- Emergency precautions
- Lifestyle recommendations

---

# 🛠️ Technologies Used

- Python
- CrewAI
- Groq LLM
- Streamlit
- ReportLab
- LiteLLM

---

# 📂 Project Structure

```
AI Medical Symptom Checker/

│
├── app.py
├── agents.py
├── tasks.py
├── crew.py
├── parser.py
├── pdf_generator.py
├── requirements.txt
│
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Medical-Symptom-Checker.git
```

Move into the project

```bash
cd AI-Medical-Symptom-Checker
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```text
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📸 Screenshots

## Home Page


<img width="465" height="443" alt="Screenshot 2026-07-29 224051" src="https://github.com/user-attachments/assets/4a7b9ecf-366b-4116-a202-b2bce4683af2" />


---

## Patient Summary

<img width="465" height="443" alt="Screenshot 2026-07-29 224051" src="https://github.com/user-attachments/assets/f8267196-373b-4adf-9fdc-8cd92e5f5eab" />


---

## AI Medical Report

<img width="472" height="470" alt="Screenshot 2026-07-29 224331" src="https://github.com/user-attachments/assets/5af79d90-2fef-43dd-85e8-ac11be746ef1" />


---

## PDF Report

<img width="467" height="437" alt="Screenshot 2026-07-29 224351" src="https://github.com/user-attachments/assets/3f44f00a-7d3a-4838-ace0-ed1608e17e1e" />


---

# 📄 Sample Output

- Symptom Analysis
- Risk Assessment
- Emergency Detection
- Healthcare Guidance
- PDF Medical Report

---

# ⚠️ Disclaimer

This application is intended for educational and demonstration purposes only.

It does not diagnose, treat, cure, or prevent any disease.

Always consult a qualified healthcare professional for medical advice.

---

# 🌟 Future Improvements

- Medical Knowledge Base (RAG)
- Hospital Recommendation System
- Medicine Information
- Chat History
- User Authentication
- Voice Input
- Multilingual Support
- Medical Report Database

---
