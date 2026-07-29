from crewai import Task
from agents import (
    symptom_analyzer,
    risk_assessor,
    emergency_detector,
    care_advisor
)


def create_tasks(patient_data):

    patient_info = f"""
Patient Name: {patient_data['name']}
Age: {patient_data['age']}
Gender: {patient_data['gender']}

Symptoms:
{patient_data['symptoms']}
"""

    symptom_task = Task(
        description=f"""
Analyze the following patient information.

{patient_info}

Your responsibilities:
- Identify all symptoms.
- Identify symptom duration.
- Mention possible medical conditions.
- Write a structured symptom summary.

Do not provide treatment.
""",

        expected_output="""
Symptom Analysis

Detected Symptoms:

Duration:

Possible Conditions:
""",

        agent=symptom_analyzer
    )

    risk_task = Task(
        description=f"""
Review the patient's symptoms.

{patient_info}

Determine:
- Risk Level (Low / Medium / High)
- Explain why.
- Mention warning signs to monitor.
""",

        expected_output="""
Risk Assessment

Risk Level:
Low / Medium / High

Reason:

Warning Signs:
""",

        agent=risk_assessor
    )

    emergency_task = Task(
        description=f"""
Review the patient's symptoms.

{patient_info}

Decide whether this is an emergency.

If emergency:
Explain why.

Otherwise state:
No immediate emergency detected.
""",

        expected_output="""
Emergency Assessment

Emergency:
YES or NO

Reason:
""",

        agent=emergency_detector
    )

    care_task = Task(
        description=f"""
Using the patient's symptoms, provide safe healthcare guidance.

{patient_info}

Include:
- Home Care
- Doctor Consultation
- Emergency Precautions
- Lifestyle Advice

Important Rules:
- Never prescribe medicines.
- Never mention medicine names.
- Recommend consulting a doctor before taking medication.
- End with a short medical disclaimer.
""",

        expected_output="""
Healthcare Guidance

Home Care

Doctor Consultation

Emergency Advice

Lifestyle Advice

Medical Disclaimer
""",

        agent=care_advisor
    )

    return [
        symptom_task,
        risk_task,
        emergency_task,
        care_task
    ]