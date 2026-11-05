
def classify_temperature(temperature):
    if temperature < -50 or temperature > 80:
        return "INVALID"
    elif temperature < 15:
        return "LOW"
    elif temperature <= 30:
        return "MODERATE"
    else:
        return "HIGH"
