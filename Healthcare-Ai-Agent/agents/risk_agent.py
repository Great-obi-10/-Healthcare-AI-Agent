def calculate_risk(symptoms):
    """
    Assign risk level based on number of symptoms
    """

    score = len(symptoms) / 5  # simple scaling

    if score < 0.3:
        level = "Low"
    elif score < 0.7:
        level = "Medium"
    else:
        level = "High"

    return {
        "risk_level": level,
        "score": round(score, 2)
    }