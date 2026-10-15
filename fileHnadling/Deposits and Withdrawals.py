with open("transactions.txt", "r") as file:
    lines = file.readlines()

total_deposit = 0
total_withdrawal = 0
transactions = []

for line in lines:
    transaction_type, amount = line.strip().split(",")

    amount = float(amount)

    transactions.append(amount)

    if transaction_type == "D":
        total_deposit += amount

    elif transaction_type == "W":
        total_withdrawal += amount

final_balance = total_deposit - total_withdrawal
largest_transaction = max(transactions)

print("Total Deposits:", total_deposit)
print("Total Withdrawals:", total_withdrawal)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)