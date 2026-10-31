
from soil_moisture_monitor import classify_moisture
from soil_temperature_monitor import classify_temperature


def display_crop_report(crop_name, moisture, temperature):

    moisture_status = classify_moisture(moisture)
    temperature_status = classify_temperature(temperature)

    if not crop_name:
        print("Error: Crop name cannot be empty.")
        return

    print(f"\n--- {crop_name} Monitoring Report ---")
    print(f"Moisture: {moisture}% ({moisture_status})")
    print(f"Temperature: {temperature}°C ({temperature_status})")

    if moisture_status == "INVALID" or temperature_status == "INVALID":
        print("Error: Invalid sensor reading.")
    elif moisture_status == "MODERATE" and temperature_status == "MODERATE":
        print("Result: Both readings are within example ranges.")
    else:
        print("Result: One or more readings are outside example ranges.")


greenhouse_crops = [
    {"name": "Tomato", "moisture": 45, "temperature": 22},
    {"name": "Pepper", "moisture": 25, "temperature": 28},
    {"name": "Cucumber", "moisture": 75, "temperature": 20},
    {"name": "Lettuce", "moisture": 25, "temperature": 28},
    {"name": "Strawberry", "moisture": 75, "temperature": 20}
]


if __name__ == "__main__":

    print("=== Greenhouse Soil Monitoring System ===")

    alert_count = 0
    lowest_moisture = None
    lowest_moisture_crop = None

    for crop in greenhouse_crops:

        display_crop_report(
            crop["name"],
            crop["moisture"],
            crop["temperature"]
        )

        moisture = crop["moisture"]

        moisture_status = classify_moisture(moisture)
        temperature_status = classify_temperature(crop["temperature"])

        # Challenge B: Count crops requiring attention
        if moisture_status != "MODERATE" or temperature_status != "MODERATE":
            alert_count += 1

        # Challenge C: Find lowest valid moisture
        if moisture_status != "INVALID":
            if lowest_moisture is None or moisture < lowest_moisture:
                lowest_moisture = moisture
                lowest_moisture_crop = crop["name"]

    # Final monitoring summary
    print("\n=== Greenhouse Summary ===")
    print(f"Total crops monitored: {len(greenhouse_crops)}")
    print(f"Crops requiring attention: {alert_count}")

    if lowest_moisture_crop is not None:
        print(f"Crop with lowest moisture: {lowest_moisture_crop}")
        print(f"Moisture: {lowest_moisture}%")
    else:
        print("No valid moisture readings found.")
