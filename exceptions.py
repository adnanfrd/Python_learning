# Program 1: Divide by zero
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


# Program 2: Input validation
try:
    age = int(input("Enter your age: "))
    print("You entered:", age)
except ValueError:
    print("Invalid input")