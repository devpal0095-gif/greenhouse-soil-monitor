
def classify_moisture(moisture):
    if moisture < 0 or moisture > 100:
        return "INVALID"
    elif moisture < 30:
        return "LOW"
    elif moisture <= 70:
        return "MODERATE"
    else:
        return "HIGH"


if __name__ == "__main__":
    moisture = float(input("Enter soil moisture (%): "))
    status = classify_moisture(moisture)
    print(f"Moisture status: {status}")
