
from soil_moisture_monitor import classify_moisture
from soil_temperature_monitor import classify_temperature
from data_storage import save_crop_data, load_crop_data


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

def collect_crop_data():

    greenhouse_crops = []

    number_of_crops = int(input("How many crops do you want to monitor? "))

    for i in range(number_of_crops):
        print(f"\n--- Enter Crop{i + 1} Information---")
        crop_name = input("Enter crop name: ").strip()
        moisture = float(input("Enter soil moisture (%): "))
        temperature = float(input("Enter soil temperature (°C): "))

        crop = {
            "name": crop_name,
            "moisture": moisture,
            "temperature": temperature
        }

        greenhouse_crops.append(crop)

    return greenhouse_crops


if __name__ == "__main__":

    print("=== Greenhouse Soil Monitoring System ===")

     # Step 1: Collect new readings
    greenhouse_crops = collect_crop_data()

    # Step 2: Save readings to CSV
    save_crop_data(greenhouse_crops)

    # Step 3: Load readings from CSV
    saved_crops = load_crop_data()

    print("\nCrop data loaded successfully!")

    alert_count = 0
    lowest_moisture = None
    lowest_moisture_crop = None
    
    # Step 4: Analyze loaded crop records
    for crop in saved_crops:

        display_crop_report(
            crop["name"],
            crop["moisture"],
            crop["temperature"]
        )

        moisture = crop["moisture"]

        moisture_status = classify_moisture(moisture)
        temperature_status = classify_temperature(crop["temperature"])

        # Count crops requiring attention
        if moisture_status != "MODERATE" or temperature_status != "MODERATE":
            alert_count += 1

        # Find lowest valid moisture
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
    
    
