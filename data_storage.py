import csv

def save_crop_data(crops):
    with open("greenhouse_readings.csv", "w", newline="") as file:

        fieldnames = ["name", "moisture", "temperature"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(crops)

    print("Crop data saved successfully!")


def load_crop_data():

    crops = []

    with open("greenhouse_readings.csv", "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            crop = {
                "name" : row["name"],
                "moisture": float(row["moisture"]),
                "temperature": float(row["temperature"])
            }

            crops.append(crop)

    return crops