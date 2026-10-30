
from soil_moisture_monitor import classify_moisture
from soil_temperature_monitor import classify_temperature


print("=== Greenhouse Soil Monitoring System ===")

crop_name = input("Enter crop name: ").strip()
moisture = float(input("Enter soil moisture (%): "))
temperature = float(input("Enter soil temperature (°C): "))

def display_crop_report(crop_name, moisture, temperature):
    
    moisture_status = classify_moisture(moisture)
    temperature_status = classify_temperature(temperature)

    print("\n--- Monitoring Report ---")

    if not crop_name:
        print("Error: Crop name cannot be empty.")
    elif moisture_status == "INVALID" or temperature_status == "INVALID":
        print("Error: Invalid sensor reading.")
    else:
        print(f"Crop: {crop_name}")
        print(f"Soil moisture: {moisture:.2f}%")
        print(f"Soil temperature: {temperature:.2f}°C")
        print(f"Moisture status: {moisture_status}")
        print(f"Temperature status: {temperature_status}")

        if moisture_status == "MODERATE" and temperature_status == "MODERATE":
            print("Result: Both readings are within example ranges.")
        else:
            print("Result: One or more readings are outside example ranges.")
display_crop_report(crop_name, moisture, temperature)

