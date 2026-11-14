crops = [
    {"name": "Tomato", "moisture": 25, "temperature": 22},
    {"name": "Pepper", "moisture": 55, "temperature": 28},
    {"name": "Cucumber", "moisture": 75, "temperature": 24},
    {"name": "Tomato", "moisture": 40, "temperature": 23}
]

for index, crop in enumerate(crops, start=1):

    print(f'{index}. {crop["name"]} {crop["moisture"]}% {crop["temperature"]}°C')    

def calculate_average_moisture(crops):
    if not crops: return 0
    return sum(crop["moisture"] for crop in crops) / len(crops)

def find_lowest_moisture(crops):
    if not crops: return None
    return min(crops, key=lambda x: x["moisture"])

def get_unique_crop_names(crops):
    return {crop["name"] for crop in crops}

def count_low_moisture(crops):
    return sum(1 for crop in crops if crop["moisture"] < 30)


driest = find_lowest_moisture(crops)

print(f'The kind of crops are {get_unique_crop_names(crops)}.')
print(f'The average moisture is {calculate_average_moisture(crops)}%.')
print(f'The driest crop is {driest["name"]} : {driest["moisture"]}%')
print(f"Low moisture readings: {count_low_moisture(crops)}")