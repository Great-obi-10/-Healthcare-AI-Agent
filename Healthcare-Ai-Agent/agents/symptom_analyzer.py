def analyze_symptoms(text: str):
    """
    Simple NLP-like symptom extractor
    """
    text = text.lower()

    symptoms_list = ["fever", "headache", "fatigue", "cough", "pain", "nausea"]

    extracted = [symptom for symptom in symptoms_list if symptom in text]

    return extracted