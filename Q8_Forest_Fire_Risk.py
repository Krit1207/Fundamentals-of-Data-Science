
# Q8 - Forest Fire Risk by District and Province

# Given district data:
# (district, province, temperature, humidity, wind speed, days since rain)

districts = [
    ("Chitwan", "Bagmati", 36, 18, 25, 40),
    ("Dang", "Lumbini", 33, 30, 35, 20),
    ("Kaski", "Gandaki", 27, 55, 10, 5),
    ("Bardiya", "Lumbini", 38, 15, 32, 35),
    ("Makwanpur", "Bagmati", 31, 40, 18, 12),
    ("Ilam", "Koshi", 24, 70, 8, 3)
]

# Dictionary to group districts by risk level
risk_groups = {
    "Low": [],
    "Moderate": [],
    "High": [],
    "Extreme": []
}

# Set to store provinces needing alerts
alert_provinces = set()

# Process each district using tuple unpacking
for district, province, temp, humidity, wind, days in districts:

    score = 0

    # Temperature score
    if temp > 35:
        score += 3
    elif temp > 30:
        score += 2
    elif temp > 25:
        score += 1

    # Humidity score
    if humidity < 20:
        score += 3
    elif humidity < 35:
        score += 2
    elif humidity < 50:
        score += 1

    # Wind speed score
    if wind > 30:
        score += 2
    elif wind > 15:
        score += 1

    # Days since rain score
    if days > 30:
        score += 3
    elif days > 14:
        score += 2
    elif days > 7:
        score += 1

    # Determine risk level
    if score >= 9:
        risk = "Extreme"
    elif score >= 7:
        risk = "High"
    elif score >= 4:
        risk = "Moderate"
    else:
        risk = "Low"

    # Store district and score as a tuple
    risk_groups[risk].append((district, score))

    # Collect provinces with High or Extreme risk
    if risk == "High" or risk == "Extreme":
        alert_provinces.add(province)

# Print districts grouped by risk level
for risk, district_list in risk_groups.items():
    print(f"{risk:<10}: {district_list}")

# Print provinces needing alerts
print("Provinces to alert:", sorted(alert_provinces))
