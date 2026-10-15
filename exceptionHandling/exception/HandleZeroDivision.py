try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    a=10;
    b=0;
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")