balance = float(input("Enter opening balance: "))
count = int(input("Enter number of transactions: "))
limit = 10000
history = []

if balance < 0 or count < 0:
    print("Invalid opening balance or transaction count")
else:
    for i in range(count):
        kind = input("Enter deposit or withdraw: ").strip().lower()
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Invalid amount")
        elif kind == "deposit":
            balance += amount
            history.append(("Deposit", amount))
            print("Deposit successful")
        elif kind == "withdraw":
            if amount > limit:
                print("Withdrawal limit exceeded")
            elif amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
                history.append(("Withdrawal", amount))
                print("Withdrawal successful")
        else:
            print("Invalid transaction type")

    print("\nTransaction Summary")
    for kind, amount in history:
        print(kind, ":", round(amount, 2))
    print("Final balance:", round(balance, 2))
