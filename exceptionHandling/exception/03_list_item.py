colors = ["red", "green", "blue", "yellow"]

try:
    position = int(input("Enter a list position: "))
    print("Selected color:", colors[position])
except ValueError:
    print("Please enter a whole number")
except IndexError:
    print("That list position does not exist")
