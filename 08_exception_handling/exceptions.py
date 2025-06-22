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


# Program 1: Handle file not found
try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")

# Program 2: Multiple exception types
try:
    num = int("abc")
except ValueError:
    print("Cannot convert to integer.")
except Exception as e:
    print("Other error:", e)