fine_rules = {"helmet": 500, "signal": 1000, "speeding": 1500}
total_fine = 0
repeat_count = 0

count = int(input("Enter number of violations: "))
if count < 0:
    print("Invalid number of violations")
else:
    for i in range(count):
        offence = input("Enter offence (helmet/signal/speeding): ").strip().lower()
        repeat = input("Is it a repeat offence? (yes/no): ").strip().lower()

        if offence not in fine_rules or repeat not in ("yes", "no"):
            print("Invalid offence or repeat status")
            continue

        fine = fine_rules[offence]
        if repeat == "yes":
            fine *= 2
            repeat_count += 1

        total_fine += fine
        print("Fine:", fine)

    print("Total penalty:", total_fine)
    if repeat_count >= 3:
        print("Review required under sample policy")
    else:
        print("No review triggered under sample policy")
