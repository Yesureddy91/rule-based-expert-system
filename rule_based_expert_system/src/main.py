from rules import RULES
from interface_engine import forward_chaining
from utilis import get_user_facts


def main():
    facts = get_user_facts()
    results = forward_chaining(facts, RULES)

    print("\n--- Expert System Result ---")

    if results:
        print("Possible Diagnosis:")
        for diagnosis in results:
            print(f"- {diagnosis}")
    else:
        print("No diagnosis found. Please consult a doctor.")


if __name__ == "__main__":
    main()
