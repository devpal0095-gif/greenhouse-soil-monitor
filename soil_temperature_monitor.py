
print("=== Greenhouse Soil Temperature Monitor ===")

crop_name = input("Enter crop name: ").strip()
soil_temperature = float(input("Enter soil temperature (°C): "))

print("\n--- Soil Temperature Report ---")

if not crop_name:
    print("Error: Crop name cannot be empty.")

elif soil_temperature < -50 or soil_temperature > 80:
    print("Error: Invalid soil temperature reading.")

else:
    print(f"Crop: {crop_name}")
    print(f"Soil temperature: {soil_temperature:.2f}°C")

    if soil_temperature < 15:
        print("Status: LOW TEMPERATURE")
        print("Result: Below the example temperature range.")

    elif soil_temperature <= 30:
        print("Status: MODERATE TEMPERATURE")
        print("Result: Within the example temperature range.")

    else:
        print("Status: HIGH TEMPERATURE")
        print("Result: Above the example temperature range.")

print("\n=== Monitoring Complete ===")
