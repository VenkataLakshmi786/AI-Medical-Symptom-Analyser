from crewai import Crew, Process

from agents import (
    symptom_analyzer,
    risk_assessor,
    emergency_detector,
    care_advisor
)

from tasks import create_tasks


def run_medical_crew(patient_data):

    tasks = create_tasks(patient_data)

    medical_crew = Crew(
        agents=[
            symptom_analyzer,
            risk_assessor,
            emergency_detector,
            care_advisor
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = medical_crew.kickoff()

    return str(result)