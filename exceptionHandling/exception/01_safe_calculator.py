try: 
    first = float(input("Enter the first number: ")) 
    operator = input("Enter an operator (+, -, *, /): ") 
    second = float(input("Enter the second number: ")) 
 
    if operator == "+": 
        result = first + second 
    elif operator == "-": 
        result = first - second 
    elif operator == "*": 
        result = first * second 
    elif operator == "/": 
        result = first / second 
    else: 
        raise ValueError("Unknown operator") 
 
except ValueError as error: 
    print("Invalid calculator input:", error) 
except ZeroDivisionError: 
    print("A number cannot be divided by zero") 
else: 
    print("Result:", result) 
finally: 
    print("Calculator finished")