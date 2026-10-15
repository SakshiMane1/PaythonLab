try:
    balance = 5000

    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    if amount > balance:
        raise Exception("Insufficient balance")

    balance = balance - amount

    print("Withdrawal successful")
    print("Remaining balance =", balance)

except ValueError as e:
    print("Invalid input:", e)

except Exception as e:
    print("Error:", e)

finally:
    print("Thank you for using ATM")