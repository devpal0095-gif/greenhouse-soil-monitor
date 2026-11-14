class Crop:
    def __init__(self, name, moisture, temperature):
        self.name = name
        self.moisture = moisture
        self.temperature = temperature

    def is_low_moisture(self):
        return self.moisture < 30

def calculate_average_moisture(crops):
    if not crops: return None  # Fixed to match your test
    return sum(c["moisture"] for c in crops) / len(crops)

def find_lowest_moisture(crops):
    if not crops: return None
    return min(crops, key=lambda x: x["moisture"])

def find_all_driest_crops(crops):
    if not crops: return []
    min_moisture = min(c["moisture"] for c in crops)
    return [c for c in crops if c["moisture"] == min_moisture]

def get_unique_crop_names(crops):
    return {c["name"] for c in crops}

def count_low_moisture(crops):
    return sum(1 for c in crops if c["moisture"] < 30)

# --- EXECUTION & TESTS ---

# Test 1: Empty lists
assert find_lowest_moisture([]) is None
assert calculate_average_moisture([]) is None
assert find_all_driest_crops([]) == []

# Test 2: Unique names & Displaying
crops = [
    {"name": "Tomato", "moisture": 20, "temperature": 22},
    {"name": "Pepper", "moisture": 20, "temperature": 24},
    {"name": "Pepper", "moisture": 55, "temperature": 28}
]

for index, crop in enumerate(crops, start=1):
    print(f'{index}. {crop["name"]} {crop["moisture"]}% {crop["temperature"]}°C')    

driest_crops = find_all_driest_crops(crops)

if driest_crops:
    print("Crops with the lowest moisture:")

    for crop in driest_crops:
        print(f'{crop["name"]}: {crop["moisture"]}%')
else:
    print("No crop readings available.")

assert get_unique_crop_names(crops) == {"Tomato", "Pepper"}

# Test 3: Tied lowest readings
assert len(find_all_driest_crops(crops)) == 2

# Test 4: Boundary values (using the Crop class)
assert Crop("Tomato", 29.9, 22).is_low_moisture() is True
assert Crop("Pepper", 30, 25).is_low_moisture() is False

print("\nAll Day 10 tests passed!")