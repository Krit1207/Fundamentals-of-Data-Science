
# Q9 - Smart Nepal Electricity Meters

# Cumulative meter readings for each household
meters = {
    "H-101": [1200, 1265, 1340, 1520, 1590],
    "H-102": [880, 910, 945, 975, 1010],
    "H-103": [2300, 2420, 2470, 2530, 2700]
}

# Electricity slabs: (units in slab, rate)
slabs = [
    (20, 4),
    (30, 7),
    (50, 9),
    (float("inf"), 11)
]

total_revenue = 0
spikes = []

# Process each household
for household, readings in meters.items():

    # Calculate monthly consumption
    monthly_units = []

    for i in range(1, len(readings)):
        consumption = readings[i] - readings[i - 1]
        monthly_units.append(consumption)

    # Calculate average monthly consumption
    if monthly_units:
        average = sum(monthly_units) / len(monthly_units)
        latest_units = monthly_units[-1]
    else:
        average = 0
        latest_units = 0

    # Calculate latest bill using electricity slabs
    remaining_units = latest_units
    bill = 0

    for slab_units, rate in slabs:
        units_used = min(remaining_units, slab_units)

        bill += units_used * rate
        remaining_units -= units_used

        if remaining_units <= 0:
            break

    total_revenue += bill

    # Print household consumption and bill
    print(
        f"{household}: monthly units {monthly_units}, "
        f"avg {average:.1f}, latest bill Rs {bill}"
    )

    # Find consumption spikes greater than 50%
    for i in range(1, len(monthly_units)):
        previous = monthly_units[i - 1]
        current = monthly_units[i]

        if previous > 0 and current > previous * 1.5:
            spikes.append(
                (household, i + 1, previous, current)
            )

# Display consumption spikes
print("Spikes (>50% jump):")

for household, month, previous, current in spikes:
    print(
        f"  {household} month {month}: "
        f"{previous} -> {current} units"
    )

# Display total revenue
print("Total latest-month revenue: Rs", total_revenue)
