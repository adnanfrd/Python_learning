# Program 1: Write to file
with open("data.txt", "w") as f:
    f.write("Hello, Python!, how are you !")

# Program 2: Read from file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)