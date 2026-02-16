def forward_chaining(facts, rules):
    conclusions = []

    for rule in rules:
        if all(condition in facts for condition in rule["if"]):
            conclusions.append(rule["then"])

    return conclusions
