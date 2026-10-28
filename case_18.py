distance = float(input("Enter journey distance in km: "))
fuel_price = float(input("Enter fuel price per litre: "))
reserve = float(input("Enter reserve fuel in litres: "))

vehicles = [("Car A", 15), ("Car B", 20), ("Car C", 12)]

if distance <= 0 or fuel_price <= 0 or reserve < 0:
    print("Invalid input")
else:
    best_vehicle = ""
    lowest_cost = float("inf")

    for name, mileage in vehicles:
        journey_fuel = distance / mileage
        total_fuel = journey_fuel + reserve
        cost = total_fuel * fuel_price
        print(name, "- fuel:", round(total_fuel, 2), "litres; cost:", round(cost, 2))

        if cost < lowest_cost:
            lowest_cost = cost
            best_vehicle = name

    print("Most economical vehicle:", best_vehicle)
    print("Minimum estimated cost:", round(lowest_cost, 2))
