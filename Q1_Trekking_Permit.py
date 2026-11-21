
# Q1 - Trekking Permit Counter

fees = {
    "Everest": {"Nepali": 100, "SAARC": 1500, "Foreign": 3000},
    "Annapurna": {"Nepali": 100, "SAARC": 1000, "Foreign": 3000},
    "Langtang": {"Nepali": 100, "SAARC": 1500, "Foreign": 3000}
}

visitors = [
    ("Aarav", "Nepali", 22, "Everest"),
    ("Emma", "Foreign", 34, "Annapurna"),
    ("Rahul", "SAARC", 8, "Langtang"),
    ("John", "Foreign", 65, "Everest"),
    ("Mina", "Nepali", 30, "Annapurna"),
    ("Li", "Foreign", 28, "Everest")
]

revenue = {}
visitor_count = {}
categories = set()

for area in fees:
    revenue[area] = 0
    visitor_count[area] = 0

for name, category, age, area in visitors:
    fee = fees[area][category]

    if age < 10:
        fee = 0
    elif age >= 60:
        fee = fee // 2

    revenue[area] += fee
    visitor_count[area] += 1
    categories.add(category)

    print(name, area, "Rs", fee)

busiest = max(visitor_count, key=visitor_count.get)
total_revenue = sum(revenue.values())

print("Revenue by area:", revenue)
print("Busiest area:", busiest, f"({visitor_count[busiest]} visitors)")
print("Visitor categories:", sorted(categories))
print("Total revenue: Rs", total_revenue)
