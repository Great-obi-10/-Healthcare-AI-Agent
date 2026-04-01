🏥 Healthcare AI Agent

A Multi-Agent AI Healthcare Assistant built with Python and FastAPI that analyzes user symptoms, maps them to possible conditions, assigns a risk level, and provides safe, informational medical guidance.

📌 Overview

The Healthcare AI Agent is designed to simulate how multiple intelligent agents collaborate in a healthcare setting.
It allows users to input symptoms and receive structured insights such as possible conditions, risk level, and recommended next steps.

⚠️ Disclaimer: This system is for informational purposes only and does NOT provide medical diagnosis or replace professional healthcare advice.

🎯 Objectives
Provide quick and structured health insights
Reduce reliance on unreliable online searches
Demonstrate multi-agent AI system design
Build a scalable AI-powered healthcare assistant
⚙️ Tech Stack
Python 3.10+
FastAPI – API framework
Pydantic – Data validation
Uvicorn – ASGI server
HTML5 – Frontend structure
CSS3 – Styling
🧠 System Architecture

This project uses a multi-agent architecture, where each component performs a specific task:

🩺 Symptom Analyzer Agent
Extracts symptoms from user input text
📚 Knowledge Agent
Maps symptoms to possible medical conditions
⚠️ Risk Agent
Calculates risk level based on symptoms
💬 Response Agent
Generates structured, user-friendly responses
🚨 Alert Agent
Triggers alerts for high-risk cases
✨ Features
🤖 Multi-agent AI pipeline
📊 Risk scoring system (Low, Medium, High)
💬 Natural language symptom input
🚨 Alert system for critical cases
🧠 Session-based memory (basic)
⚡ FastAPI-powered REST API
🌐 Clean HTML & CSS frontend
📁 Project Structure
healthcare-ai-agent/
│
├── agents/
│   ├── symptom_analyzer.py
│   ├── knowledge_agent.py
│   ├── risk_agent.py
│   ├── response_agent.py
│   └── alert_agent.py
│
├── api/
│   └── main.py
│
├── data/
│   └── symptoms_dataset.csv
│
├── utils/
│   └── helpers.py
│
├── memory/
│   └── session_store.py
│
├── frontend/
│   ├── index.html
│   └── styles.css
│
├── requirements.txt
└── README.md
⚡ Installation
1. Clone the repository
git clone https://github.com/great-obi-10/healthcare-ai-agent.git
cd healthcare-ai-agent
2. Create virtual environment
python -m venv .venv
3. Activate environment

Windows

.\.venv\Scripts\activate

macOS/Linux

source .venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
🚀 Run the Application
uvicorn api.main:app --reload

Open in browser:

http://127.0.0.1:8000
📡 API Endpoints
🔹 Health Check
GET /

Response:

{
  "message": "Healthcare AI Agent is running"
}
🔹 Analyze Symptoms
POST /analyze-symptoms

Request:

{
  "text": "I have fever, headache and fatigue"
}

Response:

{
  "session_id": "12345",
  "data": {
    "symptoms_detected": ["fever", "headache", "fatigue"],
    "possible_conditions": ["Flu", "Malaria", "Migraine", "Anemia"],
    "risk_level": "Medium",
    "confidence": "60%",
    "advice": "Monitor symptoms closely. Consider consulting a doctor."
  },
  "alert": null
}
🧪 Testing the API

You can test using:

Swagger UI → http://127.0.0.1:8000/docs
Postman
cURL

Example:

curl -X POST "http://127.0.0.1:8000/analyze-symptoms" \
-H "Content-Type: application/json" \
-d '{"text":"I have fever and headache"}'
📊 Sample Dataset
symptom,condition
fever,Flu
fever,Malaria
cough,Cold
headache,Migraine
fatigue,Anemia
🚧 Development Note
Project is in testing/prototyping phase
Uses a small dataset for validation
Focused on learning system design and AI pipelines
Will be improved with larger datasets and advanced models
🔮 Future Improvements
🧠 Integrate LLMs (OpenAI / HuggingFace)
💬 Add conversational memory
📊 Build a full dashboard
🚨 Real-time alert system (SMS/Email)
☁️ Cloud deployment (Docker, AWS)
🔐 Authentication & security
👨‍💻 Author

Great Obi
AI & Machine Learning Developer | Cybersecurity Professional | Python Engineer

📜 License

This project is licensed under the MIT License.
