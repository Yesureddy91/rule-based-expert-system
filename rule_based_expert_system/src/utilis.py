def get_user_facts():
    print("Enter symptoms separated by commas:")
    user_input = input("> ")
    
    facts = [
        symptom.strip().lower()
        for symptom in user_input.split(",")
    ]

    return facts
