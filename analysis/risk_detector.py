def detect_risks(structure):

    risks = []

    if structure["loops"] > 1:
        risks.append("performance")

    if structure["functions"] > 5:
        risks.append("maintainability")

    return risks
