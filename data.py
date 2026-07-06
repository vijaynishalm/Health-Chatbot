symptom_conditions = {
    "headache": {
        "conditions": ["Migraine", "Dehydration", "Tension headache"],
        "severity": "common",
        "urgency": 3,
        "follow_up": "Do you also feel nausea or blurred vision?",
        "refinements": {
            "yes": ["Migraine"],
            "no": ["Dehydration", "Tension headache"]
        }
    },
    "dizziness": {
        "conditions": ["Vertigo", "Low blood pressure", "Inner ear infection"],
        "severity": "critical",
        "urgency": 7,
        "follow_up": "Is it constant or triggered by movement?",
        "refinements": {
            "yes": ["Vertigo", "Low blood pressure"],
            "no": ["Inner ear infection"]
        }
    },
    "chest pain": {
        "conditions": ["Heart attack", "Anxiety", "Acid reflux"],
        "severity": "very critical",
        "urgency": 9,
        "follow_up": "Is the pain sharp, dull, or radiating to your arm?",
        "refinements": {
            "yes": ["Heart attack"],
            "no": ["Anxiety", "Acid reflux"]
        }
    },
    "fever": {
        "conditions": ["Infection", "Influenza", "COVID-19"],
        "severity": "common",
        "urgency": 4,
        "follow_up": "Is it accompanied by chills or body aches?",
        "refinements": {
            "yes": ["Influenza", "COVID-19"],
            "no": ["Infection"]
        }
    },
    "nausea": {
        "conditions": ["Food poisoning", "Pregnancy", "Migraine"],
        "severity": "common",
        "urgency": 3,
        "follow_up": "Did it start after eating or waking up?",
        "refinements": {
            "yes": ["Food poisoning", "Pregnancy"],
            "no": ["Migraine"]
        }
    },
    "shortness of breath": {
        "conditions": ["Asthma", "Heart disease", "Pulmonary embolism"],
        "severity": "very critical",
        "urgency": 9,
        "follow_up": "Is it triggered by exertion or constant?",
        "refinements": {
            "yes": ["Heart disease", "Pulmonary embolism"],
            "no": ["Asthma"]
        }
    },
    "abdominal pain": {
        "conditions": ["Appendicitis", "Gallstones", "Irritable bowel syndrome"],
        "severity": "critical",
        "urgency": 7,
        "follow_up": "Is the pain sharp and localized?",
        "refinements": {
            "yes": ["Appendicitis", "Gallstones"],
            "no": ["Irritable bowel syndrome"]
        }
    },
    "sore throat": {
        "conditions": ["Strep throat", "Common cold", "Tonsillitis"],
        "severity": "common",
        "urgency": 3,
        "follow_up": "Is it painful to swallow?",
        "refinements": {
            "yes": ["Strep throat", "Tonsillitis"],
            "no": ["Common cold"]
        }
    },
    "fatigue": {
        "conditions": ["Anemia", "Insomnia", "Chronic fatigue syndrome", "Diabetes"],
        "severity": "common",
        "urgency": 4,
        "follow_up": "Is it persistent despite rest?",
        "refinements": {
            "yes": ["Chronic fatigue syndrome", "Diabetes"],
            "no": ["Insomnia", "Anemia"]
        }
    },
    "cough": {
        "conditions": ["Bronchitis", "Pneumonia", "Allergies", "Asthma", "COPD"],
        "severity": "common",
        "urgency": 5,
        "follow_up": "Is it dry or productive?",
        "refinements": {
            "yes": ["Bronchitis", "Pneumonia", "COPD"],
            "no": ["Allergies", "Asthma"]
        }
    },
    "skin rash": {
        "conditions": ["Allergic reaction", "Eczema", "Measles"],
        "severity": "common",
        "urgency": 4,
        "follow_up": "Is it itchy or spreading?",
        "refinements": {
            "yes": ["Allergic reaction", "Measles"],
            "no": ["Eczema"]
        }
    },
    "joint pain": {
        "conditions": ["Arthritis", "Lupus", "Fibromyalgia"],
        "severity": "common",
        "urgency": 4,
        "follow_up": "Is it worse in the morning?",
        "refinements": {
            "yes": ["Arthritis", "Fibromyalgia"],
            "no": ["Lupus"]
        }
    },
    "frequent urination": {
        "conditions": ["Diabetes", "Urinary tract infection", "Kidney disease"],
        "severity": "critical",
        "urgency": 7,
        "follow_up": "Is it painful or accompanied by thirst?",
        "refinements": {
            "yes": ["Diabetes", "Urinary tract infection"],
            "no": ["Kidney disease"]
        }
    },
    "blurry vision": {
        "conditions": ["Diabetes", "Cataracts", "Migraine"],
        "severity": "critical",
        "urgency": 6,
        "follow_up": "Is it sudden or gradual?",
        "refinements": {
            "yes": ["Migraine", "Diabetes"],
            "no": ["Cataracts"]
        }
    },
    "wheezing": {
        "conditions": ["Asthma", "COPD", "Allergies"],
        "severity": "critical",
        "urgency": 6,
        "follow_up": "Is it triggered by exercise or allergens?",
        "refinements": {
            "yes": ["Asthma", "Allergies"],
            "no": ["COPD"]
        }
    },
    "persistent thirst": {
        "conditions": ["Diabetes", "Dehydration"],
        "severity": "critical",
        "urgency": 6,
        "follow_up": "Is it accompanied by frequent urination?",
        "refinements": {
            "yes": ["Diabetes"],
            "no": ["Dehydration"]
        }
    },
    "back pain": {
        "conditions": ["Muscle strain", "Herniated disc", "Kidney infection"],
        "severity": "common",
        "urgency": 5,
        "follow_up": "Is the pain radiating to the leg?",
        "refinements": {
            "yes": ["Herniated disc"],
            "no": ["Muscle strain", "Kidney infection"]
        }
    },
    "palpitations": {
        "conditions": ["Anxiety", "Arrhythmia", "Hyperthyroidism"],
        "severity": "critical",
        "urgency": 6,
        "follow_up": "Is it associated with chest pain or fainting?",
        "refinements": {
            "yes": ["Arrhythmia"],
            "no": ["Anxiety", "Hyperthyroidism"]
        }
    },
    "swelling of legs": {
        "conditions": ["Heart failure", "Deep vein thrombosis", "Kidney disease"],
        "severity": "critical",
        "urgency": 7,
        "follow_up": "Is it sudden and painful?",
        "refinements": {
            "yes": ["Deep vein thrombosis", "Heart failure"],
            "no": ["Kidney disease"]
        }
    },
    "vomiting": {
        "conditions": ["Gastroenteritis", "Migraine", "Food poisoning"],
        "severity": "common",
        "urgency": 4,
        "follow_up": "Is it accompanied by fever or diarrhea?",
        "refinements": {
            "yes": ["Gastroenteritis", "Food poisoning"],
            "no": ["Migraine"]
        }
    },
    "night sweats": {
        "conditions": ["Tuberculosis", "Menopause", "Cancer"],
        "severity": "critical",
        "urgency": 7,
        "follow_up": "Has there been weight loss as well?",
        "refinements": {
            "yes": ["Cancer", "Tuberculosis"],
            "no": ["Menopause"]
        }
    },
    "unintentional weight loss": {
        "conditions": ["Cancer", "Diabetes", "Hyperthyroidism"],
        "severity": "critical",
        "urgency": 7,
        "follow_up": "Is your appetite increased or decreased?",
        "refinements": {
            "yes": ["Hyperthyroidism"],
            "no": ["Cancer", "Diabetes"]
        }
    },
    "loss of appetite": {
        "conditions": ["Infection", "Depression", "Cancer"],
        "severity": "common",
        "urgency": 4,
        "follow_up": "Is it accompanied by weight loss?",
        "refinements": {
            "yes": ["Cancer"],
            "no": ["Infection", "Depression"]
        }
    },
    "constipation": {
        "conditions": ["Irritable bowel syndrome", "Hypothyroidism", "Colon cancer"],
        "severity": "common",
        "urgency": 4,
        "follow_up": "Is it accompanied by blood in stools?",
        "refinements": {
            "yes": ["Colon cancer"],
            "no": ["Irritable bowel syndrome", "Hypothyroidism"]
        }
    },
    "diarrhea": {
        "conditions": ["Gastroenteritis", "Food allergy", "Inflammatory bowel disease"],
        "severity": "common",
        "urgency": 5,
        "follow_up": "Is there any blood in the stool?",
        "refinements": {
            "yes": ["Inflammatory bowel disease"],
            "no": ["Gastroenteritis", "Food allergy"]
        }
    },
    "easy bruising": {
        "conditions": ["Liver disease", "Platelet disorder", "Leukemia"],
        "severity": "critical",
        "urgency": 7,
        "follow_up": "Are you also feeling weak or fatigued?",
        "refinements": {
            "yes": ["Leukemia", "Liver disease"],
            "no": ["Platelet disorder"]
        }
    },
    "hair loss": {
        "conditions": ["Thyroid disorder", "Alopecia", "Nutrient deficiency"],
        "severity": "common",
        "urgency": 3,
        "follow_up": "Is it patchy or diffuse?",
        "refinements": {
            "yes": ["Alopecia"],
            "no": ["Thyroid disorder", "Nutrient deficiency"]
        }
    },
    "bloody sputum": {
        "conditions": ["Tuberculosis", "Lung cancer", "Bronchitis"],
        "severity": "very critical",
        "urgency": 9,
        "follow_up": "Is there chest pain as well?",
        "refinements": {
            "yes": ["Lung cancer", "Tuberculosis"],
            "no": ["Bronchitis"]
        }
    }
}
