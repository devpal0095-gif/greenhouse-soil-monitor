
from soil_moisture_monitor import classify_moisture
from soil_temperature_monitor import classify_temperature
from data_storage import save_crop_data, load_crop_data, append_crop_data

from datetime import datetime
import math

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

def get_valid_crop_name():

    while True:
        crop_name = input("Enter crop name: ").strip()

        if crop_name:
            return crop_name

        print("Crop name cannot be empty.")

def get_valid_crop_count():

        while True:
            try:
                number_of_crops = int(input("How many crops do you want to monitor? "))
                
                if number_of_crops >= 1:
                    
                    return number_of_crops
                
                print("Please enter at least one crop.")

            except ValueError:
                print("Please enter a valid whole number.")

def get_valid_sensor_reading(prompt, minimum, maximum):

    while True:
        try:
            value = float(input(prompt))

            if math.isfinite(value) and minimum <= value <= maximum:
                return value

            print(f"Please enter a finite number between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input. Please enter a number.")

def collect_crop_data():

    greenhouse_crops = []

    # number_of_crops = int(input("How many crops do you want to monitor? "))

    number_of_crops = get_valid_crop_count()

    for i in range(number_of_crops):
        print(f"\n--- Enter Crop{i + 1} Information---")
        crop_name = get_valid_crop_name()
        moisture = get_valid_sensor_reading("Enter soil moisture (%)", 0, 100)
        temperature = get_valid_sensor_reading("Enter soil temperature (°C)", -50, 80)

        # Create a new record with a timestamp
        crop = {
            "timestamp": get_timestamp(),
            "name": crop_name,
            "moisture": moisture,
            "temperature": temperature
        }

        # Save the reading to historical CSV
        append_crop_data(crop)

        # Keep the crop data for the current monitoring session
       
        greenhouse_crops.append({
            "name": crop_name,
            "moisture": moisture,
            "temperature": temperature
        })

    return greenhouse_crops

def get_timestamp():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timestamp

def calculate_average_moisture(readings):
    if not readings:
        return None

    return sum(readings) / len(readings)


if __name__ == "__main__":

    print("=== Greenhouse Soil Monitoring System ===")

     # Step 1: Collect new readings
    greenhouse_crops = collect_crop_data()

    # Step 2: Save readings to CSV
    save_crop_data(greenhouse_crops)

    # Step 3: Load readings from CSV
    saved_crops = load_crop_data()

    moisture_readings = [
        crop["moisture"] for crop in saved_crops
    ]

    average_moisture = calculate_average_moisture(moisture_readings)

    
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
    print(f"Total crops monitored: {len(saved_crops)}")
    print(f"Crops requiring attention: {alert_count}")

    if lowest_moisture_crop is not None:
        print(f"Crop with lowest moisture: {lowest_moisture_crop}")
        print(f"Moisture: {lowest_moisture}%")
    else:
        print("No valid moisture readings found.")

    if average_moisture is not None:
        print(f"Average moisture: {average_moisture:.2f}%")
    else:
        print("No moisture readings available.")

    
    
