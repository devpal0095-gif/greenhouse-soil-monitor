# Greenhouse Soil Monitor For Education 🌱

A beginner-friendly Python project for monitoring soil moisture and soil temperature in greenhouse farming.

This project is part of study journey toward becoming a **Digital Agriculture Engineer**. It focuses on applying Python programming fundamentals to practical agricultural monitoring problems.

## Features

- **Soil Moisture Monitoring:** Classifies moisture readings as low, moderate, or high.
- **Soil Temperature Monitoring:** Evaluates soil temperature readings in degrees Celsius.
- **Combined Monitoring:** Checks both moisture and temperature conditions.
- **Input Validation:** Checks whether numerical readings fall within defined limits.
- **Crop Identification:** Allows users to enter the crop being monitored.
- **Monitoring Reports:** Displays measurement values, classifications, and status messages.

## Project Structure

```text
greenhouse-soil-monitor/
├── soil_moisture_monitor.py
├── soil_temperature_monitor.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3.13
- A terminal or code editor such as VS Code

No external Python libraries are required.

## Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/devpal0095-gif/greenhouse-soil-monitor.git
```

**2. Open the project directory**

```bash
cd greenhouse-soil-monitor
```

**3. Run the soil moisture monitor**

```bash
python soil_moisture_monitor.py
```

**4. Run the soil temperature monitor**

```bash
python soil_temperature_monitor.py
```

## Example Output

### Soil Moisture and Temperature Monitoring

```text
=== Greenhouse Soil Moisture Monitor ===
Enter crop name: Tomato
Enter soil moisture (%): 45
Enter soil temperature (°C): 22

--- Soil Monitoring Report ---
Crop: Tomato
Soil moisture: 45.00%
Soil temperature: 22.00°C
Moisture status: MODERATE
Temperature status: MODERATE
Result: Both readings are within the example ranges.

=== Monitoring Complete ===
```

## Monitoring Thresholds

The current program uses illustrative ranges for learning Python conditional statements.

| Measurement | Low | Moderate | High |
|---|---|---|---|
| Soil moisture | Below 30% | 30–70% | Above 70% |
| Soil temperature | Below 15°C | 15–30°C | Above 30°C |

**Important:** These thresholds are programming examples, not validated crop-specific agricultural recommendations. Actual monitoring thresholds depend on crop species, growth stage, soil properties, and sensor measurement methods.

## Technologies Used

- Python 3.13
- Visual Studio Code
- Git
- GitHub

## Future Improvements

- [ ] Add crop-specific monitoring configurations.
- [ ] Improve handling of invalid and nonnumeric inputs.
- [ ] Save monitoring records to CSV files.
- [ ] Add historical charts and data visualization.
- [ ] Integrate real soil moisture and temperature sensors.
- [ ] Build an interactive greenhouse monitoring dashboard.
- [ ] Add automated tests.

## Project Status

**In Development — Day 5 Python Fundamentals**

Currently focused on conditional statements, logical operators, and input validation.

## Author

**GitHub:** [devpal0095-gif](https://github.com/devpal0095-gif)

## License

No license has been selected yet. All rights are reserved unless a license is added.

---

*Learning Python through practical agricultural engineering projects.*
