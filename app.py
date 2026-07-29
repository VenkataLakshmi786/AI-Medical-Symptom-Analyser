import streamlit as st
from parser import create_patient_data
from crew import run_medical_crew
from pdf_generator import create_pdf

st.set_page_config(
    page_title="AI Medical Symptom Checker",
    page_icon="🏥",
    layout="wide"
)

# ==================================================
# Header
# ==================================================

st.title("🏥 AI Medical Symptom Analyser Report")

st.caption(
    "Multi-Agent AI Healthcare Assistant using CrewAI"
)

st.write(
    "Describe your symptoms and receive an AI-generated medical assessment "
    "using a Multi-Agent CrewAI system."
)

st.warning(
    "⚠️ This application provides AI-generated health guidance only. "
    "It is **not** a substitute for professional medical advice. "
    "In case of a medical emergency, contact your nearest hospital immediately."
)

st.divider()

# ==================================================
# Patient Information
# ==================================================

st.subheader("👤 Patient Information")

col1, col2 = st.columns(2)

with col1:

    patient_name = st.text_input(
        "Patient Name"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=25
    )

with col2:

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
            "Other"
        ]
    )

# ==================================================
# Symptoms
# ==================================================

st.subheader("📝 Describe Your Symptoms")

symptoms = st.text_area(
    "Symptoms",
    height=180,
    placeholder="""
Example:
• Fever for 3 days
• Dry cough
• Body pain
• Sore throat
• Headache
"""
)

# ==================================================
# Analyze Button
# ==================================================

analyze = st.button(
    "🔍 Analyze Symptoms",
    use_container_width=True
)

# ==================================================
# Analysis
# ==================================================

if analyze:

    if not patient_name.strip():

        st.error("Please enter the patient name.")

    elif not symptoms.strip():

        st.error("Please describe your symptoms.")

    else:

        patient_data = create_patient_data(
            patient_name,
            age,
            gender,
            symptoms
        )

        with st.spinner("🤖 AI Medical Team is analyzing the symptoms..."):

            report = run_medical_crew(patient_data)

        st.success("✅ Analysis Completed!")

        st.divider()

        # ==========================================
        # Patient Summary
        # ==========================================

        st.subheader("📋 Patient Summary")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Patient", patient_name)

        with c2:
            st.metric("Age", age)

        with c3:
            st.metric("Gender", gender)

        with st.expander("📝 Symptoms Entered", expanded=True):
            st.write(symptoms)

        st.divider()

        # ==========================================
        # AI Report
        # ==========================================

        st.subheader("🤖 AI Medical Report")

        with st.container(border=True):
            st.markdown(report)

        st.divider()

        # ==========================================
        # PDF Download
        # ==========================================

        pdf_file = create_pdf(
            patient_data,
            report
        )

        with open(pdf_file, "rb") as pdf:

            st.download_button(
                label="📄 Download Medical Report",
                data=pdf,
                file_name="Medical_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        st.success("📄 Medical Report generated successfully!")

        st.divider()

        # ==========================================
        # Upcoming Features
        # ==========================================

        st.info(
            """
🚀 Upcoming Features

• Hospital Recommendations

• Medical Chat History

• Medicine Advisory

• Voice Input

• Multilingual Support

• Medical Knowledge Base

• User Login & Report History
"""
        )

# ==================================================
# Footer
# ==================================================

st.divider()

st.caption(
    "🏥 AI Medical Symptom Checker v1.0\n\n"
    "Developed using Streamlit • CrewAI • Groq LLM"
)