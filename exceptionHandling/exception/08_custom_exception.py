class InsufficientBalanceError(Exception):
    pass

balance = 1000

try:
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= 0:
        raise ValueError("Withdrawal must be greater than zero")
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")
    balance -= amount
except ValueError as error:
    print("Invalid amount:", error)
except InsufficientBalanceError as error:
    print("Withdrawal failed:", error)
else:
    print("Withdrawal successful")
    print("Remaining balance:", balance)
