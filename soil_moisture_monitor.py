
def classify_moisture(moisture):
    if moisture < 0 or moisture > 100:
        return "INVALID"
    elif moisture < 30:
        return "LOW"
    elif moisture <= 70:
        return "MODERATE"
    else:
        return "HIGH"

