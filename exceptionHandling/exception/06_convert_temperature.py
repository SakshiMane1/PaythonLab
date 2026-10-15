try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
except ValueError:
    print("Temperature must be a number")
else:
    print("Temperature in Fahrenheit:", fahrenheit)
finally:
    print("Temperature conversion finished")
