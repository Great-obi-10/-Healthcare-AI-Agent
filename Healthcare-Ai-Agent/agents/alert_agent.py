def trigger_alert(risk):
    """
    Simulate alert system
    """

    if risk["risk_level"] == "High":
        return "🚨 ALERT: Immediate medical attention recommended!"
    
    return None