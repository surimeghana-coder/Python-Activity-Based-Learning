prepared = [100, 120, 90, 150, 110]
served = [85, 100, 80, 120, 95]
limit = 15

total_prepared = 0
total_served = 0
total_waste = 0

for i in range(len(prepared)):
    if prepared[i] <= 0 or served[i] < 0 or served[i] > prepared[i]:
        print("Invalid data for day", i + 1)
        continue

    waste = prepared[i] - served[i]
    percentage = waste / prepared[i] * 100
    total_prepared += prepared[i]
    total_served += served[i]
    total_waste += waste

    print("Day", i + 1, "- prepared:", prepared[i],
          "served:", served[i], "waste:", waste,
          "waste percentage:", round(percentage, 2), "%")
    if percentage > limit:
        print("Warning: waste exceeds the acceptable limit")

print("Total prepared:", total_prepared)
print("Total served:", total_served)
print("Total wasted:", total_waste)
if total_prepared > 0:
    print("Overall waste percentage:", round(total_waste / total_prepared * 100, 2), "%")
