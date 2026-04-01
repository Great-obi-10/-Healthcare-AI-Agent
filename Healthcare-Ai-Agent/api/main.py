from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uuid
import os

from agents.symptom_analyzer import analyze_symptoms
from agents.knowledge_agent import map_symptoms_to_conditions
from agents.risk_agent import calculate_risk
from agents.response_agent import generate_response
from agents.alert_agent import trigger_alert

from memory.session_store import save_session

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# ✅ Mount ONLY for CSS (static assets)
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


class SymptomRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))


@app.post("/analyze-symptoms")
def analyze(request: SymptomRequest):

    session_id = str(uuid.uuid4())

    symptoms = analyze_symptoms(request.text)
    conditions = map_symptoms_to_conditions(symptoms)
    risk = calculate_risk(symptoms)
    response = generate_response(symptoms, conditions, risk)
    alert = trigger_alert(risk)

    save_session(session_id, response)

    return {
        "session_id": session_id,
        "data": response,
        "alert": alert
    }