
print("=== Greenhouse Soil Moisture Monitor ===")

crop_name = input("Enter crop name: ").strip()
soil_moisture = float(input("Enter soil moisture (%): "))
soil_temperature = float(input("Enter soil temperature (°C): "))

print("\n--- Soil Monitoring Report ---")

if not crop_name:
    print("Error: Crop name cannot be empty.")

elif soil_moisture < 0 or soil_moisture > 100:
    print("Error: Soil moisture must be between 0% and 100%.")

elif soil_temperature < -50 or soil_temperature > 80:
    print("Error: Soil temperature is outside the allowed range.")

else:
    print(f"Crop: {crop_name}")
    print(f"Soil moisture: {soil_moisture:.2f}%")
    print(f"Soil temperature: {soil_temperature:.2f}°C")

    # Soil moisture classification
    if soil_moisture < 30:
        print("Moisture status: LOW")
    elif soil_moisture <= 70:
        print("Moisture status: MODERATE")
    else:
        print("Moisture status: HIGH")

    # Soil temperature classification
    if soil_temperature < 15:
        print("Temperature status: LOW")
    elif soil_temperature <= 30:
        print("Temperature status: MODERATE")
    else:
        print("Temperature status: HIGH")

    # Combined monitoring result
    if 30 <= soil_moisture <= 70 and 15 <= soil_temperature <= 30:
        print("Result: Both readings are within the example ranges.")

    elif soil_moisture < 30 and soil_temperature > 30:
        print("Result: Low moisture and high temperature detected.")

    elif soil_moisture < 30:
        print("Result: Low soil moisture detected.")

    elif soil_moisture > 70:
        print("Result: High soil moisture detected.")

    elif soil_temperature < 15:
        print("Result: Low soil temperature detected.")

    else:
        print("Result: High soil temperature detected.")

print("\n=== Monitoring Complete ===")
