try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Enter a valid number!")

else:
    print("Result =", result)