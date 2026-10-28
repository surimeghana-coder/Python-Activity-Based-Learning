days = int(input("Enter number of days (28-31): "))
start = int(input("Starting weekday (0=Mon, 6=Sun): "))

if days < 28 or days > 31 or start < 0 or start > 6:
    print("Invalid calendar details")
else:
    print("Mon Tue Wed Thu Fri Sat Sun")
    position = start

    print("    " * start, end="")
    for day in range(1, days + 1):
        print(f"{day:3} ", end="")
        position += 1
        if position == 7:
            print()
            position = 0

    if position != 0:
        print()
