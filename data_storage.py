
import csv
import math
from pathlib import Path

def append_crop_data(crop):

    filename = Path("greenhouse_history.csv")

    fieldnames = [
        "timestamp",
        "name",
        "moisture",
        "temperature"
    ]

    file_is_empty = (
        not filename.exists()
        or filename.stat().st_size == 0
    )

    with open(filename, "a", newline = "", encoding = "utf-8") as file:

        writer = csv.DictWriter(file, fieldnames = fieldnames)

        if file_is_empty:
            writer.writeheader()

        writer.writerow(crop)
    
    print("Sensor reading saved!")


def save_crop_data(crops):

    with open("greenhouse_readings.csv", "w", newline="") as file:

        fieldnames = ["name", "moisture", "temperature"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(crops)

    print("Crop data saved successfully!")


def load_crop_data():

    crops = []

    try:
        with open("greenhouse_readings.csv", "r", newline="") as file:

            reader = csv.DictReader(file)

            # Check required columns
            required_columns = {"name", "moisture", "temperature"}

            if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
                print("Error: CSV is missing required columns.")
                return []

            # Read each crop record
            for row in reader:

                try:
                    crop_name = row["name"].strip()
                    moisture = float(row["moisture"])
                    temperature = float(row["temperature"])

                    # Validate the data
                    if not crop_name:
                        print("Warning: Missing crop name. Skipping row.")
                        continue

                    if not math.isfinite(moisture) or not math.isfinite(temperature):
                        print("Warning: Non-finite sensor reading. Skipping row.")
                        continue

                    crop = {
                        "name": crop_name,
                        "moisture": moisture,
                        "temperature": temperature
                    }

                    crops.append(crop)

                except (ValueError, TypeError):
                    print("Warning: Invalid numeric data. Skipping row.")
                    continue

    except FileNotFoundError:
        print("No saved crop data found.")

    except PermissionError:
        print("Error: Permission denied when accessing the CSV file.")

    return crops
