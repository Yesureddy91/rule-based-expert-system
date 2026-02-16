RULES = [
    {
        "if": ["fever", "cough"],
        "then": "Viral Fever"
    },
    {
        "if": ["fever", "rash"],
        "then": "Measles"
    },
    {
        "if": ["headache", "nausea","cold"],
        "then": "Migraine"
    },
    {
        "if": ["chest pain", "shortness of breath"],
        "then": "Heart Disease"
    }
]
