def create_patient_data(name, age, gender, symptoms):
    """
    Creates a structured patient data dictionary
    for the CrewAI medical workflow.
    """

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "symptoms": symptoms
    }