
# Q7 - Glacier Lake Outburst Early Warning

# Lake data: (warning level, danger level, hourly readings)
lakes = {
    "Tsho Rolpa": (20.0, 24.0, [17.2, 17.5, 18.3, 19.0, 20.1, 22.0, 24.4, 25.0]),
    "Imja": (15.0, 18.0, [12.0, 12.1, 12.3, 12.2, 12.6, 13.0, 13.1, 13.3]),
    "Thulagi": (30.0, 33.0, [28.0, 28.9, 29.5, 30.2, 30.4, 30.1, 29.8, 29.6])
}

# Dictionary to group lakes by status
status_groups = {
    "Normal": [],
    "Watch": [],
    "Danger": []
}

for lake, (warning, danger, readings) in lakes.items():

    # Calculate hour-to-hour rises
    rises = []

    for i in range(1, len(readings)):
        rise = round(readings[i] - readings[i - 1], 2)
        rises.append(rise)

    # Find maximum water level and biggest rise
    max_level = max(readings)

    if rises:
        biggest_rise = max(rises)
    else:
        biggest_rise = 0

    # Check lake status using enumerate
    status = "Normal"
    status_hour = 0

    for hour, level in enumerate(readings):
        if level >= danger:
            status = "Danger"
            status_hour = hour
            break

        elif level >= warning and status == "Normal":
            status = "Watch"
            status_hour = hour

    # Check for 3 consecutive rapid rises
    consecutive_rises = 0
    rapid_rise = False

    for rise in rises:
        if rise > 0.5:
            consecutive_rises += 1

            if consecutive_rises >= 3:
                rapid_rise = True
        else:
            consecutive_rises = 0

    # Store lake in its status group
    status_groups[status].append(lake)

    # Prepare status message
    if status == "Normal":
        status_message = "Normal"
    else:
        status_message = f"{status} (from hour {status_hour})"

    if rapid_rise:
        status_message += " + RAPID RISE"

    # Print lake results
    print(
        f"{lake} max {max_level:.1f} m, "
        f"biggest rise {biggest_rise:.1f} m, "
        f"status {status_message}"
    )

# Print grouped lake statuses
print(status_groups)

# Print evacuation messages for danger lakes
for lake in status_groups["Danger"]:
    print("EVACUATE downstream of:", lake)
