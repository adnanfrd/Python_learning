try:
    age = int(input("Enter your age: "))
    print("You entered:", age)
except ValueError:
    print("Invalid input")
