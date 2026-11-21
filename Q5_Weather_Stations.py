
# Q5 - Weather Station Rainfall and Flood Watch

# Rainfall data for 7 days (in mm)
rain = {
    "Kathmandu": [0, 12.5, 70.2, 118.0, 40.1, 0, 1.2],
    "Pokhara": [35.0, 88.4, 20.3, 95.0, 5.0, 0, 0],
    "Biratnagar": [0, 0, 2.0, 10.5, 66.0, 210.5, 130.0]
}

heavy_limit = 64.5

station_totals = {}
heavy_stations = set()

# Process rainfall data for each station
for station, daily_rain in rain.items():

    total = sum(daily_rain)
    station_totals[station] = total

    # Count rainy days
    rainy_days = 0
    for amount in daily_rain:
        if amount > 0:
            rainy_days += 1

    # Find peak rainfall and its day number
    peak = max(daily_rain)
    peak_day = daily_rain.index(peak) + 1

    # Check for consecutive heavy rainfall
    consecutive_heavy = 0
    flood_watch = False

    for amount in daily_rain:
        if amount >= heavy_limit:
            heavy_stations.add(station)
            consecutive_heavy += 1

            if consecutive_heavy >= 2:
                flood_watch = True
        else:
            consecutive_heavy = 0

    # Determine station status
    if flood_watch:
        status = "FLOOD WATCH"
    else:
        status = "normal"

    # Print each station's results
    print(
        f"{station:<12} total {total:6.1f} mm, "
        f"rainy days {rainy_days}, "
        f"peak {peak:.1f} mm on day {peak_day}, "
        f"{status}"
    )

# Find the wettest station
wettest_station = max(station_totals, key=station_totals.get)

# Display final results
print("Wettest station:", wettest_station)
print("Stations with heavy rain:", sorted(heavy_stations))
