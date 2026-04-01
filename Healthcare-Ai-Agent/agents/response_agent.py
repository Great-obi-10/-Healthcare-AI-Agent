def generate_response(symptoms, conditions, risk):
    """
    Generate user-friendly response
    """

    return {
        "symptoms_detected": symptoms,
        "possible_conditions": conditions,
        "risk_level": risk["risk_level"],
        "confidence": f"{int(risk['score'] * 100)}%",
        "advice": generate_advice(risk["risk_level"])
    }


def generate_advice(risk_level):
    if risk_level == "Low":
        return "Symptoms appear mild. Rest and monitor."
    elif risk_level == "Medium":
        return "Monitor symptoms closely. Consider consulting a doctor."
    else:
        return "High risk detected. Seek medical attention immediately."