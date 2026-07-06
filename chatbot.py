from data import symptom_conditions

# Keyword-based urgency boost map
urgency_keywords = {
    "blurred vision": 3,
    "nausea": 2,
    "vomiting": 3,
    "fainting": 4,
    "chest tightness": 4,
    "shortness of breath": 3,
    "yes": 2,
    "no": -1
}

def refine_conditions(symptom, follow_up_answer):
    info = symptom_conditions.get(symptom)
    base_urgency = info.get("urgency", 3)
    base_severity = info["severity"]
    answer = follow_up_answer.lower().strip()

    # Refine condition list
    refined_conditions = info["refinements"].get(answer, info["conditions"])

    # Keyword-based urgency boost
    urgency_boost = 0
    for keyword, boost in urgency_keywords.items():
        if keyword in answer:
            urgency_boost += boost

    refined_urgency = max(1, min(10, base_urgency + urgency_boost))
    refined_severity = "uncommon" if urgency_boost > 0 else base_severity

    return refined_conditions, refined_urgency, refined_severity

def analyze_symptoms(user_input, follow_up_answers=None):
    results = []

    for symptom, info in symptom_conditions.items():
        if symptom in user_input.lower():
            result = {
                "symptom": symptom,
                "initial_conditions": info["conditions"],
                "initial_severity": info["severity"],
                "initial_urgency": info["urgency"],
                "follow_up": info.get("follow_up", None),
                "answer": None,
                "refined_conditions": None,
                "refined_severity": None,
                "refined_urgency": None
            }

            if follow_up_answers and symptom in follow_up_answers:
                answer = follow_up_answers[symptom]
                refined, urgency, severity = refine_conditions(symptom, answer)
                result["answer"] = answer
                result["refined_conditions"] = refined
                result["refined_urgency"] = urgency
                result["refined_severity"] = severity

            results.append(result)

    return results