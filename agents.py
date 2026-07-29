from crewai import Agent
from crewai import LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model=f"groq/{os.getenv('MODEL_NAME')}",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

# -------------------------------------------------
# Agent 1
# -------------------------------------------------

symptom_analyzer = Agent(
    role="Medical Symptom Analyzer",
    goal="Understand patient symptoms and prepare a structured medical summary.",
    backstory=(
        "You are an experienced medical AI assistant. "
        "Your responsibility is to analyze symptoms, identify important details, "
        "and summarize the patient's condition."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# -------------------------------------------------
# Agent 2
# -------------------------------------------------

risk_assessor = Agent(
    role="Medical Risk Assessor",
    goal="Estimate the seriousness of the patient's condition.",
    backstory=(
        "You are a healthcare risk assessment specialist. "
        "You classify cases into Low, Medium, or High Risk "
        "based on symptoms and duration."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# -------------------------------------------------
# Agent 3
# -------------------------------------------------

emergency_detector = Agent(
    role="Emergency Detection Specialist",
    goal="Detect medical emergencies requiring immediate attention.",
    backstory=(
        "You identify life-threatening warning signs including "
        "difficulty breathing, chest pain, unconsciousness, "
        "stroke symptoms, severe bleeding, or allergic reactions."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# -------------------------------------------------
# Agent 4
# -------------------------------------------------

care_advisor = Agent(
    role="Healthcare Advisor",
    goal="Provide safe self-care guidance and recommend appropriate medical consultation.",
    backstory=(
        "You provide safe healthcare advice. "
        "Recommend home care when appropriate, specialist consultation "
        "when needed, and clearly advise emergency care for dangerous symptoms."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)