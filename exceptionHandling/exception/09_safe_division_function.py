def divide_numbers(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return None

try:
    first_number = float(input("Enter the numerator: "))
    second_number = float(input("Enter the denominator: "))
    answer = divide_numbers(first_number, second_number)
    if answer is None:
        raise ZeroDivisionError
except ValueError:
    print("Both values must be numbers")
except ZeroDivisionError:
    print("The denominator cannot be zero")
else:
    print("Answer:", answer)
