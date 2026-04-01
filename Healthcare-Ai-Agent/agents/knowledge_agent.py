def map_symptoms_to_conditions(symptoms):
    """
    Maps symptoms to possible conditions
    """

    knowledge_base = {
        "fever": ["Flu", "Malaria"],
        "headache": ["Migraine", "Stress"],
        "cough": ["Cold", "Flu"],
        "fatigue": ["Anemia", "Infection"],
        "pain": ["Injury", "Inflammation"],
    }

    conditions = set()

    for symptom in symptoms:
        if symptom in knowledge_base:
            conditions.update(knowledge_base[symptom])

    return list(conditions)