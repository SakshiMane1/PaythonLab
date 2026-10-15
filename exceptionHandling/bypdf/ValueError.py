try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Please enter a valid number!")