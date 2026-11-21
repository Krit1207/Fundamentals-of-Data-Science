
# Q2 - Restaurant Orders and Daily Collection

# Menu with item codes, names and prices
menu = {
    1: ("Momo", 180),
    2: ("Chowmein", 150),
    3: ("Thakali Set", 450),
    4: ("Lassi", 120)
}

# Orders recorded by waiters
orders = ["1:2,4:2", "3:1,1:1,9:3", "2:3,1:2,4:1"]

items_sold = {}
invalid_codes = []
day_total = 0

# Process each table's order
for table_number, order in enumerate(orders, 1):
    subtotal = 0

    # Split order into code and quantity
    for item in order.split(","):
        code, quantity = item.split(":")
        code = int(code)
        quantity = int(quantity)

        # Skip unknown menu codes
        if code not in menu:
            invalid_codes.append(code)
            continue

        name, price = menu[code]

        subtotal += price * quantity

        # Count quantity sold for each item
        if name not in items_sold:
            items_sold[name] = 0

        items_sold[name] += quantity

    # Calculate service charge and VAT
    service_charge = subtotal * 0.10
    vat = (subtotal + service_charge) * 0.13
    final_bill = subtotal + service_charge + vat

    day_total += final_bill

    print(f"Table {table_number}: subtotal Rs {subtotal}, bill with service + VAT Rs {final_bill:.2f}")

# Find the best-selling item
best_seller = max(items_sold, key=items_sold.get)

print("Items sold:", items_sold)
print("Best seller:", best_seller, "| Invalid codes:", invalid_codes)
print(f"Day's collection: Rs {day_total:.2f}")
