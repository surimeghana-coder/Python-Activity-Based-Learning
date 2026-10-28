total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))
required = float(input("Enter required attendance percentage: "))

if total <= 0 or attended < 0 or attended > total or not 0 <= required <= 100:
    print("Invalid input")
else:
    percentage = attended / total * 100
    print("Current attendance:", round(percentage, 2), "%")

    extra = 0
    while (attended + extra) / (total + extra) * 100 < required:
        extra += 1

    if extra == 0:
        print("Attendance requirement satisfied")
    else:
        print("Additional classes needed:", extra)
