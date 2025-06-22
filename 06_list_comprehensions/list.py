# Program 1: Create a list of cubes
cubes = [x**3 for x in range(1, 6)]
print("Cubes:", cubes)


# Program 2: Filter names starting with A
names = ["Ali", "Sara", "Ahmed", "John"]
a_names = [name for name in names if name.startswith("A")]
print("A names:", a_names)
