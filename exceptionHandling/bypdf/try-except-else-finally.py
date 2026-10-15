try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Enter valid numbers!")

else:
    print("Result =", result)

finally:
    print("Execution complete.")